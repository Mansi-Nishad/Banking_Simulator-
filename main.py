from tkinter import Tk,Label,Frame,Entry,Button,simpledialog,messagebox
from tkinter.ttk import Combobox
import time
import generator
import tables
import mailing
import sqlite3
tables.create_tables()


#it is used to update date & time every 1000 ms(1 sec)
def update_time():
    datetime=time.strftime("📅%d-%b-%y ⏰%r")
    dt_lbl.configure(text=datetime)
    dt_lbl.after(1000,update_time)
    
def forgot_screen():
    frm=Frame(root)
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.7)
    frm.configure(background="pink")
    
    title_lbl=Label(frm,text="This is Forgot Password Screen",
                    font=('arial',25,'bold'),bg="white",fg='purple')
    title_lbl.pack()
    
    def back():
        frm.destroy()
        main_screen()
        
    def send_forgot_otp():
        acn=acn_entry.get()
        email=email_entry.get()

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="select name,pass from accounts where acn=? and email=?"
        curobj.execute(query,(acn,email))
        tup=curobj.fetchone()
        conobj.close()  
        
        if tup!=None:
            otp=generator.forgot_otp()
            text=f"""Hello {tup[0]},
OTP to recover password is = {otp}
"""
            mailing.forgototp_mail(email,text)
            messagebox.showinfo("Forgot","otp sent to registered email")
            attempts=1
            while attempts<=3:
                attempts+=1
                uotp=simpledialog.askinteger("Forgot","OTP")
                if otp==uotp:
                    messagebox.showinfo("Password",tup[1])
                    break
                else:
                    messagebox.showerror("Forgot","Invalid OTP,try again")

        else:
            messagebox.showerror("Forgot","Invalid Details") 
    
    def reset():
        acn_entry.delete(0,"end")
        email_entry.delete(0,"end")
        acn_entry.focus()   
    
    back_btn=Button(frm,text="Back",font=('arial',20,'bold'),background="powder blue",width=10,bd=5,activebackground="dodger blue",cursor="hand2",command=back)
    back_btn.place(relx=0,rely=0)    
    
    acn_lbl=Label(frm,text="Account",font=('arial',20,'bold'),background="pink")
    acn_lbl.place(relx=.3,rely=.2)
    acn_entry=Entry(frm,font=('arial',20,'bold'),bd=5,background="white")
    acn_entry.place(relx=.4,rely=.2)
    acn_entry.focus()
      
    email_lbl=Label(frm,text="Email",font=('arial',20,'bold'),background="pink")
    email_lbl.place(relx=.3,rely=.35)
    email_entry=Entry(frm,font=('arial',20,'bold'),bd=5,background="white")
    email_entry.place(relx=.4,rely=.35)   
    
    otp_btn=Button(frm,text="Send Otp",font=('arial',20,'bold'),background="powder blue",width=8,bd=5,activebackground="dodger blue",cursor="hand2",command=send_forgot_otp)
    otp_btn.place(relx=.4,rely=.53)   

    reset_btn=Button(frm,text="Reset",font=('arial',20,'bold'),background="powder blue",width=6,bd=5,activebackground="dodger blue",cursor="hand2",command=reset)
    reset_btn.place(relx=.52,rely=.53)

