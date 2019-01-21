from Tkinter import *
import random    #this is used to select random receipt number from the list of already provided list
from datetime import datetime #importing date and time 
import pay #importing pay.py file so that when we click on order it will redirect us to that window

def ord():  #defining a function called ord and have to declare all the buttons as global 
    global c1
    global c2
    global c3 
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    c1=0    #defining initial values of buttons
    c2=0
    c3=0
    c4=0    
    c5=0
    c6=0    
    c7=0
    c8=0   
    c9=0
    c10=0    

    def ITALIAN_BMT(): #defining  each item 
      global c1
      c1+=1       #increases the counter when we click on the button 

      e1.delete(0, 'end') 
      e1.insert(0,c1)  #text area of button where it shows the number of items that you selected
      
    def PIZZA_SUB():
      global c2
      c2+=1

      e2.delete(0, 'end')
      e2.insert(0,c2) 
    
    def CHICKEN_TERIYAKI():
      global c3
      c3+=1

      e3.delete(0, 'end')
      e3.insert(0,c3)  
      
    def OVEN_ROASTED_CHICKEN():
      global c4
      c4+=1

      e4.delete(0, 'end')
      e4.insert(0,c4) 
    def TUNA_SUB():
      global c5
      c5+=1

      e5.delete(0, 'end')
      e5.insert(0,c5)  
      
    def EGG_SANDWICH():
      global c6
      c6+=1

      e6.delete(0, 'end')
      e6.insert(0,c6) 
    def Ice_Cream():
      global c7
      c7+=1

      e7.delete(0, 'end')
      e7.insert(0,c7)  
      
    def Pastries():
      global c8
      c8+=1

      e8.delete(0, 'end')
      e8.insert(0,c8) 
    def Pops():
      global c9
      c9+=1

      e9.delete(0, 'end')
      e9.insert(0,c9)  
      
    def CHOCOLATE_MILK():
      global c10
      c10+=1

      e10.delete(0, 'end')
      e10.insert(0,c10) 
      
    def total(): #total amount calculation only if the items are not string type
        e11.delete(0, 'end')
        if e1.get()!=str and e2.get()!=str and e3.get()!=str and e4.get()!=str and e5.get()!=str and e6.get()!=str and e7.get()!=str and e8.get()!=str and e9.get()!=str and e10.get()!=str:
          a=6*int(e1.get())+4*int(e2.get())+12*int(e3.get())+17*int(e4.get())+7.5*int(e5.get())+10*int(e6.get())+4.5*int(e7.get())+5*int(e8.get())+2.5*int(e9.get())+4.5*int(e10.get())              
        a+=(a/100.0)*15
        e11.insert(0,a)
                 
    
    def adduser():
        ran=random.randint(0,4) #5 numbers generated
        code=["113626267","12732874","138636186","136868241","274476272"] #list of random receipt number for safety purpose 
        dat = datetime.now()  #date and time 
        ans=dat.strftime('%Y/%m/%d %H:%M:%S')
        adds = open ("receipt.txt", "w")
        adds.write("Welcome to SubWay\t\t\t\t"+ans+"\t\t"+code[ran]+"\n\n")
        
        lis=[e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get()]
        
        for i in range(len(lis)):
         if int(lis[i])>0:
          
          adds.write(dic[i]+" "+": " +lis[i]+"\n\n") 
        adds.write("Price :"+e11.get()+"\n\n\n\n\n")
        adds.write("ADDRESS:\n\nSUBWAY,ARAMARK CANADA, KILLAM LIBRARY\n\nDALHOUSIE UNIVERSITY,HALIFAX")
          
        adds.close ()
        main.destroy()
        return pay.payment() 
 
        
        
    main = Tk()
    
    e1=Entry(main,text=0)  
    e1.insert(0,0)
    e1.grid(row=0,column=1)
    e2=Entry(main)
    e2.insert(0,0)
    e2.grid(row=1,column=1)
    e3=Entry(main)
    e3.insert(0,0)
    e3.grid(row=2,column=1)
    e4=Entry(main)
    e4.insert(0,0)
    e4.grid(row=3,column=1)
    e5=Entry(main)
    e5.insert(0,0)
    e5.grid(row=4,column=1)
    e6=Entry(main)
    e6.insert(0,0)
    e6.grid(row=5,column=1)
    e7=Entry(main)
    e7.insert(0,0)
    e7.grid(row=6,column=1)
    e8=Entry(main)
    e8.insert(0,0)
    e8.grid(row=7,column=1)
    e9=Entry(main)
    e9.insert(0,0)
    e9.grid(row=8,column=1)
    e10=Entry(main)
    e10.insert(0,0)
    e10.grid(row=9,column=1)
    e11=Entry(main)
    e11.insert(0,0)
    e11.grid(row=10,column=1)
    
    
    Button(main, text='ITALIAN_BMT', command=ITALIAN_BMT,width=10).grid(row=0, column=0, sticky=W, pady=4)
    Button(main, text='PIZZA_SUB', command=PIZZA_SUB,width=10).grid(row=1, column=0, sticky=W, pady=4)
    Button(main, text='CHICKEN_TERIYAKI', command=CHICKEN_TERIYAKI,width=10).grid(row=2, column=0, sticky=W, pady=4)
    Button(main, text='OVEN_ROASTED_CHICKEN', command=OVEN_ROASTED_CHICKEN,width=10).grid(row=3, column=0, sticky=W, pady=4)
    Button(main, text='TUNA_SUB', command=TUNA_SUB,width=10).grid(row=4, column=0, sticky=W, pady=4)
    Button(main, text='EGG_SANDWICH', command=EGG_SANDWICH,width=10).grid(row=5, column=0, sticky=W, pady=4)
    Button(main, text='Ice_Cream', command=Ice_Cream,width=10).grid(row=6, column=0, sticky=W, pady=4)
    Button(main, text='Pastries', command=Pastries,width=10).grid(row=7, column=0, sticky=W, pady=4)
    Button(main, text='Pops', command=Pops,width=10).grid(row=8, column=0, sticky=W, pady=4)
    Button(main, text='CHOCOLATE_MILK', command=CHOCOLATE_MILK,width=10).grid(row=9, column=0, sticky=W, pady=4)
    Button(main, text='price', command=total,width=10).grid(row=10, column=0, sticky=W, pady=4)
    
    Button(main, text='PAY', command=adduser,width=10).grid(row=11, column=1, sticky=W, pady=0,)
   
    

    dic={0:"ITALIAN_BMT",1:'PIZZA_SUB',2:'CHICKEN_TERIYAKI',3:'OVEN_ROASTED_CHICKEN',4:'TUNA_SUB',5:'EGG_SANDWICH',6:'Ice_Cream',7:'Pastries',8:'Pops',9:'CHOCOLATE_MILK'}
    mainloop()
