from Tkinter import *
import mail #import email.py
import cod  #import cod.py 


def payment():
 def pay():
     mail.build_widgets()
     main.destroy()  #this will open new popup and closes the present window
 main = Toplevel()

 text1 = Text(main, height=14, width=39)
 photo=PhotoImage(file='./1.gif',height=900, width=4000) #insert image
  
 text1.image_create(END, image=photo)
 text1.pack(side=TOP)
  #defining buttons specifications
 button1 = Button(main,height=5, width=40)
 button1["text"] = "     COD     "
 button1["command"] = cod.cod
 button1.pack()
 button2 = Button(main,height=5, width=40)
 button2["text"] = "     PICK UP     "
 button2["command"] = pay
 button2.pack()


 
 mainloop()
