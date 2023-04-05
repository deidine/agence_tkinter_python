import customtkinter
from tkinter import scrolledtext as st
import tempfile,os
import os,sys
sys.path.append("..") #this is importent when you import some thing in other folder
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
from database import connects
from img import imagePath

from tabulate import tabulate
from agc_tamplate import template_long


class CherRes:
    """
    if you dont put self behind eny image will not import in others folder \n
    this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()
        scr_height=self.root.winfo_screenheight()
        self.root.geometry("%ix%i+0+0"% (scr_width,scr_height)) # Setting width
        self.root.title("Registration Window")
        self.root.config(bg="white")
        self.root.resizable(width=False, height=False)# self.root.resizable(width=False, height=False)
        scr_width=root.winfo_screenwidth()
        scr_height=root.winfo_screenheight()

        frame1=Frame(self.root)
        frame1.place(x=0,y=0,width=scr_width,height=scr_height)

        text_ear=st.ScrolledText(frame1,width=140,height=40)
        text_ear.place(x=0,y=0)

        def retour():
            self.root.destroy()
        def table():
                conn=connects()
                cur=conn.cursor()
                q="SELECT numero as chaise,nom, depart , telephone ,  prix , date ,bus_num as bus_numero ,emploiyer ,direction ,payer  from client where date=CURRENT_DATE()  order by (id) desc "
                cur.execute(q)
                res=cur.fetchall()
                txt=template_long()
                txt+="\t\t"+" حدد كل من  رقم الباص و رقم المقعد وتاريخ الحجز" +"\n"
                txt+="\n"+"_"*80+"\n"
                txt+=tabulate(res,headers='keys',tablefmt="rounded_grid")
                txt+="\n"
                text_ear.insert(END,txt)
        table()
        numL=customtkinter.CTkLabel(frame1,text="NUMERO chaise رقم المقعد", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=1100,y=300)
        num=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        num["values"]=("1"," 2"," 3"," 4","5","6","7","8","9","10","12","13","14","15")
        num.place(x=1100,y=350,width=50) 
        num.current(0) 
        bus_numl=customtkinter.CTkLabel(frame1,text="numero bus رقم الباص", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=1100,y=200)
        
        cmb_depart=ttk.Combobox(frame1,font=("times new roman",16), state="readonly", justify=CENTER)
        cmb_depart["values"]=("matin","soir")
        cmb_depart.place(x=1100,y=100,width=scr_width/8)
        cmb_depart.current(0)

        cmb_bus_num=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_bus_num["values"]=("1"," 2"," 3"," 4","5","6","7","8","9","10")
        cmb_bus_num.place(x=1100,y=250,width=50) 
        cmb_bus_num.current(0)
        def serch():
            """
                used for finding spesific data in treeview\n
            this serchE.get()+"%" because you can't write in sql code like % %s %
            """
    
            conn=connects()
            cur=conn.cursor()
            q="SELECT numero as chaise,nom,depart,telephone, prix,date,bus_num as bus_numero ,emploiyer ,direction ,payer from client where depart like %s and bus_num like %s and numero like %s and date=CURRENT_DATE()  order by (id) desc"
            cur.execute(q,("%"+cmb_depart.get()+"%","%"+cmb_bus_num.get()+"%","%"+num.get()+"%"))
            res=cur.fetchall()
            text_ear.delete('1.0',END)
            txt=template_long()
            txt+="\t\t"+" حدد كل من  رقم الباص و رقم المقعد وتاريخ الحجز" +"\n"
            txt+="\n"+"_"*80+"\n"
            txt+=tabulate(res,headers='keys',tablefmt="rounded_grid")
            txt+="\n"
            text_ear.insert(END,txt)
    
        sr=customtkinter.CTkButton(master=root,text_color="white",text_font=(20), text="بحث",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
        sr.place(x=1250,y=450)

# root=customtkinter.CTk()
# obj=CherRes(root)
# root.mainloop()
