import os
import sys
import tkinter
from tkcalendar import DateEntry
from tkinter import BOTTOM, CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter import messagebox
import customtkinter
from tkinter.messagebox import showinfo
from turtle import width
sys.path.append('..')#this is importent when you import some thing in other folder
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk
from database import connects


class Emp:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
         
            my_conn = connects()
            cur=my_conn.cursor()
            # Creating tkinter my_w
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width/2,scr_height/2))
            my_w.title("l'inforamtion du client")  
            my_w.tk.call('encoding','system','utf-8')
            my_w.resizable(0,0)
            #style
            # Add Some Style
            style = ttk.Style()
            # Pick A Theme
            style.theme_use('default')
            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
            with open("login.txt") as file:
                fl=file.read()
            
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=0,y=0,width=1400,height=500)
            title=customtkinter.CTkLabel(frame1,text_color="white",text="L'information du traveileur au system معلومات العمال المستعملين لتطبيق ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=0,y=0)
            
            def rel():
                my_w.destroy()
                os.system("py emp.py")
            
            # sr=customtkinter.CTkButton(master=my_w,text_color="white", text="relod",command=rel, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            # sr.place(x=0,y=50)
                          
            # def info():
            q="SELECT *,count(emploiyer) as total from client where emploiyer =%s "
            cur.execute(q,fl)
            res=cur.fetchall()
            for dt in res:
                a=dt['total']
                title=Label(my_w,text="Clock",font=("\nBook Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
                title.place(x=0,y=80)
                title.config(text=f"l'emploiyer {str(fl)} a registrer\n{str(a)} clients")
            q1="SELECT *,count(emploiyer) as total from message where emploiyer =%s "
            cur.execute(q1,fl)
            res1=cur.fetchall()
            for dt in res:
                a=dt['total']
                title1=Label(my_w,text="Clock",font=("\nBook Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
                title1.place(x=0,y=150)
                title1.config(text=f"l'emploiyer {str(fl)} a registrer\n{str(a)} messages")
            
# my_w =customtkinter.CTk()
# my_w1=Emp(my_w)
# my_w.mainloop()




'''import os
import sys
import tkinter
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter import messagebox
import customtkinter
from tkinter.messagebox import showinfo
from turtle import width
sys.path.append('..')#this is importent when you import some thing in other folder
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk
from database import connects


class Emp:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
         
            my_conn = connects()
            cur=my_conn.cursor()
            # Creating tkinter my_w
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width,scr_height))
            my_w.title("l'inforamtion du client")  
            my_w.tk.call('encoding','system','utf-8')
            my_w.resizable(0,0)
            #style
            # Add Some Style
            style = ttk.Style()
            # Pick A Theme
            style.theme_use('default')
            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
            with open("../login.txt") as file:
                fl=file.read()
            
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=10,y=350,width=1400,height=500)
            title=customtkinter.CTkLabel(frame1,text_color="white",text="L'information du traveileur au system معلومات العمال المستعملين لتطبيق ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=400,y=170)
            
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=500)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher phone ,nom...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=500,width=250)
            def rel():
                my_w.destroy()
                os.system("py emp.py")

            def serch():
                """
                 used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %
                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from client where emploiyer like %s order by (emploiyer) desc"
                cur.execute(q,(serchE.get()+"%",))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['emploiyer'],dt['total']))
                    
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=500)
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="relod",command=rel, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=550)
                          
            global trv
            trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1","2"),show='headings')
            trv.grid(row=10, column=0, sticky='nsew')

            # width of columns and alignment 
            trv.heading("0", text ="id")
            trv.heading("1", text ="emploiyer")
            trv.heading("2", text ="total")
            #nom,prenom,numero,telephone,direction,prix,date
            # Headings  
            # respective columns 
            trv.heading("0", text ="id")
            trv.heading("1", text ="emploiyer")
            trv.heading("2", text ="total")
            
            # add a scrollbar
            scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
            trv.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=10, column=1, sticky='ns')
            # # getting data from MySQL student table 
            # r_set=cur.execute("SELECT * from client ")
            # res=cur.fetchall()
            q="SELECT id ,emploiyer,count(emploiyer) as total from client where emploiyer=%s order by id desc "
            q2="SELECT * from login where username=%s"
            cur.execute(q2,fl)
            res1=cur.fetchall()
            for i in res1:
                print(i)
            cur.execute(q,fl)
            res=cur.fetchall()

            for dt in res:
                trv.insert("", 'end',iid=dt['id'], text=dt['id'],values =(dt['id'],dt['emploiyer'],dt['total']))
                # trv.insert("", 'end',iid=dt['id'], text=dt['id'],values =(dt['id'],dt['username'],dt['password']))


#----------------------functions---------------
            def retour():
                my_w.destroy()
            # serch()
            
            




# my_w =customtkinter.CTk()
# my_w1=Emp(my_w)
# my_w.mainloop()
'''