import sys,os,customtkinter
from tkinter import simpledialog
from time import gmtime, strftime
import customtkinter as cus
from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from tkinter import messagebox
from datetime import *
from math import *
from client.bus_cl import Show_Bus
from message.bus_mess import Show_Bus_Mess
import webbrowser

sys.path.append("..")
from database import connects
from img import imagePath
class index:
    def __init__(self, root ): # default constructor and root is a tkinter class object
        con=connects()
        cur=con.cursor()
        self.root = root
        scr_width=self.root.winfo_screenwidth()
        scr_height=self.root.winfo_screenheight()
        self.root.title("System de voyage et transport")
        self.root.geometry("%ix%i+0+0"% (scr_width,scr_height)) # Setting width
        self.root.resizable(0, 0)
        # self.root.config(bg="darksalmon",)
       
        def Exit():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=self.root)
            if sure == True:
                self.root.destroy()               
        self.root.protocol("WM_DELETE_WINDOW", Exit)

      #***********Content Window***********
        self.bg_img=Image.open(imagePath()+"bus.png")
        # self.bg_img=Image.open("../images/bus.png")
        self.bg_img=self.bg_img.resize((1420, 650), Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=0, y=0,relwidth=1,relheight=1)  
        #***********Creating Menu***********
        scr_width=root.winfo_screenwidth()
        scr_height=root.winfo_screenheight()
        def reload():
            self.root.withdraw()
            os.system("py main.py")
        
        M_Frame=Label(self.root, font=("times new roman", 20), bg = "cornsilk")
        M_Frame.place(x=0, y=0, width = scr_width, height = scr_height/8)
        btn_mes=customtkinter.CTkButton( self.lbl_bg,text_color="black",hover_color="darkslategrey",text="الرسائل", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=message)
        btn_mes.place(x=400, y=5, width=scr_width/8, height=scr_height/18)   

        # btn_chf=customtkinter.CTkButton(M_Frame,text_color="white",text="reload", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=reload)
        # btn_chf.place(x=10, y=5,width=scr_width/8, height=scr_height/18)  
        
        btn_cln=customtkinter.CTkButton( self.lbl_bg,text_color="black",hover_color="darkslategrey",text="المسافرين", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=client)
        btn_cln.place(x=850, y=5,width=scr_width/8, height=scr_height/18)  
        btn_reg=customtkinter.CTkButton( self.lbl_bg,text_color="black",hover_color="darkslategrey",text="الباص", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=buss)
        
        btn_reg.place(x=600, y=5,width=scr_width/8, height=scr_height/18)  
          
  
    #---------------------------------------------------
        def clientBusMat():
            op=simpledialog.askstring("Input","entrer le numero du buss",parent=self.root)
            if (op):
                my_w =customtkinter.CTk()
                Show_Bus(my_w,op,"matin" )
                my_w.mainloop()
                
        def clientBussr():
            
            op=simpledialog.askstring("Input","entrer le numero du buss",parent=self.root)
            if (op):

                my_w =customtkinter.CTk()
                Show_Bus(my_w,op,"soir" )
                my_w.mainloop()
        
        def MessBus():
                op=simpledialog.askstring("Input","entrer le numero du buss",parent=self.root)
                
                # self.root.destroy()
                if(op):
                        
                    my_w =customtkinter.CTk()
                    Show_Bus_Mess(my_w,op )
                    my_w.mainloop()
        btn3=cus.CTkButton(self.root,hover_color="darkslategrey",command=clientBusMat,text="حالة باص المسافرين\n في الصباح",text_color="black", text_font=("times new roman",15,"bold"),fg_color="bisque",bg_color="white", cursor="hand2")
        btn3.place(x=360,y=630,width=200)
        btn3=cus.CTkButton(self.root,hover_color="darkslategrey",command=clientBussr,text="حالة باص المسافرين\n في المساء",text_color="black", text_font=("times new roman",15,"bold"),fg_color="bisque",bg_color="white", cursor="hand2")
        btn3.place(x=600,y=630,width=200)
        btn3=cus.CTkButton(self.root,hover_color="darkslategrey",command=MessBus,text="حالة باص \nالرسائل",text_color="black", text_font=("times new roman",15,"bold"),fg_color="bisque",bg_color="white", cursor="hand2")
        btn3.place(x=850,y=630,width=200)
        #***********clock***********
        
