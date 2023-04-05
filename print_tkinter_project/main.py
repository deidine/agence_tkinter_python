import sys,os,customtkinter
from time import gmtime, strftime
import customtkinter as cus
from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from tkinter import messagebox
from datetime import *
from math import *

sys.path.append("..")

class index:
    def __init__(self, root ): # default constructor and root is a tkinter class object
     
     
        self.root = root
        scr_width=self.root.winfo_screenwidth()
        scr_height=self.root.winfo_screenheight()
        self.root.title("System d'imprimation")
        self.root.geometry("%ix%i+0+0"% (scr_width,scr_height)) # Setting width
        self.root.config(bg="white")
        self.root.resizable(0, 0)
        def Exit():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=self.root)
            if sure == True:
                self.root.destroy()               
        self.root.protocol("WM_DELETE_WINDOW", Exit)
        #***********icons***********
        
        def reload():
            self.root.withdraw()
            os.system("py main.py")
        #***********Creating Menu***********
        scr_width=root.winfo_screenwidth()
        scr_height=root.winfo_screenheight()
        M_Frame=LabelFrame(self.root, text = "cliquer l'un des ses bouttons pou naviger vers d'autre fenetres  أضغط على زر من الأزرار لدخول الى نوافذ أخرى", font=("times new roman", 20), bg = "white")
        M_Frame.place(x=10, y=100, width = scr_width, height = scr_height/8)
        btn_mes=customtkinter.CTkButton(M_Frame,text_color="white",text="أخذ لقطة من الشاشة", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=screenshort)
        btn_mes.place(x=400, y=5, width=scr_width/8, height=scr_height/18)       
        btn_cln=customtkinter.CTkButton(M_Frame,text_color="white",text="طباعة صورة", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=image)
        btn_cln.place(x=200, y=5,width=scr_width/8, height=scr_height/18)  

        btn_chf=customtkinter.CTkButton(M_Frame,text_color="white",text="طباعة نص", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=text)
        btn_chf.place(x=10, y=5,width=scr_width/8, height=scr_height/18)  

        btn_reg=customtkinter.CTkButton(M_Frame,text_color="white",text=" طباعة ورد", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=word)
        btn_reg.place(x=600, y=5, width=scr_width/8, height=scr_height/18) 
        def Enreg():
            import Registration as reg
            root=cus.CTk()
            obj=reg.Reg_Login_windows(root)
            root.mainloop()
        def show():
            import show as sw
            root=cus.CTk()
            obj=sw.Show(root)
            root.mainloop()
        btn_reg=customtkinter.CTkButton(M_Frame,text_color="white",text="تسجيل", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=Enreg)
        btn_reg.place(x=900, y=5, width=scr_width/8, height=scr_height/18)  
        
        btn_reg=customtkinter.CTkButton(M_Frame,text_color="white",text="عرض", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=show)
        btn_reg.place(x=1100, y=5, width=scr_width/8, height=scr_height/18)  
        
        #***********Content Window***********
        self.bg_img=Image.open("bus2.jpg")
        self.bg_img=self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=100, y=200,width=scr_width, height=scr_height/2)  
        # prix=cus.CTkEntry(master=self.root,placeholder_text="nom d'utilisateur",text_font=("times new roman",15),bg_color="lightgray")
        # prix.place(x=700,y=150)
        
        #***********clock***********
        self.lbl=Label(self.root,text="Clock",font=("\nBook Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=200,height=450,width=310)
        time="\n"+strftime('%m-%d-%Y')+"\n"
        # time+=strftime('%H:%M')
        self.lbl.config(text=f"{str(time)}")
        self.working()

        #***********footer***********
        
        footer = Label(self.root,width=150,height=5, text="System de imprimation  devolloper par deidine 49619609", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.place(x=0, y=650)
       
       
#=============================================================================
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        #***********For clock Image***********
        bg=Image.open("c.png")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))

        #***********Hour Line Image***********
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #***********Min Line Image***********
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #***********Sec Line Image***********
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("clock_new.png")       
    def logout(self):
        op=messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            # root=Tk()
            # obj=Login_window(root)
            # root.mainloop()
    def exit_(self):
        op=messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op==True:
            self.root.destroy()
    def Emp_Inf(self):  
                    a=2


# verification  toplevl ------------------------------------------
def screenshort():
    # Import the required libraries
    import pyautogui
    from PIL import ImageTk, Image
    import time
    import win32api,win32print
    import tempfile
    # Create an instance of tknter frame or window
    win = Tk()

    # Set the size of the window
    win.geometry("50x50")


    # Define a function to take the screenshot
    def printImage(img):
        filename = tempfile.mktemp(".png")
        img.save(filename)
        win32api.ShellExecute(0,"print",filename,None,".",0)
    def take_screenshot():
        w= win.winfo_screenwidth()
        h= win.winfo_screenheight()
        x = 0
        y =0
        print(x,y,w,h)
        win.destroy()
        time.sleep(10)
        capImg = pyautogui.screenshot(region=(x, y, w, h))
        printImage(capImg)

    Button(win, text=' لقطة من الشاشة', command=take_screenshot).pack(padx=10, pady=10)

    win.mainloop()


#toplevel clien---------------------,-------
def text():
    from tkinter.filedialog import askopenfilename
    from tkinter.messagebox import showerror
    import os

    def print_any_file(file=None):
        if os.path.exists(file):
            try:
                os.startfile(file, "print")
            except Exception as e:
                showerror('Error',message='printing Error',detail=e)
        else:
            showerror('Printing Error',message='Please Select a file to print.')
            
    def selectfile():
        global file_to_print
        file= askopenfilename(filetypes =[('Text Files', '*.txt')])
        print_any_file(file)
    selectfile()


#toplevel message-----------------------
def image():
    from tkinter.filedialog import askopenfilename
    # from PIL import Image, ImageTk, ImageDraw # pip install pillow
    import time
    import win32api 
    from tkinter import messagebox, ttk
    import os
    import customtkinter as cus


    scr_width=root.winfo_screenwidth()
    scr_height=root.winfo_screenheight()

    def select_file():
        file=askopenfilename(initialdir="/",title="select image")
        if file:
            return win32api.ShellExecute(0,"print",file,None,".",0)

    select_file()
    # root.mainloop()
#chauffeur ------------------------

def word():
    from tkinter.filedialog import askopenfilename
    # from PIL import Image, ImageTk, ImageDraw # pip install pillow
    import time
    import win32api 
    from tkinter import messagebox, ttk
    import os
    import customtkinter as cus

    scr_width=root.winfo_screenwidth()
    scr_height=root.winfo_screenheight()

    def select_file():
        file=askopenfilename(initialdir="/",title="select image")
        if file:
            return win32api.ShellExecute(0,"print",file,None,".",0)
    select_file()            

    # root.mainloop()

# if __name__=="__main__":
root=Tk()
obj=index(root)
root.mainloop()