import sys
from tkinter.filedialog import askopenfilename
import win32api
from home import index 
from tkinter import*
# from PIL import Image, ImageTk, ImageDraw # pip install pillow
from datetime import*
import time
from math import*
from database import connects
from tkinter import messagebox, ttk
import os
import customtkinter as cus

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")#)#هذا للموضوع الشاشة
        self.root.geometry("600x555+300+70")#)هذا لحجم الشاشة 
        self.root.config(bg="lavender")
        
        scr_width=self.root.winfo_screenwidth()
        scr_height=self.root.winfo_screenheight()
        self.root.resizable(width=False, height=False)#)هذا لان تكون الشاشة غير قابلة التغير

        #***********Background***********
        # left_lbl=cus.CTkLabel(self.root,bg_color="#08A3D2")
        # left_lbl.place(x=0,y=0,relheight=1,width=300)

        # right_lbl=cus.CTkLabel(self.root,bg_color="#031F3C")
        # right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #***********Frames***********
        scr_width=root.winfo_screenwidth()
        scr_height=root.winfo_screenheight()

        login_frame=cus.CTkFrame(self.root,fg_color="cornsilk")
        login_frame.place(x=100,y=30,width=scr_width/4,height=scr_height*2)

        #***********Title***********
        title=cus.CTkLabel(login_frame,text="LOGIN", text_font=("times new roman", 20, "bold"),bg_color="cornsilk",fg_color="cornsilk",text_color="black").place(x=100,y=50)
        username=cus.CTkLabel(login_frame,text="Entrer nom utilisateur",text_color="black", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="cornsilk").place(x=50,y=150)
        self.txt_username=cus.CTkEntry(master=login_frame,placeholder_text="nom d'utilisateur",text_font=("times new roman",15),bg_color="lightgray")
        
        self.txt_username.place(x=50,y=180,width=scr_width/6)

        cus.CTkLabel(login_frame,text="Entrer password",text_color="black", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="cornsilk").place(x=50,y=230)
        self.txt_password=cus.CTkEntry(master=login_frame,placeholder_text="mot de pass",show="*",text_font=("times new roman",15),bg_color="lightgray")
        self.txt_password.place(x=50,y=260,width=scr_width/6)
        btn_login=cus.CTkButton(login_frame,text="Entrer",hover_color="white",text_color="black", text_font=("times new roman",18,"bold"),fg_color="lavender",bg_color="white", cursor="hand2",command=self.login).place(x=100,y=350,width=scr_width/9)
        # btn_login=cus.CTkButton(login_frame,text="rest",text_color="white", text_font=("times new roman",18,"bold"),fg_color="purple",bg_color="white", cursor="hand2",command=self.reset).place(x=250,y=350,width=scr_width/9)
       
        def reload():
            self.root.destroy()
            os.system("py login.py")
        # Button(login_frame,text="reload",command=reload).place(x=250,y=400)


#====================functions==========================================================
    def reset(self):
        self.txt_password.delete(0,END)#هذا يكون لحذف مكان الادخال
        self.txt_username.delete(0,END)
    def session(self):
        return self.txt_username.get()

 
    def login(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "tous les champs sont obligatoire",parent=self.root)
        else:
            try:
                con=connects()
                cur=con.cursor()
                cur.execute("select * from login where username=%s and password=%s",(self.txt_username.get(),self.txt_password.get(),))
                row=cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root) 
                    # reset(self)
                else:
                    with open("login.txt","w") as log:
                        log.write(self.txt_username.get())
                        log.close()                     
                    self.root.destroy()
                    # os.system("python index.py")
                    root2=Tk()
                    obj=index(root2)
                    root2.iconbitmap("index.ico")

                    root2.mainloop()
                   
                con.close()    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)
root=Tk()
obj=Login_window(root)
root.iconbitmap("index.ico")
root.mainloop()