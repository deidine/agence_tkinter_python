import os
import sys
from time import strftime
import tkinter
from tkinter import Toplevel, simpledialog
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter import messagebox
import customtkinter
from tkinter.messagebox import showinfo
from tabulate import tabulate
from turtle import width
sys.path.append('..')
from PIL import Image, ImageTk # pip install pillow


import tkinter as tk

import tkinter as tk
import pymysql.cursors

# Connect to the database
def connects():
   return pymysql.connect(host='localhost',user='root',password='',db='impriment',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

class Show:
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")
            customtkinter.set_default_color_theme("dark-blue")
            
            my_conn = connects()
            cur=my_conn.cursor()
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width,scr_height))
            my_w.title("l'inforamtion du message")  
            my_w.resizable(0,0)
            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
# ------------------------------------frame 

       # Using treeview widget 
            r_set=cur.execute("SELECT count(id) as no from feille")
            data_row=cur.fetchall()
            no_rec=data_row[0]['no']# Total number of rows in tabl
            limit = 30;
            def display(offset):
                global trv
                trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1", "2","3"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                trv.column("0", width = 100, anchor ='c')
                trv.column("1", width = 100, anchor ='c')
                trv.column("2", width = 200, anchor ='c')
                trv.column("3", width = 200, anchor ='c')
                trv.heading("0", text ="id")
                trv.heading("1", text ="prix")
                trv.heading("2", text ="nombre de page")
                trv.heading("3", text ="date")
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')
                q="SELECT * from feille order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['prix'],dt['nombre'],dt['date']))

                back = offset - limit
                next = offset + limit    
                


                if(no_rec <= next): 
                    b2=customtkinter.CTkButton(master=my_w,state=tkinter.DISABLED , text="suivant>>>",command=lambda: display(next), width=50, height=40, compound="right",fg_color="white", hover_color="#C77C78")

                else:
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="white",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=500)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="white",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
                else:
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",state=tkinter.DISABLED ,command=lambda: display(back), width=50, height=40, compound="right",fg_color="white", hover_color="yellow")
                b1.place(x=50,y=500)
                
#----------------------functions---------------
        
                    
            display(0)
    


# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()
