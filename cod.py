from Tkinter import *
import mail
def cod(): #cod button will ask for name, address and phone number
        main = Tk()
        Label(main, text = "NAME  :").grid(row=0)
        num1 = Entry(main)
        num1.grid(row=0, column=1)
        Label(main, text = "PHONE  :").grid(row=1)
        num2 = Entry(main)
        num2.grid(row=1, column=1)
        Label(main, text = "ADDRESS:").grid(row=2)
        num3 = Entry(main)
        num3.grid(row=2, column=1)
        
        def wr(): #defining writing area to write the name address and phone number 
            adds = open ("1.txt", "a")
            adds.write("Name :"+num1.get()+"\n")
            adds.write("Phone :"+num2.get()+"\n")
            adds.write("address :"+num3.get()+"\n")
            adds.close ()
            
    
            r = Tk()
            r.title('Confirm the order')
            r.geometry('150x50')
            rlbl = Label(r, text='Order Placed') #here 'r' means only readable format 
            rlbl.pack()
            b=Button(r, text="confirm", command=mail.build_widgets)
            b.pack(side=BOTTOM)
            r.mainloop()
          
           
            
        Button(main, text='confirm', command=wr).grid(row=3, column=0, sticky=W, pady=4)

        mainloop()
