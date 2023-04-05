import tkinter as tk
from tkhtmlview import HTMLText, RenderHTML
import customtkinter
from tkinter import scrolledtext as st
import tempfile,os
from time import strftime
import webbrowser

import os,sys
sys.path.append("..") #this is importent when you import some thing in other folder
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk,Toplevel
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
from database import connects
from img import imagePath,logotiket
from agc_tamplate import template,footer
class Register:
    """
    if you dont put self behind eny image will not import in others folder \n
    # this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()/2+50
        scr_height=self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+200+100"% (scr_width,scr_height)) # Setting width
        self.root.title("Registration Window")
        self.root.resizable(width=False, height=False)# self.root.resizable(width=False, height=False)
        self.root.config(bg="beige",)

        #***********Bg Image***********
        # self.bg=ImageTk.PhotoImage(file=imagePath()+"b2.jpg",master=self.root)
        # self.bg=ImageTk.PhotoImage(file="../images/b2.jpg",master=self.root)

        # bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #***********Register Frame***********
        
        scr_width=root.winfo_screenwidth()
        scr_height=root.winfo_screenheight()
        frame1=Frame(self.root,bg="beige")
        frame1.place(x=10,y=10,width=scr_width/2-20,height=scr_height*0.65)
        frame2=Frame(self.root)
        frame2.place(x=800,y=10,width=700,height=500)

        #***********Row1***********
        noml=customtkinter.CTkLabel(frame1,text="NOM du passageur اسم المسافر", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=100)
        nom=customtkinter.CTkEntry(frame1,placeholder_text="Nom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        nom.place(x=50,y=130,width=scr_width/6) 
        cmb_depart=ttk.Combobox(frame1,font=("times new roman",16), state="readonly", justify=CENTER)
        cmb_depart["values"]=("matin","soir")
        cmb_depart.place(x=370,y=130,width=scr_width/8)
        cmb_depart.current(0)
        #***********Row2***********
      
        
        telel=customtkinter.CTkLabel(frame1,text="Numero Telephone الهاتف", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=170)
        tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15))
        tele.place(x=50,y=200,width=scr_width/8) 
        

        numL=customtkinter.CTkLabel(frame1,text="NUMERO chaise رقم المقعد", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=170)
        num=ttk.Combobox(frame1,font=("times new roman",13),state="readonly", justify=CENTER)
        num["values"]=("1"," 2"," 3"," 4","  5"," 6","7","8","9","10","12","13","14","15")
        num.place(x=370,y=200,width=50) 
        num.current(0) 
#reloadfunction
            
        def reload():
            self.root.destroy()
            os.system("py enclient.py")
        #***********Row3***********
        directioinl=customtkinter.CTkLabel(frame1,text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=240)
        cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_dir["values"]=("Selection","noikchott","atar","noidibou","nema")
        cmb_dir.place(x=50,y=270,width=scr_width/8) 
        cmb_dir.current(0)
        bus_numl=customtkinter.CTkLabel(frame1,text="numero bus رقم الباص", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=300)

        cmb_bus_num=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
     
        cmb_bus_num.place(x=50,y=340,width=150) 
  
        datel=customtkinter.CTkLabel(frame1,text="Date now تاريخ اليوم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=240)
        date=DateEntry(frame1,selectmode='day',font=("times new roman",15),fg="black",bg="white")
        date.place(x=370,y=270,width=scr_width/8) 

        #***********Row4***********

        prixl=customtkinter.CTkLabel(frame1,text="prix De Ticket", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=250,y=310)
        prix=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        prix.place(x=300,y=340,width=90)
        cmb_prix=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_prix["values"]=("✅","❌")
        cmb_prix.place(x=400,y=340,width=50)
        cmb_prix.current(0)
        prix.insert(END,"5000")
        tele.delete(0,END)
        num.delete(0,END)
        cmb_dir.current(0)
        
        text_ear=st.ScrolledText(frame2,width=40,height=20)
        text_ear.place(x=50,y=50)

        def chaise():
                from agc_tamplate import template_long
                from tabulate import tabulate

                topchaise=Toplevel()
                scr_width=topchaise.winfo_screenwidth()
                scr_height=topchaise.winfo_screenheight()
                topchaise.geometry("%ix%i+0+0"% (scr_width,scr_height/2+60))
                frame1=Frame(topchaise)
                frame1.place(x=0,y=0,width=scr_width,height=scr_height)

                text_ear=st.ScrolledText(frame1,width=140,height=40)
                text_ear.place(x=0,y=0)

                def retour():
                    self.root.destroy()
                def table():
                        conn=connects()
                        cur=conn.cursor()
                        q="SELECT numero as chaise,nom, depart , telephone ,  prix , date ,bus_no as bus_numero ,emploiyer ,direction ,payer  from client where date=CURRENT_DATE()  order by (id) desc "
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
                    q="SELECT numero as chaise,nom,depart,telephone, prix,date,bus_no as bus_numero ,emploiyer ,direction ,payer from client where depart like %s and bus_num like %s and numero like %s and date=CURRENT_DATE()  order by (id) desc"
                    cur.execute(q,("%"+cmb_depart.get()+"%","%"+cmb_bus_num.get()+"%","%"+num.get()+"%"))
                    res=cur.fetchall()
                    text_ear.delete('1.0',END)
                    txt=template_long()
                    txt+="\t\t"+" حدد كل من  رقم الباص و رقم المقعد وتاريخ الحجز" +"\n"
                    txt+="\n"+"_"*80+"\n"
                    txt+=tabulate(res,headers='keys',tablefmt="rounded_grid")
                    txt+="\n"
                    text_ear.insert(END,txt)
            
                sr=customtkinter.CTkButton(master=topchaise,text_color="white",text_font=(20), text="بحث",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
                sr.place(x=1150,y=400)


        def clear():
            nom.delete(0,END)
            tele.delete(0,END)
            num.delete(0,END)
            cmb_dir.current(0)
            cmb_prix.current(0)
        def write():
            

            html='''<html>
            <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>Document</title>
                        <style>
.box {display: flex;justify-content: center;align-items: center;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
flex-wrap: wrap;background-color: rgba(0,0,0,0.4);backdrop-filter: blur(10px);}
.ticket {width: 600px;height: 490px;padding-top: 10px;transform: scale(0.8);}
.label {display: inline-block;justify-content: center;align-items: center;
font-size: 16px;font-weight: bold;}
.serial {height: 30px;display: flex;justify-content: center;align-items: center;border-bottom: 1px solid #000;
font-size: 20px;font-weight: 300;}
.rate {margin: auto;height: 30px;display: flex;justify-content: center;align-items: center;border-bottom: 1px solid #000;
font-size: 16px;font-weight: bold;}
.grid_wrapper {padding: 2px 5px;}
.grid {display: grid;
  grid-template-columns: 0.5fr 1fr 1fr 1fr 0.5fr;
grid-template-rows: repeat(8, 40px);/*grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr*/;
gap: 0px 0px;grid-template-areas:
"name . . . message""name . . . message""name . . . message""name . . . message""name . . . message ""number . . . date";
width: auto;height: auto;text-align: center;border: 1px solid rgba(0, 0, 0, 0.8);border-bottom: 0;}
.name {grid-area: name;border-right: 1px solid black;
border-bottom: 1px solid rgba(0, 0, 0, 0.8);writing-mode: vertical-rl;text-orientation: mixed;}
.message {grid-area: message;display: inline-block; padding-top: 10px ;
  padding-bottom: 10px;
border-left: 1px solid rgba(0, 0, 0, 0.8);border-bottom: 1px solid rgba(0, 0, 0, 0.8);writing-mode: vertical-rl;text-orientation: mixed;}
.number {border-left: 1px solid black;width: 200px;border-right: 1px solid black;border-bottom: 1px solid rgba(0, 0, 0, 0.8);display: inline-block;justify-content: center;
align-items: center;font-size: 20px;}/* Colors */
.date {float: left;
  padding-top: 10px ;
  padding-bottom: 10px;
  width: auto; grid-area: date;
border-left: 1px solid rgba(0, 0, 0, 0.8);
writing-mode: horizontal-tb;text-orientation:mixed;}
.yellow {background-color: #c2b27e;} 
</style></head><body onload="window.print()">
            <div class="box"><!-- ticket 1 -->
            <div class="ticket yellow">
            '''+logotiket()+'''
            <div class="serial">رقم الباص'''+cmb_bus_num.get()+'''</div><div class="rate">الوجهة'''+cmb_dir.get()+'''  '''+cmb_depart.get()+'''
            </div><div class="grid_wrapper"><div class="grid">
            <div class="name">لا نتحمل المسؤلية بعد 15 يوم <br> aucun responsabiliter apres 15 jours</div>
            <div class="number">إسم المسافر</div>
            <div class="number">'''+nom.get()+'''</div><br>
            <div class="number">الهاتف</div>
            <div class="number">'''+tele.get()+'''</div><br>
            <div class="number">رقم المقعد</div>
            <div class="number">'''+num.get()+'''</div><br>
            <div class="number">السعر</div>
            <div class="number">'''+prix.get()+'''</div><br>
            <div class="number">دفع</div>
            <div class="number">'''+cmb_prix.get()+'''</div><br>
            <div class="message">🌝 رقم مبرمج التطبيق 49619609 </div></div></div>
            '''
            time=strftime('%m-%d-%Y')
            dat="DATE D'IMPRIMATION:\t"+str(time)+"\t:تاريخ الطباعة "
            html+='''<div class="date">'''+dat+''' </div>  </div>  
                </body>'''
            file=open("tiket.html","w",encoding='utf-8')
            file.write(html)
            file.close()
            
            
        def print_text():
            a=text_ear.get('1.0',END)
            with open("enreg.txt","w",encoding='utf-8') as dd:
                dd.write(a)
                dd.close()

                
            # os.startfile("enreg.txt","print")

        btn1=Button(frame2,text='print',command=lambda: print_text(text_ear.get('1.0',END)))
        btn1.place(x=400,y=300)
        btn1=Button(frame2,text='reload',command=reload)
        btn1.place(x=450,y=300)
        btn=Button(frame2,text='write',command=write)
        btn.place(x=200,y=300)
#==================================================================

        def register_data():
            """test if the user enter  only the number 
            in telephone and numero chaise"""
            numVal=int(num.get())
            teleVal=tele.get()
            if nom.get()==""  or teleVal=="" or  cmb_dir.get()=="Selection"  or prix.get()=="" or num.get()=="":
                messagebox.showerror("Error", "tous les champs sont obligatoire", parent=root)
            else:
                try:
                        if teleVal.isdigit():
                            n=numVal
                            with open("login.txt") as file:
                                f=file.read()
                            t=tele.get()
                            con=connects()
                            cur=con.cursor()
                        else: 
                            messagebox.showerror("Error", "numero du chaise ou numero de telephone doit etre des nombre", parent=self.root)
                        cur.execute("insert into client (depart,bus_no,imprimer,nom,numero,telephone,direction,prix,date,payer,emploiyer) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (cmb_depart.get(),cmb_bus_num.get(),"✔",
                            nom.get(),
                            n,
                            t,
                            cmb_dir.get(),
                            prix.get(),
                            date.get_date(),
                            cmb_prix.get(),f
                        ))
                        con.commit()
                        con.close()
                        write()
                        print_text()
                        op=messagebox.askyesno("imprimer","tu veux imprimer",parent=root)
                        if op==True:
                            # from htmlpg import webPage
                            # webPage("tiket.html")
                            webbrowser.open("tiket.html")
                            # os.startfile("tiket.html","print")

                            clear()
                        else :
                            clear()
                         

                        

                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

        btn1=customtkinter.CTkButton(master=self.root,text="حالة المقاعد",text_font=(15),    command=chaise,width=scr_width/8, height=scr_height/18,text_color="black", compound="right",hover_color="dimgray",fg_color="darkkhaki")
        btn1.place(x=450,y=400)
        customtkinter.CTkButton(master=root,command=register_data,bg_color="systembuttonface",text="تسجيل",text_font=15, text_color="black",width=scr_width/8, height=scr_height/18, compound="right",hover_color="dimgray",fg_color="darkkhaki").place(x=100,y=400)
      
      

# root=customtkinter.CTk()
# obj=Register(root)
# root.mainloop()
