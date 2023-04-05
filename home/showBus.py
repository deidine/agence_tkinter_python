import os
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


class Show:

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
            
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=10,y=350,width=1400,height=500)
            title=customtkinter.CTkLabel(frame1,text_color="white",text="MODIFFIER CHAUFFEUR ICI غير معلومات السائق هنا", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=4000,y=170)
            numerol=customtkinter.CTkLabel(frame1,text="NOM الإسم",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=0,y=2000)
            numero=customtkinter.CTkEntry(frame1,placeholder_text="NOM",text_font=("times new roman",15),bg_color="lightgray")
            numero.place(x=0,y=2500,width=250)
            nombrechaise=customtkinter.CTkLabel(frame1,text_color="white",text="PRESNOM الإسم العائلي",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=3000,y=200)
            nbre_chse=customtkinter.CTkEntry(frame1,placeholder_text="PRENOM",text_font=("times new roman",15),bg_color="lightgray")
            nbre_chse.place(x=3000,y=250,width=250)
            directioinl=customtkinter.CTkLabel(frame1,text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=240)
            cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            cmb_dir["values"]=("Selection","noikchott","atar","noidibou","nema")
            cmb_dir.place(x=280,y=240,width=scr_width/8) 
            cmb_dir.current(0)
            
            numero.delete(0,'end')
            nbre_chse.delete(0,'end')
            # Change Selected Color
            style.map('Treeview',background=[('selected', "#347083")])           
            style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=700)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=700,width=250)
            def serch():
                """
                 used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %
                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from seats where bus_no like %s "
                cur.execute(q,(serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['bus_no'],dt['direction'],dt['seat_booked']))
                    
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=700)
                
        
        
            # Using treeview widget 
            my_str = tk.StringVar()
            r_set=cur.execute("SELECT count(id) as no from seats")
            data_row=cur.fetchall()
            no_rec=data_row[0]['no']# Total number of rows in tabl
            limit = 30;
            # serchE.grid(row=9,column=0)

            def display(offset):
                """ this function for display data by limit and next and previous method \n
                param offset for the numbre will show in data and shoul start by 0 and \n
                increment when click next or prev button

                """
                global trv
                trv = ttk.Treeview(my_w,height=25,selectmode ='browse',columns=("0","1", "2", "3"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                trv.bind("<ButtonRelease-1>",select)

                # width of columns and alignment 
                trv.column("0", width = 300, anchor ='c')
                trv.column("1", width = 300, anchor ='c')
                trv.column("2", width = 300, anchor ='c')
                trv.column("3", width = 200, anchor ='c')
               
                #nom,prenom,numero,telephone,direction,prix,date
                # Headings  
                # respective columns
                trv.heading("0", text ="id")
                trv.heading("1", text ="numero buss")
                trv.heading("2", text ="direction")
                trv.heading("3", text ="chaise reserver")
                
                # add a scrollbar
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')

                q="SELECT * from seats order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['bus_no'],dt['direction'],dt['seat_booked']))
                            # Show buttons 
                back = offset - limit # This value is used by Previous button
                next = offset + limit # This value is used by Next button       
                


                if(no_rec <= next): 
                    b2=customtkinter.CTkButton(master=my_w,state=tkinter.DISABLED , text="suivant>>>",command=lambda: display(next), width=50, height=40, compound="right",fg_color="white", hover_color="#C77C78")

                else:
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="white",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=700)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="white",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
                else:
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",state=tkinter.DISABLED ,command=lambda: display(back), width=50, height=40, compound="right",fg_color="white", hover_color="yellow")
                b1.place(x=50,y=700)

#----------------------functions---------------
            def retour():
                my_w.destroy()
            def reload1():
                my_w.destroy()
                os.system("py showBus.py")
            def delete():
                #for delete a row in tree view
                op=messagebox.askyesno("Confirm", "tu veut vraimment suprimer ?", parent=my_w)
                if op==True:
                    selected_item = trv.selection()[0]#the frist column id
                    trv.delete(selected_item)
                    try:
                        cur.execute("delete from seats where id=%s",(selected_item))
                        my_conn.commit()
                        messagebox.showinfo("Success", "le nom et suprimer", parent=my_w)
                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
            
            def select(ev):
                """
                this function used when you click the treeview and it will insert the data into input to be updated later\n
                param ev is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work

                """
                clear()
                r=trv.focus()
                content=trv.item(r)
                row=content["values"]
                numero.insert(END,row[1])
                nbre_chse.insert(END,row[2])
                
            def update_data():
                """
                this function is for updating data mysql \n
                it test two option if the user click direction or forget it and that will not evect the changing of information 
                """
                #for updating data at the tree view and in our data base
                op=messagebox.askyesno("Confirm", "tu veut vraimment editer ?", parent=my_w)
                con=connects()
                if op==True:
                        
                        try:
                            id=trv.selection()[0]
                            if cmb_dir.get()!="Selection":
                             
                                cur=con.cursor()
                                sql="update seats set direction=%s where id=%s"
                                cur.execute(sql,(cmb_dir.get(),id))
                                selected = trv.focus()
                                trv.item(selected, text="", values=(id,numero.get(), cmb_dir.get(),'1'))
                                 
                            con.commit()
                            clear()
                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
                else :
                    clear()


            def clear():
                numero.delete(0,END)
                nbre_chse.delete(0,END)
                
            btn=customtkinter.CTkButton(master=frame1, text="suprimer",command=delete, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            btn.place(x=550,y=240)

            btn2=customtkinter.CTkButton(master=frame1, text="reload",command=reload1, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            btn2.place(x=1270,y=280)
            btn2=customtkinter.CTkButton(master=frame1, text="update",command=update_data, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            btn2.place(x=470,y=240)
         
            display(0)
            # serch()


# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()
