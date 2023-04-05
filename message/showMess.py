import os
import sys
from time import strftime
import tkinter
from tkinter import Toplevel, simpledialog
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter import messagebox
from img import imagePath,logo
import customtkinter
from tkinter.messagebox import showinfo
from tabulate import tabulate
from turtle import width
sys.path.append('..')
from PIL import Image, ImageTk # pip install pillow
from agc_tamplate import template_long
import tkinter as tk
from tkhtmlview import HTMLText, RenderHTML,HTMLLabel
import tkinter as tk
from database import connects


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
            my_w.title("l'inforamtion du message")  
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
            frame1.place(x=10,y=350,width=scr_width,height=scr_height)
            title=customtkinter.CTkLabel(frame1,text_color="black",text="MODIFFIER MESSAGE ICI غير معلومات الرسالة هنا", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=400,y=170)
            resvl=customtkinter.CTkLabel(frame1,text="le respteur المستلم",text_color="black", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=0,y=200)
            resv=customtkinter.CTkEntry(frame1,placeholder_text="...المستلم",text_font=("times new roman",15),bg_color="lightgray")
            resv.place(x=0,y=250,width=scr_width/8)
            typel=customtkinter.CTkLabel(frame1,text="type message نوعية الرسالة", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=180,y=200)
            # self.nomv=StringVar()
            type=customtkinter.CTkEntry(frame1,placeholder_text="type mess...",text_font=("times new roman",15),fg_color="white",text_color="black")
            type.place(x=200,y=250,width=scr_width/8)

            telel=customtkinter.CTkLabel(frame1,text_color="black",text="Telephone ", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=400,y=200)
            tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            tele.place(x=400,y=250,width=scr_width/8)
            prixl=customtkinter.CTkLabel(frame1,width=50,text_color="black",text="prix السعر", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=600,y=200)
            prix=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            prix.place(x=600,y=250,width=50)
            cmb_prixl=customtkinter.CTkLabel(frame1,width=50,text_color="black",text="payer دفع", text_font=("times new roman", 19, "bold"),bg_color="white").place(x=700,y=200)
            cmb_prix=ttk.Combobox(frame1,font=("times new roman",19), state="readonly", justify=CENTER)
            cmb_prix["values"]=("✅","❌")#✔✖
            cmb_prix.place(x=700,y=250,width=100)
            cmb_prix.current(0)
            bus_numl=customtkinter.CTkLabel(frame1,text="numero bus رقم الباص", text_font=("times new roman", 10, "bold"),bg_color="white").place(x=1200,y=200)
            cmb_bus_num=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            cmb_bus_num["values"]=("1"," 2"," 3"," 4","  5"," 6","7","8","9","10")
            cmb_bus_num.place(x=1200,y=250,width=50) 
            cmb_bus_num.current(0)          
            directioinl=customtkinter.CTkLabel(frame1,text_color="black",text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=850,y=200)
            cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            cmb_dir["values"]=("Selection","شنقيط "," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا","عين اهل الطائع","يغرف")
            cmb_dir.place(x=850,y=250,width=scr_width/8)
            cmb_dir.current(0)
            datel=customtkinter.CTkLabel(frame1,text_color="black",text="Date now", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=10100,y=250)
            date=DateEntry(frame1,selectmode='day',font=("times new roman",15),bg="lightgray")
            date.place(x=11000,y=200,width=scr_width/8)
            impl=customtkinter.CTkLabel(frame1,width=50,text_color="black",text="imprimer طباعة", text_font=("times new roman", 15, "bold"),bg_color="white").place(x=1050,y=200)
            cmb_imp=ttk.Combobox(frame1,font=("times new roman",20), state="readonly", justify=CENTER)
            cmb_imp["values"]=("✔","✖")#
            cmb_imp.place(x=1050,y=250,width=scr_width/10)
            cmb_imp.current(0)
            tele.delete(0,'end')
            prix.delete(0,'end')
        
        
            # Change Selected Color
            style.map('Treeview',background=[('selected', "#347083")])           
            style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")

        
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=500)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher phone ,nom...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=500,width=scr_width/8)
            def serch():
                """
                used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %

                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from message where respteur like %s  or telephone like %s order by (id) desc"
                cur.execute(q,(serchE.get()+"%",serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['respteur'],dt['typemessage'],dt['telephone'],dt['prix'],dt['direction'],dt['date'],dt['emploiyer'],dt['imprimer'],dt['bus_num'],dt['payer']))
                    selected = trv.focus()
                    
            sr=customtkinter.CTkButton(my_w,text_color="black" ,hover_color="darkslategrey",text="بحث", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=serch)
             
            sr.place(x=900,y=500)
                
        
        
            # Using treeview widget 
            r_set=cur.execute("SELECT count(id) as no from message")
            data_row=cur.fetchall()
            no_rec=data_row[0]['no']# Total number of rows in tabl
            limit = 30;
            # serchE.grid(row=9,column=0)
            
            def display(offset):
                """
                this function for display data by limit and next and previous method \n
                param offset for the numbre will show in data and shoul start by 0 and \n
                increment when click next or prev button
