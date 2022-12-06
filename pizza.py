from tkinter import *
import time
from sqlite3 import *
import random
from tkinter import messagebox

class Pizza:
    cartlist=[]
    amount=0
#--  page 1------
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()
            except:
                pass

        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))
        sf.scr.title("Python Tkinter GUI application")
        #sf.scr.resizable(False, False)
        sf.scr.iconbitmap('p.ico')
        sf.mainf1=Frame(sf.scr,height=100,width=1000)
        sf.logo=PhotoImage(file="logo1.png")
        sf.l=Label(sf.mainf1,image=sf.logo)
        sf.l.place(x=70,y=0)
        sf.mainf1.pack(fill=BOTH,expand=1)
        sf.mainf2=Frame(sf.scr,height=618,width=1000)
        sf.c=Canvas(sf.mainf2,height=618,width=1000)
        sf.c.pack()
        sf.back=PhotoImage(file="pizzamain.png")
        sf.c.create_image(500,304,image=sf.back)
        sf.lab=Button(sf.mainf2,text= "Click Here to Enter store",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("algerian",30, 'bold'),fg="black",bg="#a80202")
        sf.lab.place(x=190,y=250)
        
        sf.mainf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#------ page 2------
    def Login(sf):
        sf.cartlist=[]
        sf.amount=0
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Python Tkinter GUI application")
        sf.scr.geometry('%dx%d+%d+%d' % (1000, 650, 100, 0))
        #sf.scr.resizable(False, False)
        sf.loginf1=Frame(sf.scr,height=150,width=1000)
        sf.logo=PhotoImage(file="logo1.PNG")
        sf.ba=Label(sf.loginf1,image=sf.logo,height=150).place(x=70,y=0)
        sf.home=Button(sf.loginf1,text="Home",command=lambda:sf.main(),bg="black",cursor="hand2",bd=4,fg="white",font=("algerian",16))
        sf.home.place(x=10,y=110)
        sf.adlog=Button(sf.loginf1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bd=4,bg="black",fg="white",font=("algerian",16))
        sf.adlog.place(x=370,y=110)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.tim=Label(sf.loginf1,text=sf.localtime,fg="white",font=("default",16),bg="black")
        sf.tim.place(x=730,y=110)
        sf.loginf1.pack(fill=BOTH,expand=1)
        sf.loginf2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.loginf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(500,309,image=sf.logo1)
        sf.c.create_rectangle(250,100,780,450,fill="#a80202",outline="white",width=6)
        sf.log=Label(sf.loginf2,text="LOGIN",fg="white",bg="black",width=20,font=("algerian",27))
        sf.log.place(x=289,y=105)
        sf.lab1=Label(sf.loginf2,text="UserName",bg="#a80202",font=("algerian",22))
        sf.lab1.place(x=260,y=180)
        sf.user=Entry(sf.loginf2,bg="white",font=("algerian",22),bd=6 ,justify='left')
        sf.user.place(x=420,y=180)
        sf.lab2=Label(sf.loginf2,text="Password",bg="#a80202",font=("algerian",22))
        sf.lab2.place(x=260,y=250)
        sf.pasd=Entry(sf.loginf2,bg="white",font=("algerian",22),bd=6 ,justify='left')
        sf.pasd.place(x=420,y=250)
        sf.lg=Button(sf.loginf2,text="Login",cursor="hand2",command=lambda:sf.logindatabase(),fg="white",bg="black",font=("algerian",20),bd=4)
        sf.lg.place(x=360,y=320)
        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)
        sf.cl=Button(sf.loginf2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="black",font=("algerian",20),bd=4)
        sf.cl.place(x=560,y=320)
        sf.rg=Button(sf.loginf2,text="New into MyPizzaStore",command=lambda:sf.Register(),fg="white",cursor="hand2",bg="#8c68c1",font=("algerian",20),bd=6)
        sf.rg.place(x=340,y=380)
        # sf.c.create_rectangle(850,120,1310,480,fill="#d3ede6",outline="white",width=4)
        # sf.ext=PhotoImage(file="p4.png")
        # sf.url=Label(sf.loginf2,image=sf.ext,cursor="hand2").place(x=855,y=125)
        sf.loginf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultlog(sf):
        sf.loguser=sf.user.get()
        sf.logpass=sf.pasd.get()
        return sf.loguser,sf.logpass


#--  page 3------
    def Adminlogin(sf):
        sf.scr.destroy()
        sf.scr=Tk()
        sf.scr.title("Python Tkinter GUI application")
        sf.scr.geometry("1366x768")
        #sf.scr.resizable(False, False)
        sf.adminf1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.adminf1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.adminf1,text="Home",command=lambda:sf.main(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1000,y=90)
        sf.localtime=time.asctime(time.localtime(time.time()))
        sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.adminf1.pack(fill=BOTH,expand=1)
        sf.adminf2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.adminf2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(350,100,1016,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.adminf2,text="ADMIN LOGIN",fg="white",bg="#0b1335",width=27,font=("algerian",27))
        sf.log.place(x=357,y=110)
        sf.lab1=Label(sf.adminf2,text="UserName",bg="#d3ede6",font=("algerian",22))
        sf.lab1.place(x=400,y=200)
        sf.usera=Entry(sf.adminf2,bg="white",font=("algerian",22),bd=5)
        sf.usera.place(x=650,y=200)
        sf.lab2=Label(sf.adminf2,text="Password",bg="#d3ede6",font=("algerian",22))
        sf.lab2.place(x=405,y=270)
        sf.pasda=Entry(sf.adminf2,bg="white",font=("algerian",22),bd=5)
        sf.pasda.place(x=650,y=270)
        sf.lg=Button(sf.adminf2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.admindatabase(),font=("algerian",20,'bold'),bd=5)
        sf.lg.place(x=650,y=350)
        sf.cl=Button(sf.adminf2,text="Back",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Login(),font=("algerian",20,'bold'),bd=5)
        sf.cl.place(x=400,y=350)
        def clear(sf):
            sf.usera.delete(0,END)
            sf.pasda.delete(0,END)
        sf.rg=Button(sf.adminf2,text="Clear",fg="white",cursor="hand2",bg="#0b1335",command=lambda:clear(sf),bd=5,font=("algerian",20,'bold'))
        sf.rg.place(x=900,y=350)
        
        sf.adminf2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()


 #-----  database-------               
    def logindatabase(sf):
        sf.credlog=sf.resultlog()
        sf.con=connect("pizza.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r and password=%r"%(sf.credlog[0],sf.credlog[1]))
        if list(x)[0][0]==0:
            if sf.credlog[0]=="" or sf.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            messagebox.showinfo("Login","You have Successfully Log In\nWelcome to PizzaStore")            
            sf.pizmain()

        
x=Pizza()
x.main()
