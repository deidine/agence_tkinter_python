import os
import sys
import tempfile
from time import strftime
import tkinter
from tkinter import YES, Toplevel, simpledialog
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk,scrolledtext as st
from tkinter import messagebox
import customtkinter
from tabulate import tabulate
from tkinter.messagebox import showinfo
from turtle import width
sys.path.append('..')#this is importent when you import some thing in other folder
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk
from database import connects
from agc_tamplate import template_long

class Show:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
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
            frame2=Frame(my_w)
            frame2.place(x=800,y=1000,width=700,height=500)

            title=customtkinter.CTkLabel(frame1,text_color="black",text="MODIFFIER CLIENT ICI غير معلومات المسافر هنا", text_font=("times new roman", 15, "bold"),bg_color="white" ).place(x=400,y=170)
            noml=customtkinter.CTkLabel(frame1,text="NOM الإسم",text_color="black", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=0,y=200)
            nom=customtkinter.CTkEntry(frame1,placeholder_text="NOM",text_font=("times new roman",15),bg_color="lightgray")
            nom.place(x=0,y=250,width=scr_width/8)
            telel=customtkinter.CTkLabel(frame1,text_color="black",text="Telephone ", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=200,y=200)
            tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            tele.place(x=200,y=250,width=scr_width/8)
            numL=customtkinter.CTkLabel(frame1,width=50,text_color="black",text="chaise ", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=400,y=200)
            num=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            num.place(x=400,y=250,width=90)
            directioinl=customtkinter.CTkLabel(frame1,text_color="black",text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=500,y=200)
            cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
            cmb_dir.place(x=500,y=250,width=scr_width/8)
            cmb_dir.current(0)            
            datel=customtkinter.CTkLabel(frame1,text_color="black",text="Date now", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=800,y=250)
            date=DateEntry(frame1,selectmode='day',font=("times new roman",13),bg="lightgray")
            date.place(x=800,y=180,width=scr_width/8)
            prixl=customtkinter.CTkLabel(frame1,width=50,text_color="black",text="payer دفع", text_font=("times new roman", 19, "bold"),bg_color="white").place(x=1000,y=200)
            prix=customtkinter.CTkEntry(frame1,text_font=("times new roman",1),bg_color="green")
            prix.place(x=900,y=2050,width=10)
            cmb_prix=ttk.Combobox(frame1,font=("times new roman",19), state="readonly", justify=CENTER)
            cmb_prix["values"]=("✅","❌")#✔✖
            cmb_prix.place(x=1000,y=250,width=100)
            cmb_prix.current(0)
            bus_nol=customtkinter.CTkLabel(frame1,text="numero bus رقم الباص", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=1100,y=200)

            cmb_bus_no=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            cmb_bus_no["values"]=("1"," 2"," 3"," 4","5"," 6","7","8","9","10")
            cmb_bus_no.place(x=1100,y=250,width=50) 
            cmb_bus_no.current(0)            
            impl=customtkinter.CTkLabel(frame1,width=50,text_color="black",text="imprimer طباعة", text_font=("times new roman", 19, "bold"),bg_color="white").place(x=7050,y=200)
            cmb_imp=ttk.Combobox(frame1,font=("times new roman",22), state="readonly", justify=CENTER)
            cmb_imp["values"]=("✔","✖")#
            cmb_imp.place(x=7500,y=250,width=100)
            cmb_imp.current(0)
            # prix.insert(END,'5000')#for inserting time at entry time 
            tele.delete(0,'end')
            num.delete(0,'end')
            # Change Selected Color
            style.map('Treeview',background=[('selected', "#347083")])           
            style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=500)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher phone ,nom...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=500,width=250)
            def serch():
                """
                 used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %
                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from client where nom like %s  or telephone like %s order by (id) desc"
                cur.execute(q,(serchE.get()+"%",serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['numero'],dt['telephone'],dt['direction'],dt['prix'],dt['date'],dt['payer'],dt['emploiyer'],dt['imprimer'],dt['bus_no'],dt['depart']))
                   
            sr=customtkinter.CTkButton(my_w,text_color="black" ,hover_color="darkslategrey",text="بحث", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=serch)
             
            sr.place(x=900,y=500)
        
        
            # Using treeview widget 
            my_str = tk.StringVar()
            r_set=cur.execute("SELECT count(id) as no from client")
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
                trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1","2","3","4","5","6","7","8","9","10","11"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                trv.bind("<ButtonRelease-1>",select)

                # width of columns and alignment 
                trv.column("0", width = 100, anchor ='c',stretch=YES)
                trv.column("1", width = 180, anchor ='c',stretch=YES)
                trv.column("2", width = 40, anchor ='c',stretch=YES)
                trv.column("3", width = 100, anchor ='c',stretch=YES)
                trv.column("4", width = 180, anchor ='c',stretch=YES)
                trv.column("5", width = 40, anchor ='c',stretch=YES)
                trv.column("6", width = 180, anchor ='c',stretch=YES)
                trv.column("7", width = 50, anchor ='c',stretch=YES)
                trv.column("8", width = 100, anchor ='c',stretch=YES)
                trv.column("9", width = 60, anchor ='c',stretch=YES)
                trv.column("10", width = 60, anchor ='c',stretch=YES)
                trv.column("11", width = 60, anchor ='c',stretch=YES)
                #nom,prenom,numero,telephone,direction,prix,date
                # Headings  
                # respective columns 
                trv.heading("0", text ="id")
                trv.heading("1", text ="nom")
                trv.heading("2", text ="chaise")
                trv.heading("3", text ="telephone")
                trv.heading("4", text ="direction")
                trv.heading("5", text ="prixs")
                trv.heading("6", text ="date")
                trv.heading("7", text ="payer")
                trv.heading("8", text ="emploiyer")
                trv.heading("9", text ="imprimer")
                trv.heading("10", text ="bus")
                trv.heading("11", text ="depart")
                
                # add a scrollbar
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')
                # # getting data from MySQL student table 
                # r_set=cur.execute("SELECT * from client ")
                # res=cur.fetchall()
                q="SELECT * from client order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['numero'],dt['telephone'],dt['direction'],dt['prix'],dt['date'],dt['payer'],dt['emploiyer'],dt['imprimer'],dt['bus_no'],dt['depart']))
                            # Show buttons 
                back = offset - limit # This value is used by Previous button
                next = offset + limit # This value is used by Next button       
                


                if(no_rec <= next): 
                    b2=customtkinter.CTkButton(master=my_w,state=tkinter.DISABLED , text="suivant>>>",command=lambda: display(next), width=50, height=40, compound="right",fg_color="white", hover_color="#C77C78")

                else:
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="black",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=500)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="black",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
                else:
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",state=tkinter.DISABLED ,command=lambda: display(back), width=50, height=40, compound="right",fg_color="white", hover_color="yellow")
                b1.place(x=50,y=500)

#----------------------functions---------------
            def retour():
                my_w.destroy()
            def reload1():
                my_w.destroy()
                os.system("py showCL.py")
            def delete():
                #for delete a row in tree view
                op=messagebox.askyesno("Confirm", "tu veut vraimment suprimer ?", parent=my_w)
                if op==True:
                    selected_item = trv.selection()[0]#the frist column id
                    trv.delete(selected_item)
                    try:
                        cur.execute("delete from client where id=%s",(selected_item))
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
                nom.insert(END,row[1])
                num.insert(END,row[2])
                tele.insert(END,row[3])
                prix.insert(END,row[5])
            def table():
                conn=connects()
                cur=conn.cursor()
                value="✖"
                op=simpledialog.askinteger("Input","أدخل عدد المسافرين للطباعة",parent=my_w)
                op2=simpledialog.askinteger("Input","أدخل رقم الباص",parent=my_w)
                q="SELECT numero,telephone,payer,nom,direction  from client where bus_no=%s and not imprimer=%s order by (id) desc limit %s"
                cur.execute(q,(op2,value,op))
                res=cur.fetchall()
                
                aa=":_____________________________________________:رقم الباص"
                aaa="type du vehicule:_____________________________________"+"\n"+"\n"+"nom et responsable du gare:_____________________"+"\n"+"\n"+"Nom du chauffeur:___________________________________"+"\n"+"\n"+"DESTINATION:________________________________"
		
                txt=template_long()
                a1="رقم المقعد"
                a2="إسم المسافر "
                a3="الهاتف"
                a4="دفع"
                txt+=aa+"\n"+"\n"+aaa+"\n"
                txt+="\n"+"_"*80+"\n"
                # txt+=tabulate(res,headers='keys',tablefmt="rounded_grid")
                txt+="{:<8}\t{:<8}\t{:<8}\t{:<8}\n__________________________________________________________________________\n".format('numero','telephone','payer','nom','direction')
                for dt in res:      
                    txt+="{:<8}\t{:<8}\t{:<8}\t{:<8}\n__________________________________________________________________________\n".format(dt['numero'],dt['telephone'],dt['payer'],dt['nom'],dt['direction'])

                txt+="\n"
                time=strftime('%m-%d-%Y')
                txt+="DATE D'IMPRIMATION:\t"+str(time)+"\t:تاريخ الطباعة "
                with open("print.txt","w",encoding="utf-8") as log:
                    log.write(txt)
                    os.startfile("print.txt","print")
                    log.close()
                
            def imp():
                table()
                clear()
                
            def update_data():
                """
                this function is for updating data mysql \n
                it test two option if the user click direction or forget it and that will not evect the changing of information 
                """
                #for updating data at the tree view and in our data base
                op=messagebox.askyesno("Confirm", "tu veut vraimment editer ?", parent=my_w)
                if op==True:
                    numVal=num.get()
                    teleVal=tele.get()
                    if nom.get()=="" or numVal=="" or teleVal=="" or num.get()=="":
                        messagebox.showerror("Error", "tous les champs sont obligatoire", parent=my_w)
                    else:
                        try:
                            id=trv.selection()[0]
                            if numVal.isdigit() and teleVal.isdigit() and cmb_dir.get()!="Selection":
                                #cette if et pour le cas ou l'user nest pas entrer le direction dans update system
                                n=num.get()
                                t=tele.get()
                                con=connects()
                                cur=con.cursor()
                                sql="update client set bus_no=%s,nom=%s,numero=%s,telephone=%s,direction=%s,payer=%s,date=%s where id=%s"
                                cur.execute(sql,(cmb_bus_no.get(),nom.get(),n,t,cmb_dir.get(),cmb_prix.get(),date.get_date(),id))
                                selected = trv.focus()
                                 
                            elif numVal.isdigit() and teleVal.isdigit():
                                n=num.get()
                                t=tele.get() 
                                sql="update client set bus_no=%s,nom=%s,imprimer=%s,numero=%s,telephone=%s,prix=%s,date=%s,payer=%s where id=%s"
                                con=connects()
                                cur=con.cursor()
                                cur.execute(sql,(cmb_bus_no.get(),nom.get(),cmb_imp.get(),n,t,prix.get(),date.get_date(),cmb_prix.get(),id))
                                selected = trv.focus()
                            trv.item(selected, text="", values=(id,nom.get(), n, t, cmb_dir.get(),prix.get(), date.get_date(),cmb_prix.get(),"emploiyer",cmb_imp.get(),cmb_bus_no.get(),"matin"))
                            selected = trv.focus()
                            con.commit()
                            clear()
                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
                else :
                    clear()

            def clear():
                nom.delete(0,END)
                tele.delete(0,END)
                prix.delete(0,END)
                num.delete(0,END)
                cmb_dir.current(0)
   
            btn=customtkinter.CTkButton(master=frame1,text_color="black",hover_color="darkslategrey",text="حذف", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=delete)
            btn.place(x=350,y=300)
            btn3=customtkinter.CTkButton(master=frame1,text_color="black",hover_color="darkslategrey",text="تغير", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=update_data)
             
            btn3.place(x=700,y=300)
     
            display(0)      
            

# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()
