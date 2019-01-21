from Tkinter import *
import ScrolledText
import tkFileDialog
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


def build_widgets():
        main = Tk()
        Label(main, text = "Your mail Id:").grid(row=0)
        num1 = Entry(main)
        num1.grid(row=0, column=1)
        
        def mail1(): 
              fromaddr = "vicky.semprojpyt@gmail.com" #applications email id
              toaddr = num1.get() #restaurants email id
 
              msg = MIMEMultipart()
 
              msg['From'] = fromaddr
              msg['To'] = toaddr
              msg['Subject'] = "Confirmation Report"   #subject of the mail
 
              body = "This email is the confirmation of the order. Have a nice day"  #text you want to send to the restaurant
 
              msg.attach(MIMEText(body, 'plain'))
 
              filename = "receipt.txt" #attachment to send
              attachment = open("/home/vikranth/Documents/LiClipse Workspace/new/receipt.txt", "rb")
 
              part = MIMEBase('application', 'octet-stream')
              part.set_payload((attachment).read())
              encoders.encode_base64(part)
              part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
              msg.attach(part)
 
              server = smtplib.SMTP('smtp.gmail.com', 587) #this will set server to use your gmail account
              server.starttls()
              server.login(fromaddr, "Python1*") # password of the gmail account which will send email to restaurant and customer
              text = msg.as_string()
              server.sendmail(fromaddr, toaddr, text)
              server.quit()
              main.destroy()
        
        def mail2():
                    
              fromaddr = "vicky.semprojpyt@gmail.com" #applications email id
              toaddr = "vicky.semprojpyt@gmail.com" #restaurants email id
 
              msg = MIMEMultipart()
 
              msg['From'] = fromaddr
              msg['To'] = toaddr
              msg['Subject'] = "Confirmation Report"   #subject of the mail
 
              body = "This email is the confirmation of the order. Have a nice day"  #text you want to send to the restaurant
 
              msg.attach(MIMEText(body, 'plain'))
 
              filename = "receipt.txt" #attachment to send
              attachment = open("/home/vikranth/Documents/LiClipse Workspace/new/receipt.txt", "rb")
 
              part = MIMEBase('application', 'octet-stream')
              part.set_payload((attachment).read())
              encoders.encode_base64(part)
              part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
              msg.attach(part)
 
              server = smtplib.SMTP('smtp.gmail.com', 587) #this will set server to use your gmail account
              server.starttls()
              server.login(fromaddr, "Python1*") # password of the gmail account which will send email to restaurant and customer
              text = msg.as_string()
              server.sendmail(fromaddr, toaddr, text)
              server.quit()
              
        mail2()
        Button(main, text='confirm', command=mail1).grid(row=3, column=0, sticky=W, pady=4) #defining button

        mainloop()