#=============================================================================
    
    def logout(self):
        op=messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()

    def exit_(self):
        op=messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op==True:
            self.root.destroy()
    def Emp_Inf(self):  
        from home.emp import Emp
        my_w =customtkinter.CTk()
        my_w1=Emp(my_w)
        my_w.mainloop()

#toplevel clien---------------------,-------
def client():
    from client import Register,Show
    topcl=Toplevel()
    topcl.geometry("300x300+500+70")
    topcl.resizable(0, 0)
    topcl.config(bg="beige",)

    #***********Background***********
    lbl=Label(topcl,bg="beige",bd=0)
    lbl.place(x=0,y=0,relheight=1,width=300)
    #***********Title***********
    title=cus.CTkLabel(lbl,text=" المسافرين", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="beige",text_color="black").place(x=87,y=60)
    def enclient():
        topcl.withdraw() 
        root=customtkinter.CTk()
        obj=Register(root)
        root.mainloop()
    def showcl():
        topcl.withdraw() 
        my_w =customtkinter.CTk()
        my_w1=Show(my_w)
        my_w.mainloop()
    def payer():
        import webview
       

        webview.create_window('valide payement', 'http://localhost/payer/index.html')
        webview.start()
            
    btn1=cus.CTkButton(lbl,command=showcl,text="عرض\nالمسافرين",text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn1.place(x=20,y=150,width=120)
    btn2=cus.CTkButton(lbl,text="تسجيل \n مسافر",command=enclient,text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn2.place(x=150,y=150,width=100)
    btn3=cus.CTkButton(lbl,text="عرض  \n الدفع",command=payer,text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn3.place(x=70,y=230,width=100)
#toplevel message-----------------------
def message():
    from message import Register,Show
    topmess=Toplevel()
    topmess.geometry("300x300+500+70")
    topmess.resizable(0, 0)
    topmess.config(bg="beige",)

    #***********Background***********
    lbl=Label(topmess,bg="beige",bd=0)
    lbl.place(x=0,y=0,relheight=1,width=300)
    #***********Title***********
    title=cus.CTkLabel(lbl,text="الرسائل", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="beige",text_color="black").place(x=87,y=60)
    
    def enMessage():
        topmess.withdraw() 
        root=customtkinter.CTk()
        obj=Register(root)
        root.mainloop()
    def showMs():
        topmess.withdraw() 
        my_w =customtkinter.CTk()
        my_w1=Show(my_w)
        my_w.mainloop()
    btn1=cus.CTkButton(lbl,command=showMs,text="عرض \n الرسائل",text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn1.place(x=20,y=150,width=120)
    btn2=cus.CTkButton(lbl,text="تسجيل\nرسالة",command=enMessage,text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn2.place(x=150,y=150,width=100)
#bus ------------------------

def buss():
    def vider(): 
            op=messagebox.askyesno("imprimer","tu veux vider les chaises du buss",parent=topcl)
            if op==True:            
                try:
                    con=connects()
                    cur=con.cursor()
                    sql="UPDATE seats set `seat_booked`='1'"
                    cur.execute(sql)
                    con.commit()
            
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=topcl)
        

    from .enbuss import Register
    from .showBus import Show
    topcl=Toplevel()
    topcl.geometry("300x300+500+70")
    topcl.resizable(0, 0)
    topcl.config(bg="beige",)

    #***********Background***********
    lbl=Label(topcl,bg="beige",bd=0)
    lbl.place(x=0,y=0,relheight=1,width=300)
    #***********Title***********
    title=cus.CTkLabel(lbl,text="Buss", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="beige",text_color="black").place(x=87,y=60)
    def enBuss():
        topcl.withdraw() 
        root=customtkinter.CTk()
        obj=Register(root)
        root.mainloop()
    def showBuss():
        topcl.withdraw() 
        my_w =customtkinter.CTk()
        my_w1=Show(my_w)
        my_w.mainloop()
    
    btn1=cus.CTkButton(lbl,command=showBuss,text="عرض\n الباص",text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn1.place(x=20,y=100,width=120)
    btn2=cus.CTkButton(lbl,text="تسجيل\n الباص",command=enBuss,text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn2.place(x=150,y=100,width=120) 

    btn2=cus.CTkButton(lbl,text="تفريغ \nالمقاعد",command=vider,text_color="black", text_font=("times new roman",15,"bold"),hover_color="dimgray",fg_color="darkkhaki",bg_color="white", cursor="hand2")
    btn2.place(x=50,y=200,width=170) 
  

# # # # if __name__=="__main__":
# root=Tk()
# obj=index(root)
# root.mainloop()