and shoul trv variable be global to acced into it for the others funtion
the buttonn will not appere because of some connditionell 
                """
                global trv
                
                trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1", "2", "3","4","5","6","7","8","9","10"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                # trv.place(x=50)
                trv.bind("<ButtonRelease-1>",select)

                    
                # width of columns and alignment 
                trv.column("0", width = 100, anchor ='c')
                trv.column("1", width = 100, anchor ='c')
                trv.column("2", width = 100, anchor ='c')
                trv.column("3", width = 100, anchor ='c')
                trv.column("4", width = 50, anchor ='c')
                trv.column("5", width = 280, anchor ='c')
                trv.column("6", width = 180, anchor ='c')
                trv.column("7", width = 100, anchor ='c')
                trv.column("8", width = 100, anchor ='c')
                trv.column("9", width = 100, anchor ='c')
                trv.column("10", width = 50, anchor ='c')
                # Headings  
                # respective columns
                trv.heading("0", text ="id")
                trv.heading("1", text ="respteur")
                trv.heading("2", text ="typemessage")
                trv.heading("3", text ="telephone")
                trv.heading("4", text ="prix")
                trv.heading("5", text ="direction")
                trv.heading("6", text ="date")
                trv.heading("7", text ="emploiyer")
                trv.heading("8", text ="imprimer")
                trv.heading("9", text ="bus")
                trv.heading("10", text ="payer")

                # add a scrollbar
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')
               
                # # getting data from MySQL student table 
                # r_set=cur.execute("SELECT * from message ")
                # res=cur.fetchall()
                q="SELECT * from message order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['respteur'],dt['typemessage'],dt['telephone'],dt['prix'],dt['direction'],dt['date'],dt['emploiyer'],dt['imprimer'],dt['bus_num'],dt['payer']))
                    
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
                os.system("py showMess.py")
            def delete():
                #for delete a row in tree view
                op=messagebox.askyesno("Confirm", "tu veut vraimment suprimer ?", parent=my_w)
                if op==True:
                    selected_item = trv.selection()[0]#the frist column id
                    trv.delete(selected_item)
                    try:
                        cur.execute("delete from message where id=%s",(selected_item))
                        my_conn.commit()
                        # messagebox.showinfo("Success", "le nom et suprimer", parent=my_w)
                        clear()

                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
            def table():
                conn=connects()
                cur=conn.cursor()
                op=simpledialog.askinteger("Input","أدخل عدد الرسائل للطباعة",parent=my_w)
                value="✖"
                q="SELECT * from message   where  not imprimer=%s  order by (id) desc limit %s"
                # q="SELECT respteur ,telephone ,prix ,typemessage as type_message,nombre,direction  from message  order by (id) desc limit %s"
                cur.execute(q,(value,op))
                res=cur.fetchall()
                html='''<html>
                    <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <style>   
                      fieldset{height:50%;}table{height: 50px;font-size:20px;border:1px solid ;border-collapse:collapse;}
                        th,td{border:1px solid;}
                        .p{margin-left:70%;margin-bottom:0px;margin-top:2px;}.i{margin-left:100px;}.ii{margin-left:300px;}
                        .iii{margin-left:400px;
                        font-family:sans-serif;
                        }i{font-size:20px;}.r{margin-left:50%;    }.a{font-size:20px;margin:auto;}
                        .tab{border:unset;}.imp{height:1%;font-size:15px;padding:10px;font-weight:142px;}
                        .label{
                            margin-right: auto;
                            margin-left: auto;
                            font-size: larger;
                            font-weight: bold;
                            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                        }
                        .imge{
                            
/* background-image: url("images/bus1.png");
background-repeat:no-repeat; */
     background-size:100% 100%;
     /* margin: auto; */
     padding:-10px -10px -10px -10px;width:20%;height: 10%;
}
.date{
    font-weight: bold;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-style: inherit;
} .tab{
    display: inline-block;
    margin-left: 300px;
}</style>
                        </head><body onload="window.print()">
                   '''+logo()+'''
                   <br>
                   
                    <h4>type du veicule <div class="tab"></div> نوع السيارة </h4>
              
                    <h4>numerodu voiture   <div class="tab"></div> رقم السيارة</h4> 
                    
                    <table border=1 cellspacing=10 width=90%>
                        <tr>
                        <th>order التنظيم</th>
                            <th>nom de passageur إسم المستلم</th>
                            <th>telephone الهاتف</th>
                            <th>le numero العدد</th>
<td>نوعية الرسالة</td>
                        <th>direction الإتجاه</th>
                        <th>payer دفع</th>
                        </tr>
                        <tr>
                    '''
                    
                
                file=open("index.html","w",encoding='utf-8')
                # txt7=tabulate(res,headers='keys',tablefmt="html")
                i=1
                for dt in res:
                    html+='''<tr><td>'''+str(i)+'''</td>'''  
                    html+='''<td>'''+dt['respteur']+'''</td>'''  
                    html+='''<td>'''+str(dt['telephone'])+'''</td>'''
                    html+='''<td>'''+str(dt['nombre'])+'''</td>'''  
                    html+='''<td>'''+dt['typemessage']+'''</td>'''  
                    html+='''<td>'''+dt['direction']+'''</td>'''  
                    html+='''<td>'''+dt['payer']+'''</td></tr>'''  
                    i+=1  
                time=strftime('%m-%d-%Y')
                dat="DATE D'IMPRIMATION:\t"+str(time)+"\t:تاريخ الطباعة "
                html+=''' </table><p></p> </div>   </fieldset>
                <div class="date"> '''+dat+'''</div>
                </body>

                    </html>'''
                file.write(html)
                file.close()
     
     
                
            def imp():
                table()
                import webbrowser
                os.startfile("index.html","print")
                # webbrowser.open("index.html")
                # from htmlpg import webPage
                # webPage("index.html")
                clear()   
            def select(event):
                
                """
                 this function used when you click the treeview and it will insert the data into input to be updated later\n
                param event is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work
                """
                clear()
                r=trv.focus()#the frist column id
                # r=trv.selection()[0]
                content=trv.item(r)
                row=content["values"]
                resv.insert(END,row[1])
                type.insert(END,row[2])
                tele.insert(END,row[3])
                prix.insert(END,row[4])
                # print(row[4])

            def update_data():
                #for updating data at the tree view and in our data base
                op=messagebox.askyesno("Confirm", "tu veut vraimment editer ?", parent=my_w)
                if op==True:
                    prixVal=prix.get()
                    teleVal=tele.get()
                    if type.get()=="" or prixVal=="" or teleVal=="" or resv.get()=="" or prix.get()=="":
                        messagebox.showerror("Error", "tous les champs sont obligatoire", parent=my_w)
                    else:
                        try:
                            id=trv.selection()[0]
                            if prixVal.isdigit() and teleVal.isdigit() and cmb_dir.get()=="Selection":
                                #cette if et pour le cas ou l'user nest pas entrer le direction dans update system
                                p=prix.get()
                                t=tele.get()
                                con=connects()
                                cur=con.cursor()
                                sql="update message set bus_num=%s, typemessage=%s,imprimer=%s,respteur=%s,prix=%s,telephone=%s,direction=%s,date=%s,payer=%s where id=%s"
                                cur.execute(sql,(cmb_bus_num.get(),type.get(),cmb_imp.get(),resv.get(),p,t,cmb_dir.get(),date.get_date(),cmb_prix.get(),id))
                                selected = trv.focus()
                                 
                            elif prixVal.isdigit() and teleVal.isdigit():
                                p=prix.get()
                                t=tele.get()
                                sql="update message set bus_num=%s,typemessage=%s,imprimer=%s,respteur=%s,prix=%s,telephone=%s,date=%s,payer=%s where id=%s"
                                con=connects()
                                cur=con.cursor()
                                cur.execute(sql,(cmb_bus_num.get(),type.get(),cmb_imp.get(),resv.get(),p,t,date.get_date(),cmb_prix.get(),id))
                                selected = trv.focus()
                            trv.item(selected, text="", values=(id,resv.get(), type.get(),t, p,  cmb_dir.get(), date.get_date(),"emploiyer",cmb_imp.get(),cmb_bus_num.get(),cmb_prix.get()))
                            selected = trv.focus()
                            con.commit()
                            # messagebox.showinfo("Success", "l'update est terminer", parent=my_w)
                            clear()
                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
                else :
                    clear()

            def clear():
                type.delete(0,END)
                resv.delete(0,END)
                tele.delete(0,END)
                # temp.delete(0,END)
                prix.delete(0,END)
                cmb_dir.current(0)
             
            btn4=customtkinter.CTkButton(master=frame1,text_color="black",hover_color="darkslategrey",text="طباعة", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=imp)
            btn4.place(x=550,y=300)
            btn=customtkinter.CTkButton(master=frame1,text_color="black",hover_color="darkslategrey",text="حذف", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=delete)
            btn.place(x=350,y=300)
            btn3=customtkinter.CTkButton(master=frame1,text_color="black",hover_color="darkslategrey",text="تغير", text_font=("times new roman",15),bg_color="white",fg_color="cornsilk",cursor="hand2", command=update_data)
             
            btn3.place(x=700,y=300)
                 
            display(0)
    


# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()
