from tkinter import Checkbutton, StringVar, scrolledtext as st
import tempfile,os
import os,sys
sys.path.append("..") #this is importent when you import some thing in other folder
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
from database import connects
from img import imagePath,logo
from agc_tamplate import template,footer
import customtkinter
from time import strftime
import tkinter
from tkinter import Toplevel, simpledialog
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter.messagebox import showinfo
from tabulate import tabulate
from turtle import width
from agc_tamplate import template_long
import tkinter as tk
from tkhtmlview import HTMLText, RenderHTML,HTMLLabel
import tkinter as tk
from database import connects


class Show_Bus:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w,bus_numero) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
            self.bus_numero=bus_numero
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
        #     title=customtkinter.CTkLabel(frame1,text_color="white",text="MODIFFIER MESSAGE ICI غير معلومات الرسالة هنا", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=400,y=170)
        #     resvl=customtkinter.CTkLabel(frame1,text="le respteur المستلم",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=0,y=200)
        #     resv=customtkinter.CTkEntry(frame1,placeholder_text="...المستلم",text_font=("times new roman",15),bg_color="lightgray")
        #     resv.place(x=0,y=250,width=scr_width/8)
        #     typel=customtkinter.CTkLabel(frame1,text="type message نوعية الرسالة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=180,y=200)
        #     # self.nomv=StringVar()
        #     type=customtkinter.CTkEntry(frame1,placeholder_text="type mess...",text_font=("times new roman",15),fg_color="white",text_color="black")
        #     type.place(x=200,y=250,width=scr_width/8)

        #     telel=customtkinter.CTkLabel(frame1,text_color="white",text="Telephone ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=400,y=200)
        #     tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
        #     tele.place(x=400,y=250,width=scr_width/8)
        #     prixl=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="prix السعر", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=600,y=200)
        #     prix=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
        #     prix.place(x=600,y=250,width=50)
        #     cmb_prixl=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="payer دفع", text_font=("times new roman", 19, "bold"),bg_color="white",fg_color="gray").place(x=700,y=200)
        #     cmb_prix=ttk.Combobox(frame1,font=("times new roman",19), state="readonly", justify=CENTER)
        #     cmb_prix["values"]=("✅","❌")#✔✖
        #     cmb_prix.place(x=700,y=250,width=100)
        #     cmb_prix.current(0)
        #     bus_numl=customtkinter.CTkLabel(frame1,text="numero bus رقم الباص", text_font=("times new roman", 10, "bold"),bg_color="white",fg_color="gray").place(x=1200,y=200)
        #     cmb_bus_num=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        #     cmb_bus_num["values"]=("1"," 2"," 3"," 4","  5"," 6","7","8","9","10")
        #     cmb_bus_num.place(x=1200,y=250,width=50) 
        #     cmb_bus_num.current(0)          
        #     directioinl=customtkinter.CTkLabel(frame1,text_color="white",text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=850,y=200)
        #     cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        #     cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
        #     cmb_dir.place(x=850,y=250,width=scr_width/8)
        #     cmb_dir.current(0)
        #     datel=customtkinter.CTkLabel(frame1,text_color="white",text="Date now", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=10100,y=250)
        #     date=DateEntry(frame1,selectmode='day',font=("times new roman",15),bg="lightgray")
        #     date.place(x=11000,y=200,width=scr_width/8)
        #     impl=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="imprimer طباعة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=1050,y=200)
        #     cmb_imp=ttk.Combobox(frame1,font=("times new roman",20), state="readonly", justify=CENTER)
        #     cmb_imp["values"]=("✔","✖")#
        #     cmb_imp.place(x=1050,y=250,width=scr_width/10)
        #     cmb_imp.current(0)
        #     tele.delete(0,'end')
        #     prix.delete(0,'end')
        
        
        #     # Change Selected Color
        #     style.map('Treeview',background=[('selected', "#347083")])           
        #     style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")

        
        # #serch-------------
        #     serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
        #     serchl.place(x=1000,y=500)
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
                    
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=500)
                
        
        
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
                q="SELECT * FROM message WHERE CURRENT_DATE()=date and bus_num=%s order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q,self.bus_numero)
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
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="white",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=500)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="white",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
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
                        # clear()

                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
            def table():
                conn=connects()
                cur=conn.cursor()
                op=simpledialog.askinteger("Input","أدخل عدد الرسائل للطباعة",parent=my_w)
                value="✖"
                q="SELECT * from message   where CURRENT_DATE()=date  and not imprimer=%s  order by (id) desc limit %s"
                # q="SELECT respteur ,telephone ,prix ,typemessage as type_message,nombre,direction  from message  order by (id) desc limit %s"
                cur.execute(q,(value,op))
                res=cur.fetchall()
                html='''<html>
                    <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>    
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
}.tab{
    display: inline-block;
    margin-left: 300px;
}
                        </style>
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
                # os.startfile("index.html","print")

                import webbrowser
                webbrowser.open("index.html")
                # from htmlpg import webPage
                # webPage("index.html")
                # clear()        
            
            def select(event):
                print(self.bus_numero)
                """
                 this function used when you click the treeview and it will insert the data into input to be updated later\n
                param event is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work
                """
         
         
            btn4=customtkinter.CTkButton(master=frame1,text_font=(20), text="Imprimer طباعة",command=imp, width=50, height=40, compound="right",fg_color="green", hover_color="#C77C78")
            btn4.place(x=550,y=300)
            
            display(0)
       





class Bus:
    """
    if you dont put self behind eny image will not import in others folder \n
    this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()/2+130
        scr_height=self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+300+100"% (scr_width,scr_height)) # Setting width
        self.root.title("Registration Window")
        self.root.config(bg="beige",)
        # self.root.resizable(width=False, height=False)# self.root.resizable(width=False, height=False)


        
        scr_width=root.winfo_screenwidth()
        scr_height=root.winfo_screenheight()
        frame1=Frame(self.root,bg="beige")
        frame1.place(x=10,y=10,width=scr_width/2+160,height=scr_height*0.65)
        frame2=Frame(self.root)
        frame2.place(x=800,y=10,width=700,height=500)

        def reload():
            self.root.destroy()
            os.system("py test.py")
         

         
#reloadfunction
        # def selectionner():

        btn1=customtkinter.CTkButton(master=self.root,command=reload,text="reloead",text_font=(15),width=scr_width/8, height=scr_height/18,text_color="black", compound="right",hover_color="dimgray",fg_color="darkkhaki")
        btn1.place(x=0,y=400)
        # self.root.destroy()
        def showButton():
            conn=connects()
            cur=conn.cursor()
            q="SELECT * FROM buss"
            cur.execute(q)
            res=cur.fetchall()
            v = StringVar()
            for dt in range(len(res)):
                checkButton = Checkbutton(root, text ="Buss numero=>"+str(res[dt]['numero']), variable = v, 
                onvalue =res[dt]['numero'], offvalue = "0", height=2, width = 0, justify='left')
                # checkButton.grid(column=dt,row=0)
                checkButton.pack()

            def select():

                self.root.destroy()
                my_w =customtkinter.CTk()
                Show_Bus(my_w,v.get() )
                my_w.mainloop()
                
        # print(self.v.get())
        
            #***********Row3***********
            btn1=customtkinter.CTkButton(master=self.root,command=select,text="buss selectioner test",text_font=(15),width=scr_width/8, height=scr_height/18,text_color="black", compound="right",hover_color="dimgray",fg_color="darkkhaki")
            btn1.place(x=0,y=100)
        showButton()

root=customtkinter.CTk()
obj=Bus(root)
root.mainloop()
