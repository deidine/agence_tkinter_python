from doctest import master
import tkinter as tk
from tkhtmlview import HTMLText, RenderHTML

import tempfile
from tkinter.scrolledtext import ScrolledText
import customtkinter
import os,sys
sys.path.append("..")
from time import strftime
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
    this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()/2+50
        scr_height=self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+200+100"% (scr_width,scr_height))
        self.root.geometry("720x520+300+90") # Setting width
        self.root.config(bg="white")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="beige",)

        frame1=Frame(self.root,bg="beige")
        frame1.place(x=10,y=10,width=700,height=500)
        frame2=Frame(self.root)
        frame2.place(x=800,y=10,width=700,height=500)

        #***********Row1***********

        # self.var_fname=StringVar()

        envl=customtkinter.CTkLabel(frame1,text="l'envoiyeur المرسل",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=100)
        # self.prenomv=StringVar()
        env=customtkinter.CTkEntry(frame1,placeholder_text="nom et Prenom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        env.place(x=50,y=130,width=scr_width/4) 

        typel=customtkinter.CTkLabel(frame1,text="type message نوعية الرسالة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=100)
        # self.nomv=StringVar()
        type=customtkinter.CTkEntry(frame1,placeholder_text="type mess...",text_font=("times new roman",15),fg_color="white",text_color="black")
        type.place(x=370,y=130,width=scr_width/4) 

        #***********Row2***********
        
        telel=customtkinter.CTkLabel(frame1,text="Numero Telephone الهاتف", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=170)
        # self.telev=IntVar()
        # self.tele=Entry(frame1,textvariable=self.telev,font=("times new roman",15),bg="lightblue")
        tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15))
        tele.place(x=50,y=200,width=scr_width/4) 

        prixl=customtkinter.CTkLabel(frame1,text="السعر", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=170)
        prix=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        prix.place(x=370,y=200,width=70)
        prix.insert(END,"5000")
        cmb_prix=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_prix["values"]=("✅","❌")
        cmb_prix.place(x=450,y=200,width=50)
        cmb_prix.current(0)
        nmbl=customtkinter.CTkLabel(frame1,text="العدد", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=500,y=170)
        nmb=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        nmb.place(x=520,y=200,width=70)

        