def customer_screen(uacn):
    frm=Frame(root,highlightbackground='BLACK',highlightthickness=2)
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.73)
    frm.configure(background="pink")
    
    def logout():
        frm.destroy()
        main_screen()
        
        
        
    def show():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.2,relwidth=.7,relheight=.7)

        title_lbl=Label(ifrm,text="This is Show Details Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack()
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="select * from accounts where acn=?"
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        text=f"""
Account No = {tup[0]}

Acc Open Date = {tup[7]}

Acc Adhar = {tup[5]}

Acc Mob = {tup[4]}

Acc Bal = {tup[3]}

"""
        info_lbl=Label(ifrm,text=text,font=("arial",18),bg="white",fg="blue")
        info_lbl.place(relx=.2,rely=.1)

    def edit():
        
            
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.2,relwidth=.7,relheight=.7)
        

        
        def update():
            name=name_entry.get()
            pwd=pass_entry.get()
            mob=mob_entry.get()
            email=email_entry.get()

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            query="update accounts set name=?,pass=?,mob=?,email=? where acn=?"
            curobj.execute(query,(name,pwd,mob,email,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update","Details Updated")

        
        title_lbl=Label(ifrm,text="This is Edit Details Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack()
        
        name_lbl=Label(ifrm,text="Name",font=('arial',15,'bold'),bg="white")
        name_lbl.place(relx=.15,rely=.13)

        name_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        name_entry.place(relx=.15,rely=.21)
        name_entry.focus()

        email_lbl=Label(ifrm,text="Email",font=('arial',15,'bold'),bg="white")
        email_lbl.place(relx=.55,rely=.13)

        email_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        email_entry.place(relx=.55,rely=.21)
        
        mob_lbl=Label(ifrm,text="Mob",font=('arial',15,'bold'),bg="white")
        mob_lbl.place(relx=.15,rely=.37)

        mob_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        mob_entry.place(relx=.15,rely=.45)

        pass_lbl=Label(ifrm,text="Pass",font=('arial',15,'bold'),bg="white")
        pass_lbl.place(relx=.55,rely=.37)

        pass_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        pass_entry.place(relx=.55,rely=.45)
        
        update_btn=Button(ifrm,text="Update & Save",font=('arial',18,'bold'),
                       bg="green",activebackground="limegreen",bd=5,fg="white",width=12,cursor="hand2",command=update)
    
        update_btn.place(relx=.28,rely=.68)
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="select name,mob,email,pass from accounts where acn=?"
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        name_entry.insert(0,tup[0])
        pass_entry.insert(0,tup[3])
        mob_entry.insert(0,tup[1])
        email_entry.insert(0,tup[2])
        
        def reset():
            name_entry.delete(0,"end")
            email_entry.delete(0,"end")
            mob_entry.delete(0,"end")
            pass_entry.delete(0,"end")
            
        reset_btn=Button(ifrm,text="Reset",font=('arial',18,'bold'),background="green",fg="white",width=12,bd=5,activebackground="limegreen",cursor="hand2",command=reset)
        reset_btn.place(relx=.5,rely=.68)
    
    def deposit():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.2,relwidth=.7,relheight=.7)
        
        title_lbl=Label(ifrm,text="This is Deposit Details Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack()

        uamt=simpledialog.askfloat("Deposit","Amount")
        if uamt==None:
            return
    
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="update accounts set bal=bal+? where acn=?"
        curobj.execute(query,(uamt,uacn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo("Deposit",f"{uamt} deposited")

        
        
    def withdraw():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.2,relwidth=.7,relheight=.7)

        title_lbl=Label(ifrm,text="This is Withdraw Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack()

        uamt=simpledialog.askfloat("Withdraw","Amount")
        if uamt==None:
            return
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="select bal from accounts where acn=?"
        curobj.execute(query,(uacn,))
        bal=curobj.fetchone()[0]
        conobj.close()

        if bal>=uamt:
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            query="update accounts set bal=bal-? where acn=?"
            curobj.execute(query,(uamt,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Withdarw",f"{uamt} withdrawn")
        else:
            messagebox.showerror("Withdraw","Insufficient bal")

    def transfer():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.2,rely=.2,relwidth=.7,relheight=.7)

        title_lbl=Label(ifrm,text="This is Transfer Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack()

        toacn=simpledialog.askinteger("Transfer","To ACN")
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="select * from accounts where acn=?"
        curobj.execute(query,(toacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        if tup!=None:
            uamt=simpledialog.askfloat("Transfer","Amount")

            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            query="select bal from accounts where acn=?"
            curobj.execute(query,(uacn,))
            bal=curobj.fetchone()[0]
            conobj.close()
            if bal>=uamt:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                query1="update accounts set bal=bal-? where acn=?"
                query2="update accounts set bal=bal+? where acn=?"

                curobj.execute(query1,(uamt,uacn))
                curobj.execute(query2,(uamt,toacn))
                
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Transfer",f"{uamt} transfered to {toacn}")
            else:
                messagebox.showerror("Withdraw","Insufficient bal")

        else:
            messagebox.showerror("Transfer","Invalid TO ACN")

    
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    query="select name from accounts where acn=?"
    curobj.execute(query,(uacn,))
    name=curobj.fetchone()[0]
    conobj.close()

    wel_lbl=Label(frm,text=f"Welcome {name.capitalize()}",
                        font=('arial',23,'bold'),bg="pink",fg='purple',background="white")
    wel_lbl.place(relx=.45,rely=0)   
    
    logout_btn=Button(frm,text="⏻Logout",font=('arial',18,'bold'),
                       bg="powder blue",activebackground="dodger blue",cursor="hand2",command=logout,bd=4)
    logout_btn.place(relx=.9,rely=0) 
    
    
    
    show_btn=Button(frm,text="Show Details",font=('arial',20,'bold'),
                       bg="yellow",activebackground="gold",bd=5,width=12,cursor="hand2",command=show)
    show_btn.place(relx=.001,rely=.16)

    
    edit_btn=Button(frm,text="Edit Details",font=('arial',20,'bold'),
                       bg="blue",activebackground="royalblue",bd=5,width=12,cursor="hand2",command=edit)
    
    edit_btn.place(relx=.001,rely=.3)

    
    deposit_btn=Button(frm,text="💰Deposit",font=('arial',20,'bold'),
                       bd=5,width=12,bg="green",activebackground="limegreen",fg="white",cursor="hand2",command=deposit)
    
    deposit_btn.place(relx=.001,rely=.45)

    
    withdraw_btn=Button(frm,text="Withdraw",font=('arial',20,'bold')
                      ,bd=5,width=12,bg="red",activebackground="tomato",fg="white",cursor="hand2",command=withdraw)
    
    withdraw_btn.place(relx=.001,rely=.6)
    
    
    transfer_btn=Button(frm,text="Transfer",font=('arial',20,'bold')
                       ,bd=5,width=12,bg="red",activebackground="tomato",fg="white",cursor="hand2",command=transfer)
    
    transfer_btn.place(relx=.001,rely=.75)
    
    
    
def admin_screen():
    frm=Frame(root)
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.7)
    frm.configure(background="pink")
    
    def logout():
        frm.destroy()
        main_screen()
        
    wel_lbl=Label(frm,text="Welcome Admin",
                        font=('arial',23,'bold'),bg="pink",fg='purple',background="white")
    wel_lbl.place(relx=.45,rely=0)   
    
    
    
    logout_btn=Button(frm,text="⏻Logout",font=('arial',18,'bold'),
                       bg="powder blue",activebackground="dodger blue",cursor="hand2",command=logout,bd=4)
    logout_btn.place(relx=.9,rely=0)  
      
    def new():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.12,rely=.24,relwidth=.79,relheight=.7)
        
        title_lbl=Label(ifrm,text="This is New Account Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack()
        
        def open_acn():
            name=name_entry.get()
            email=email_entry.get()
            mob=mob_entry.get()
            adhar=adhar_entry.get()
            bal=0
            opendate=time.strftime("%d-%b-%Y %r")
            pwd=generator.password()
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            query="insert into accounts values(null,?,?,?,?,?,?,?)"
            curobj.execute(query,(name,pwd,bal,mob,adhar,email,opendate))
            conobj.commit()
            conobj.close()
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            query="select max(acn) from accounts"
            curobj.execute(query)
            acn=curobj.fetchone()[0]
            conobj.close()
            
            
            text=f"""Welcome {name},
We have successfully opened your account in ABC Bank
This is your Credentials,
ACN={acn},
Pass={pwd}
"""
            mailing.openacn_mail(email,text)
            messagebox.showinfo("Account Open","We have opened your account and mailed credentials")

            
            
        name_lbl=Label(ifrm,text="Name",font=('arial',15,'bold'),bg="white")
        name_lbl.place(relx=.15,rely=.13)

        name_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        name_entry.place(relx=.15,rely=.21)
        name_entry.focus()

        email_lbl=Label(ifrm,text="Email",font=('arial',15,'bold'),bg="white")
        email_lbl.place(relx=.55,rely=.13)

        email_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        email_entry.place(relx=.55,rely=.21)
        
        mob_lbl=Label(ifrm,text="Mob",font=('arial',15,'bold'),bg="white")
        mob_lbl.place(relx=.15,rely=.37)

        mob_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        mob_entry.place(relx=.15,rely=.45)

        adhar_lbl=Label(ifrm,text="Adhar",font=('arial',15,'bold'),bg="white")
        adhar_lbl.place(relx=.55,rely=.37)

        adhar_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        adhar_entry.place(relx=.55,rely=.45)
        
        open_btn=Button(ifrm,text="Open Account",font=('arial',20,'bold'),
                       bg="green",activebackground="limegreen",bd=5,fg="white",width=12,cursor="hand2",command=open_acn)
        open_btn.place(relx=.39,rely=.68)
        
    def view():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.12,rely=.24,relwidth=.79,relheight=.7)

        title_lbl=Label(ifrm,text="This is View Account Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack() 
        
        uacn=simpledialog.askinteger("View Account","Enter Account")
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="select * from accounts where acn=?"
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        if tup!=None:
            msg = f"""
Account No : {tup[0]}
Name       : {tup[1]}
Password   : {tup[2]}
Balance    : {tup[3]}
Mobile     : {tup[4]}
Adhar      : {tup[5]}
Email      : {tup[6]}
Open Date  : {tup[7]}
"""
            messagebox.showinfo("Details",msg)
        else:
            messagebox.showerror("Details","Acccount does not exist")
            


        
    def close():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg="white")
        ifrm.place(relx=.12,rely=.24,relwidth=.79,relheight=.7)

        title_lbl=Label(ifrm,text="This is Close Account Screen",
                        font=('arial',20,'bold'),bg="white",fg='purple')
        title_lbl.pack()  
        
        uacn=simpledialog.askinteger("Close Account","Enter Account")
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        query="select name,email from accounts where acn=?"
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        if tup!=None:
            otp=generator.close_otp()
            text=f"Hello {tup[0]}\nOTP to close you account :{otp}"
            mailing.closeotp_mail(tup[1],text)
            messagebox.showinfo("Close","We have sent otp to close account")
            uotp=simpledialog.askinteger("Close OTP","OTP")
            
            if otp==uotp:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                query="delete from accounts where acn=?"
                curobj.execute(query,(uacn,))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Close","Account closed")
            else:
                messagebox.showerror("Close Account","Invalid OTP")
        else:
            messagebox.showerror("Close","Acccount does not exist")

             
    
    newacn_btn=Button(frm,text="New Account",font=('arial',20,'bold'),background="green",width=12,bd=5,activebackground="limegreen",fg="white",cursor="hand2",command=new)
    newacn_btn.place(relx=.14,rely=.1)
    
    viewacn_btn=Button(frm,text="View Account",font=('arial',20,'bold'),background="powder blue",width=12,bd=5,activebackground="dodger blue",cursor="hand2",command=view)
    viewacn_btn.place(relx=.45,rely=.1)
    
    closeacn_btn=Button(frm,text="Close Account",font=('arial',20,'bold'),background="red",width=12,foreground="white",bd=5,activebackground="tomato",cursor="hand2",command=close)
    closeacn_btn.place(relx=.75,rely=.1,)
    
        
def main_screen():
    def refresh():
        global gen_cap
        gen_cap=generator.captcha()
        cap_lbl.configure(text=gen_cap)
        
    def forgot():
        frm.destroy()
        forgot_screen()
    
    def login():
        utype=user_combo.get()
        uacn=acn_entry.get()
        upass=pass_entry.get()
        ucap=cap_entry.get()
        
        if len(uacn)==0:
            messagebox.showerror("Login","Please enter acn")
            return
        if len(upass)==0:
            messagebox.showerror("Login","Please enter password")
            return
        if len(ucap)==0:
            messagebox.showerror("Login","Please enter captcha")
            return
        

        global gen_cap
        gen_cap=gen_cap.replace(" ","")
        if ucap!=gen_cap:
            messagebox.showerror("Login","Invalid Captch")
            return
        
        if utype=="Admin":
            # uacn=int(acn_entry.get())
            # upass=pass_entry.get()
            if uacn=='0' and upass=="admin":
                frm.destroy()
                admin_screen()
            else:
                messagebox.showerror("Login","Invalid Credentials")
                    
        elif utype=="Customer":
            # uacn=int(acn_entry.get())
            # upass=pass_entry.get()
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            query="select * from accounts where acn=? and pass=?"
            curobj.execute(query,(uacn,upass))
            tup=curobj.fetchone()
            conobj.close()
            if tup!=None:
                frm.destroy()
                customer_screen(uacn,)
            else:
                messagebox.showerror("Login","Invalid Credentials")
        else:
            messagebox.showerror("Login","Please select user type")
            
        
    def reset():
        user_combo.current(0)
        acn_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        cap_entry.delete(0,"end")
        user_combo.focus()
               
    frm=Frame(root)
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.7)
    frm.configure(background="pink")
    
    title_lbl=Label(frm,text="This is Login Screen",
                    font=('arial',20,'bold'),bg="white",fg='purple')
    title_lbl.pack()
    
    user_lbl=Label(frm,text="User",font=('arial',20,'bold'),background="pink")
    user_lbl.place(relx=.3,rely=.14)
    
    user_combo=Combobox(frm,values=['---Select---','Admin','Customer'],font=('arial',20,'bold'),background="pink")
    user_combo.place(relx=.4,rely=.14)
    user_combo.current(0)
    
    acn_lbl=Label(frm,text="Account",font=('arial',20,'bold'),background="pink")
    acn_lbl.place(relx=.3,rely=.24)
    acn_entry=Entry(frm,font=('arial',20,'bold'),bd=5,background="white",width=21,

)
    acn_entry.place(relx=.4,rely=.24)
    acn_entry.focus()
    
    pass_lbl=Label(frm,text="Password",font=('arial',20,'bold'),background="pink")
    pass_lbl.place(relx=.3,rely=.34)
    pass_entry=Entry(frm,font=('arial',20,'bold'),bd=5,background="white",show="*",width=21)
    pass_entry.place(relx=.4,rely=.34)
    
    global gen_cap

    gen_cap=generator.captcha()
    cap_lbl=Label(frm,text=gen_cap,font=('arial',20,'bold'),background="white",width=10,bd=5)
    cap_lbl.place(relx=.45,rely=.45)
    
    refresh_btn=Button(frm,text="🔄",font=('arial',13,'bold'),background="powder blue",width=3,command=refresh,bd=5,activebackground="blue",cursor="hand2")
    refresh_btn.place(relx=.57,rely=.45)
    
    
    cap_tex_lbl=Label(frm,text="Captcha",font=('arial',20,'bold'),background="pink",width=10)
    cap_tex_lbl.place(relx=.29,rely=.56)
    cap_entry=Entry(frm,font=('arial',20,'bold'),bd=5,background="white",width=21)
    cap_entry.place(relx=.4,rely=.56)
    
    login_btn=Button(frm,text="Login",font=('arial',20,'bold'),background="powder blue",width=6,bd=5,activebackground="dodger blue",cursor="hand2",command=login)
    login_btn.place(relx=.42,rely=.67)
    
    reset_btn=Button(frm,text="Reset",font=('arial',20,'bold'),background="powder blue",width=6,bd=5,activebackground="dodger blue",cursor="hand2",command=reset)
    reset_btn.place(relx=.51,rely=.67)
    
    forgot_btn=Button(frm,text="Forgot Password",font=('arial',20,'bold'),background="powder blue",width=16,bd=5,command=forgot,activebackground="dodger blue",activeforeground="white",cursor="hand2",padx=5, pady=5)
    forgot_btn.place(relx=.41,rely=.82)
    
    
root=Tk()
root.state("zoomed")
root.configure(bg="powder blue",highlightbackground='black',highlightthickness=2)
root.title("🏦Banking Simulator")


title_lbl=Label(root,text="🏦Banking Simulator🏦",font=('arial',50,'bold','underline'),background="powder blue",fg="dark blue")
title_lbl.pack()

datetime=time.strftime("%d-%b-%Y %r")
dt_lbl=Label(root,text=datetime,font=('arial',20,'bold'),background="powder blue",fg="dark blue")
dt_lbl.pack()
update_time()

footer_lbl=Label(root,text="👩‍💻 ✨Developed by Mansi Nisahd ✨ \n 📞:9999999999 \n 📧  mansinishad123123@gmail.com",font=('Segoe UI Emoji',15,"bold"),background="powder blue",foreground="black")
footer_lbl.pack(side="bottom",pady=2)


main_screen()
root.mainloop()
