from Tkinter import *  #importing tinker 
import order  #importing order.py file


root = Tk()
#used GIF image, because PhotoImage() takes only .gif files. also specified the height width of image 
text1 = Text(root, height=14, width=39)
photo=PhotoImage(file='./1.gif',height=900, width=4000)
 
text1.image_create(END, image=photo)

text1.pack(side=TOP) #pack is used to place image on top

#here i have defined the area for the menu and some style of my text eg. item names
text2 = Text(root, height=25, width=39)

text2.tag_configure('bold_italics', font=('Arial', 8, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 8, 'bold'))
text2.tag_configure('color', foreground='#476042', 
                        font=('Tempus Sans ITC', 8, 'bold'))

text2.insert(END,'\n\tWelcome To University SUBWAY', 'big')
text2.insert(END,'\n\t\t Menu\n','big')
quote = """
STARTERS(COST):       
----------------------------
ITALIAN BMT($6)    
PIZZA SUB($4)                 
                 
MAIN COURSE(COST)  :
----------------------------
CHICKEN TERIYAKI($12)          
OVEN ROASTED CHICKEN($17)          
TUNA SUB($7.5)         
EGG SANDWICH($10)       

DESERTS(COST)  :
----------------------------   
ICE-CREAM($4.5)
PASTRIES($5)     

DRINKS(COST)  :
----------------------------
POPS($2.5)
CHOCOLATE MILK($4.5)
"""
text2.insert(END, quote, 'color')
text2.configure(state='disabled')

text2.pack()
button1 = Button(root,height=1, width=31) #creating button()
button1["text"] = "      ORDER     "  #button name
button1["command"] = order.ord #button will refer to ord function defined in order.py
button1.pack(side=BOTTOM) #button is packed at bottom

root.mainloop() #this will keep application running (like infinite loop)