#reload------------------function
        # def validator(num):
        #     return num.isdigit() or num == ""
       

        text_ear=ScrolledText(frame2,width=40,height=20)
        text_ear.place(x=50,y=50)

            
        def reload():
            self.root.destroy()
            os.system("py enclient.py")
        # Button(self.root,text="reload",command=reload).place(x=660,y=5)
        #***********Row3***********

        directioinl=customtkinter.CTkLabel(frame1,text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=240)
        # dirv=StringVar()
        cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_dir["values"]=("Selection","noikchott","atar","noidibou","nema")
        cmb_dir.place(x=50,y=270,width=scr_width/4) 
        cmb_dir.current(0)
        bus_numl=customtkinter.CTkLabel(frame1,text="numero bus رقم الباص", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=280,y=320)

        cmb_bus_num=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        # cmb_bus_num["values"]=("1"," 2"," 3"," 4","  5"," 6","7","8","9","10")
        cmb_bus_num.place(x=300,y=360,width=150) 
        # cmb_bus_num.current(0)

        datel=customtkinter.CTkLabel(frame1,text="Date now تاريخ اليوم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=240)
        # datev=IntVar()
        #self.date=Calendar(self.root,selectmode='day',year=2020,month=5,day=22,width=50)
        date=DateEntry(frame1,selectmode='day',font=("times new roman",15),fg="black",bg="white")
        date.place(x=370,y=270,width=scr_width/4) 

        def retour():
            self.root.destroy()
    
        def clear():
            env.delete(0,END)
            type.delete(0,END)
            tele.delete(0,END)
            # self.temp.delete(0,END)
            prix.delete(0,END)
            nmb.delete(0,END)
            cmb_dir.current(0)
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
<script> alert("من فضلك لاتنسى غلق النافذة بعد الطباعة sur te plait nous oblier pas de fermer le venetre apre l'imprimation");</script>

            <div class="box"><!-- ticket 1 -->
            <div class="ticket yellow">   '''+logotiket()+'''
            <div class="serial">رقم الباص'''+cmb_bus_num.get()+'''</div><div class="rate">الوجهة'''+cmb_dir.get()+'''  '''+prix.get()+'''
            </div><div class="grid_wrapper"><div class="grid">
            <div class="name">لا نتحمل المسؤلية بعد 15 يوم <br> aucun responsabiliter apres 15 jours</div>
            <div class="number"> المرسل</div>
            <div class="number">'''+env.get()+'''</div><br>
            <div class="number">الهاتف</div>
            <div class="number">'''+tele.get()+'''</div><br>
            <div class="number">العدد </div>
            <div class="number">'''+nmb.get()+'''</div><br>
            <div class="number">النوعية</div>
            <div class="number">'''+type.get()+'''</div><br>
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
            from tkhtmlview import HTMLLabel
            
            
            

        btn1=Button(frame2,text='print',command=lambda: print_text(text_ear.get('1.0',END)))
        btn1.place(x=400,y=300)
        btn1=Button(frame2,text='reload',command=reload)
        btn1.place(x=450,y=300)
        btn=Button(frame2,text='write',command=write)
        btn.place(x=200,y=300)
        tele.delete(0,END)
        #self.temp.delete(0,END)
        # prix.delete(0,END)
        cmb_dir.current(0)

#===================================================================

        def register_data():
            """
                    test if the user enter  only the number 
                    in telephone and prix
            """
            # print(self.var_fname.get(), self.prenom.get())
            prixVal=prix.get()
            teleVal=tele.get()
            nmbval=nmb.get()

            if env.get()=="" or prixVal=="" or teleVal=="" or type.get()=="" or  cmb_dir.get()=="Selection"  or prix.get()=="":
                messagebox.showerror("Error", "tous les champs sont obligatoire", parent=root)
                # messagebox.showerror("Error", numVal, parent=self.root)
            else:
                try:
                    
                        if prixVal.isdigit() and teleVal.isdigit() and nmbval.isdigit():
                            n=prix.get()
                            m=nmb.get()
                            t=tele.get()
                            con=connects()
                            cur=con.cursor()
                        else: 
                            messagebox.showerror("Error", "numero du chaise ou numero de telephone doit etre des nombre", parent=self.root)
                        with open("login.txt") as file:
                             f=file.read()
                        cur.execute("INSERT INTO message(imprimer,nombre,typemessage,respteur,prix, telephone ,direction, date,emploiyer,bus_num,payer ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                           "✔", m,type.get(),
                            env.get(),
                            n,
                            t,
                            cmb_dir.get(),
                            date.get_date(),f,cmb_bus_num.get(),
                             cmb_prix.get()
                        ))
                        con.commit()
                        con.close()
                        write()
                        
                        print_text()
                        import webbrowser
                        op=messagebox.askyesno("imprimer","tu veux imprimer",parent=root)
                        if op==True:
                            # from htmlpg import webPage
                            # webPage("tiket.html")
                            os.startfile("index.html","print")
                            # webbrowser.open("tiket.html")
                            clear()
                        else :
                            clear()
                        clear()
                        # self.login_window()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)


        btn1=customtkinter.CTkButton(master=self.root,text="RETOUR",text_font=(15),    command=retour,width=scr_width/8, height=scr_height/18,text_color="black", compound="right",hover_color="dimgray",fg_color="darkkhaki")
        btn1.place(x=450,y=400)
        customtkinter.CTkButton(master=root,command=register_data,bg_color="systembuttonface",text="تسجيل",text_font=15, text_color="black",width=scr_width/8, height=scr_height/18, compound="right",hover_color="dimgray",fg_color="darkkhaki").place(x=100,y=400)




# root=customtkinter.CTk()
# obj=Register(root)
# root.mainloop()

