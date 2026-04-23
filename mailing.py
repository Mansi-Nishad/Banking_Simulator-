import gmail

def openacn_mail(to,text):
    con=gmail.GMail("mansinishad123123@gmail.com","zsyo hflg ovkt wbxb")
    msg=gmail.Message(to=to,subject="Account Opened in ABC Bank",text=text)
    con.send(msg)
    
def closeotp_mail(to,text):
    con=gmail.GMail("mansinishad123123@gmail.com","zsyo hflg ovkt wbxb")
    msg=gmail.Message(to=to,subject="OTP to close account",text=text)
    con.send(msg)  
    

def forgototp_mail(to,text):
    con=gmail.GMail("mansinishad123123@gmail.com","zsyo hflg ovkt wbxb")
    msg=gmail.Message(to=to,subject="OTP to recover password",text=text)
    con.send(msg)     