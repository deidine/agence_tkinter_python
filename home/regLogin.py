from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from database import connects
from tkinter import messagebox, ttk
import customtkinter as cus
class Reg_Login_window:
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

        username=cus.CTkLabel(login_frame,text="Entrer nom utilisateur",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=150)
        self.txt_username=cus.CTkEntry(master=login_frame,placeholder_text="nom d'utilisateur",text_font=("times new roman",15),bg_color="lightgray")
        self.txt_username.place(x=50,y=180,width=250)

        cus.CTkLabel(login_frame,text="Entrer password",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=230)
        self.txt_password=cus.CTkEntry(master=login_frame,placeholder_text="mot de pass",text_font=("times new roman",15),bg_color="lightgray")
        self.txt_password.place(x=50,y=260,width=250)
        btn_login=cus.CTkButton(login_frame,text="EnRegistrer",text_color="white", text_font=("times new roman",18,"bold"),fg_color="purple",bg_color="white", cursor="hand2",command=self.login).place(x=100,y=350,width=150)
       
        
#===================functions===========================================================

    def register_window(self):
        self.root.destroy()
        #import register

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
                    cur.execute("insert into login (username,password) values(%s,%s) ",(self.txt_username.get(),self.txt_password.get(),))
                    con.commit()
                    messagebox.showinfo('succss',"l'inregistrement du nouveau compte et terminer")
                    self.txt_password.delete(0,END)
                    self.txt_username.delete(0,END)
                    self.root.destroy()
                else:
                    messagebox.showerror("error", "error le mod de pass et degas exist", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)

# root=cus.CTk()
# obj=Reg_Login_window(root)
# root.mainloop()