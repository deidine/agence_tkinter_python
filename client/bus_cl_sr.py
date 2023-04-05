from tkinter import Checkbutton, StringVar, scrolledtext as st
import tkinter as tk
import pymysql
from tkhtmlview import HTMLText, RenderHTML,HTMLLabel
import os
import os,sys

from traitlets import Callable
sys.path.append("..") #this is importent when you import some thing in other folder
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
import customtkinter
from time import strftime
import tkinter
from tkinter import Toplevel, simpledialog

from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk

import tkinter as tk
# from database import connects
def connects():
   return pymysql.connect(host='localhost',user='root',password='',db='agencetk',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

def logo():
    return '<div class="label">سفريات بوه ولد مصطفى<img width="200" height="60" src="images/2.jpg" >BOUHA EL MOUSTAPHA VOYAGES</div>'
    

class Show_Bus:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w,bus_numero,depart) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
            self.bus_numero=bus_numero 
            self.depart=depart        
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
                q="SELECT * from client where nom like %s or  telephone like %s order by (id) desc"
                cur.execute(q,(serchE.get()+"%",serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['numero'],dt['telephone'],dt['direction'],dt['prix'],dt['date'],dt['payer'],dt['emploiyer'],dt['imprimer'],dt['bus_no'],dt['depart']))
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=500)
                
        
        
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
                trv.column("0", width = 100, anchor ='c')
                trv.column("1", width = 180, anchor ='c')
                trv.column("2", width = 40, anchor ='c')
                trv.column("3", width = 100, anchor ='c')
                trv.column("4", width = 180, anchor ='c')
                trv.column("5", width = 40, anchor ='c')
                trv.column("6", width = 180, anchor ='c')
                trv.column("7", width = 50, anchor ='c')
                trv.column("8", width = 100, anchor ='c')
                trv.column("9", width = 60, anchor ='c')
                trv.column("10", width = 60, anchor ='c')
                trv.column("11", width = 60, anchor ='c')
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
                q="SELECT * FROM client WHERE CURRENT_DATE()=date and bus_no=%s and depart=%s order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q,(self.bus_numero,self.depart))
                print(self.bus_numero)
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
                os.system("py showCL.py")
         
           
            def select(ev):
                """
                this function used when you click the treeview and it will insert the data into input to be updated later\n
                param ev is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work

                """
             
             
            def table():
                conn=connects()
                cur=conn.cursor()
                value="✖"
                op=simpledialog.askinteger("Input","أدخل عدد المسافرين للطباعة",parent=my_w)
                q="SELECT numero,telephone,payer,nom,direction  from client where CURRENT_DATE()=date  and bus_no=%s and depart=%s and not imprimer=%s order by (id) desc limit %s"
                cur.execute(q,(self.bus_numero,self.depart,value,op))
                res=cur.fetchall()
                
                html='''<html>
                    <head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>         fieldset{height:50%;}table{height: 50px;font-size:20px;border:1px solid ;border-collapse:collapse;}
                        th,td{border:1px solid;}
                        .p{margin-left:70%;margin-bottom:0px;margin-top:2px;}.i{margin-left:100px;  font-family:sans-serif;}.ii{  font-family:sans-serif;margin-left:300px;}
                        .iii{margin-left:400px;
                        font-family:sans-serif;
                        }i{font-size:20px;}.r{margin-left:50%;    }.a{font-size:20px;margin:auto;}
                        .tab{
display: inline-block;
margin-left: 300px;
}.imp{height:1%;font-size:15px;padding:10px;font-weight:142px;}
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
}     </style>
                        </head><body onload="window.print()">
                           '''+logo()+'''
                <h4> gare Routie ou point de collecte <div class="tab"></div> 
                    المحطة الطرقية أو نقطة التجمع</h4>
                    <h4>nom du rsponsable du gare <div class="tab"></div> إسم مسؤول المحطة  </h4>
                
                    <h4> type du veicule<div class="tab"></div>  نوع السيارة </h4> 
                    <h4>numerodu voiture  <div class="tab"></div> رقم السيارة</h4> 

                    
                    <h4>nom du chauffeur<div class="tab"></div>  إسم السائق</h4> 
                    
                    <table border=1 cellspacing=10 width=90%>
                        <tr>
                        <th>order التنظيم</th>
                            <th>nom de passageur إسم المسافر</th>
                            <th>telephone الهاتف</th>
                            <th>chaise numero  رقم المقعد</th>

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
                    html+='''<td>'''+dt['nom']+'''</td>'''  
                    html+='''<td>'''+str(dt['telephone'])+'''</td>'''
                    html+='''<td>'''+str(dt['numero'])+'''</td>'''  
                    html+='''<td>'''+dt['direction']+'''</td>'''  
                    html+='''<td>'''+dt['payer']+'''</td></tr>'''  
                    i+=1  
                time=strftime('%m-%d-%Y')
                dat="DATE D'IMPRIMATION:\t"+str(time)+"\t:تاريخ الطباعة "
                html+=''' </table><p></p>
                <div class="date"> '''+dat+'''</div>
                 </div>   </fieldset>
                </body>

                    </html>'''
                file.write(html)
                file.close()
                
                
            def imp():
                table()
                import webbrowser
                # os.startfile("index.html","print")

                webbrowser.open("index.html")
                # from htmlpg import webPage
                # webPage("index.html")
                # clear()   
                
         
            btn4=customtkinter.CTkButton(master=frame1,text_font=(20), text="Imprimer طباعة",command=imp, width=50, height=40, compound="right",fg_color="green", hover_color="#C77C78")
            btn4.place(x=550,y=300)
            display(0)      
            

# my_w =customtkinter.CTk()
# my_w1=Show_Bus(my_w,1,"matin")
# my_w.mainloop()



class Bus_Sr:
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

        def select():
            op=simpledialog.askstring("Input","أدخل عدد المسافرين للطباعة",parent=self.root)

            self.root.destroy()
            my_w =customtkinter.CTk()
            Show_Bus(my_w,op,"soir" )
            my_w.mainloop()
                
        # print(self.v.get())
        
            #***********Row3***********
        btn1=customtkinter.CTkButton(master=self.root,command=select,text="buss selectioner test",text_font=(15),width=scr_width/8, height=scr_height/18,text_color="black", compound="right",hover_color="dimgray",fg_color="darkkhaki")
        btn1.place(x=0,y=100)
 
 


root=customtkinter.CTk()
obj=Bus_Sr(root)
root.mainloop()
