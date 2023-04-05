from tkinter import CENTER, Spinbox, Button, END, Frame, Tk, Toplevel
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import customtkinter
from tkinter import scrolledtext as st
import os
import os
import sys
sys.path.append("..")
from database import connects


class Register:

    def __init__(self, root):
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = root
        scr_width = self.root.winfo_screenwidth()/2+50
        scr_height = self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+200+100" % (scr_width, scr_height))
        self.root.title("Registration Window")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="beige",)

        scr_width = root.winfo_screenwidth()
        scr_height = root.winfo_screenheight()
        frame1 = Frame(self.root, bg="beige")
        frame1.place(x=10, y=10, width=scr_width/2-20, height=scr_height*0.65)
        frame2 = Frame(self.root)
        frame2.place(x=800, y=10, width=700, height=500)

        # ***********Row1***********
        numerol = customtkinter.CTkLabel(frame1, text="numero bus", text_font=(
            "times new roman", 15, "bold"), bg_color="white", fg_color="white").place(x=50, y=100)
        numero = customtkinter.CTkEntry(frame1, placeholder_text="numero....", text_font=(
            "times new roman", 15), fg_color="white", text_color="black")
        numero.place(x=50, y=130, width=scr_width/6)
        # ***********Row2***********
        nmbreL = customtkinter.CTkLabel(frame1, text="direction ", text_font=(
            "times new roman", 15, "bold"), bg_color="white", fg_color="white").place(x=50, y=200)

        direction=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        direction["values"]=("noikchott","atar","noidibou","nema")
        direction.place(x=50,y=270,width=scr_width/8) 
        direction.current(0)
# reloadfunction

        def reload():
            self.root.destroy()
            os.system("py enclient.py")

        def clear():
            numero.delete(0,END)
            direction.delete(0,END)

# ==================================================================

        def register_data():
      
            if numero.get() == "" or direction.get() == ""  :
                messagebox.showerror(
                    "Error", "tous les champs sont obligatoire", parent=root)
            else:
                try:
                   
                    con = connects()
                    cur = con.cursor()
                    cur.execute("insert into seats (bus_no,direction ) values(%s,%s)",
                                (numero.get(),direction.get()
                                 ))
                    con.commit()
                    con.close()
                    clear()
                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Error due to: {str(es)}", parent=root)

        btn1 = customtkinter.CTkButton(master=self.root, text="Annuller", text_font=(
            15),command=clear, width=scr_width/8, height=scr_height/18, text_color="black", compound="right", hover_color="dimgray", fg_color="darkkhaki")
        btn1.place(x=450, y=400)
        customtkinter.CTkButton(master=root, command=register_data, bg_color="systembuttonface", text="Enregistrer", text_font=15, text_color="black",
                                width=scr_width/8, height=scr_height/18, compound="right", hover_color="dimgray", fg_color="darkkhaki").place(x=100, y=400)


# root = customtkinter.CTk()
# obj = Register(root)
# root.mainloop()
