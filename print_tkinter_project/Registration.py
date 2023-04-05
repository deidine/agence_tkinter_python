from time import strftime
from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from tkinter import messagebox, ttk
import customtkinter as cus
import pymysql.cursors

# Connect to the database
def connects():
   return pymysql.connect(host='localhost',user='root',password='',db='impriment',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

class Reg_Login_windows:
    def __init__(self,root):
        self.root = root
        self.root.title("Fenetre d'EnRegistrement")
        self.root.geometry("600x555+300+70")
        self.root.config(bg="#021e2f")
        self.root.resizable(width=False, height=False)

        #***********Background***********
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=300)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #***********Frames***********
        login_frame=cus.CTkFrame(self.root,bg_color="white")
        login_frame.place(x=100,y=30,width=370,height=500)

        
        #***********Title***********
        title=cus.CTkLabel(login_frame,text="D'ENREGISTRER NOUVELLE COMPT", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green",text_color="white").place(x=5,y=50)

        username=cus.CTkLabel(login_frame,text="كم عدد الاوراق",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=150)
        self.nombre=cus.CTkEntry(master=login_frame,placeholder_text="numero de feille",text_font=("times new roman",15),bg_color="lightgray")
        self.nombre.place(x=50,y=180,width=250)

        cus.CTkLabel(login_frame,text="سعر الورقة",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=230)
        self.prix=cus.CTkEntry(master=login_frame,placeholder_text="le prix",text_font=("times new roman",15),bg_color="lightgray")
        self.prix.place(x=50,y=260,width=250)
        self.prix.insert('end','50')
        btn_login=cus.CTkButton(login_frame,text="تسجيل",text_color="white", text_font=("times new roman",18,"bold"),fg_color="purple",bg_color="white", cursor="hand2",command=self.login).place(x=100,y=350,width=150)
       
        
#===================functions===========================================================

    def register_window(self):
        self.root.destroy()
        #import register

    def login(self):
        if self.nombre.get()=="" or self.prix.get()=="":
            messagebox.showerror("Error", "tous les champs sont obligatoire",parent=self.root)
        else:
            try:
                con=connects()
                cur=con.cursor()
                time=strftime('%m-%d-%Y')
                pr=int(self.nombre.get())*int(self.prix.get())
                cur.execute("insert into feille (nombre,prix,date) values(%s,%s,%s) ",(self.nombre.get(),pr,str(time)))
                con.commit()
                messagebox.showinfo('succss',"l'inregistrement  et terminer")
                # self.prix.delete(0,END)
                self.nombre.delete(0,END)
                self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)

# root=cus.CTk()
# obj=Reg_Login_windows(root)
# root.mainloop()