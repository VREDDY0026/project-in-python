SUBWAY FOOD CALCULATOR AND LOCATION FINDER

Installation Guide:

In order to execute this files you need to install virtual box in any windows system and then run ubuntu desktop file.
This will help you in building Virtual machine. So we need an interpretor pydev 2.7 which is already a part of liclipse.
So we need to install liclipse and this installation includes a couple of codes:
sudo tar xvzf liclipse_3.0.1_linux.gtk.x86.tar.gz
Move the extracted folder to /opt folder using the command

sudo mv liclipse /opt
Now create a shortcut of LiClipse in the applications folder:

sudo ln -s /opt/liclipse/LiClipse /usr/bin/liclipse
We have now installed LiCipse in our system. But we need to create a launcher for easier access. Paste the following command
in terminal to create the launcher

sudo nano /usr/share/applications/liclipse.desktop
Paste the following content in the file. NB: in my case I used the version 3.0.1, you should use the version you are working with.

[Desktop Entry]
Version=3.0.1(tentative)
Name=LiClipse
Comment=IDE for Python/Django developers
Exec=env UBUNTU_MENUPROXY=0 /opt/liclipse/LiClipse
Icon=/opt/liclipse/icon.xpm
Terminal=false
Type=Application
Categories=Utility;Application;Development;IDE
Rest of the content should not be changed. Save this file :

CTRL+O : To save the changes.
CTRL+X : To exit

So, after this installation we need to install packages like tkinker and requests for importing code from one file into another.


Also we need to download a .gif subway logo and track its location into menu.py and create any .txt file and track its location into order.py and mail.py.






Steps to run the program:

There are six python files in order to completely execute this. My complete python package includes
1.menu.py
2.order.py
3.pay.py
4.cod.py
5.mail.py
6.GEO.py

Here we need to run this according to the order mentioned above.

This project is like a desktop app student friendly one where students can order their food from subway. The main reason behind this desktop app is that 
subway do not have websites and servers. For example, if we have servers there will be chances of hanging. For this desktop app there will not be such problems.

First we run this menu.py file in liclipse python 2.7 interpretor. Then the GUI window will be displayed with menu of food items and then we need to select 
the food item after pressing the order button through menu window and after that selection we need to pay.

Then pay.py comes into action and asks for the mode of delivery whether it is pick-up or COD. If we select COD mode then COD.py comes into action asks for 
the entry name fields. And after that new window comes askingfor the email. So atlast we need to type in email id.Then a receipt will be coming to both the 
student whose email id is given and to the store.

For example, if we need to know the exact location co-ordinates of the store inside the university through GEO.py file.
       