import gmail

def openacn_mail(to,text):
    con=gmail.GMail("your_email@gmail.com","your_app_password")
    msg=gmail.Message(to=to,subject="Account Opened in ABC Bank",text=text)
    con.send(msg)
    
def closeotp_mail(to,text):
    con=gmail.GMail("your_email@gmail.com","your_app_password")
    msg=gmail.Message(to=to,subject="OTP to close account",text=text)
    con.send(msg)  
    

def forgototp_mail(to,text):
    con=gmail.GMail("your_email@gmail.com","your_app_password")
    msg=gmail.Message(to=to,subject="OTP to recover password",text=text)
    con.send(msg)     
