#! /python26/python.exe
#! -*- coding: utf-8 -*-

from Tkinter import * 
import Tkinter, Tkconstants, tkFileDialog
import Tkinter
import sys
import socket
import tkMessageBox

flag = False
class Exit_Button(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.widget1()

def exit():
	root.destroy()
	s.close()
def login():
	global flag
	#invoco  el metodo connect del socket pasando como parametro la tupla IP , puerto 
	login = value.get()
	password = value_2.get()
	if ((len(login) == 0) or (len(password)) == 0):
		tkMessageBox.showinfo("Error", "insert correct login and password") 
		salir ()
	else:
		s.send(login)
		s.send(password)
		recibido = s.recv(1024)
		tkMessageBox.showinfo("Notify", recibido)
		if (recibido=="Error Check user & Password"):
			salir ()
		else:
			flag = True
			
def attach_to_print():
	global flag
	if (flag==False):
		tkMessageBox.showinfo("Error", "You must login") 
		salir ()
	else:
    # get filename		
		filename = tkFileDialog.askopenfilename(**file_opt)
    # open file on your own
		if filename:
			f= open(filename, 'rb')
			l = f.read(1024)
			s.send (filename)					
			while (l):
				s.send(l)
				l = f.read(512)				
			
		

##@@--------------------------------------------------------------------------------@@##	
	
root = Tk() 
s = socket.socket()
s.connect(("localhost",  9999))	 
# define options for opening or saving a file
file_opt = options = {}
options['defaultextension'] = '' # couldn't figure out how this works, magic dont touch
options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
options['initialdir'] = 'C:\\'
options['initialfile'] = 'myfile.txt'
options['parent'] = root
options['title'] = 'This is a title'


frame = Frame(root) 
frame.pack(side=LEFT) 
frame.master.title("Servicio de impresion")
value = StringVar()
value_2 = StringVar()

w =  Label(root, text="User Name", fg="red")
w.pack(side = LEFT)
entry_1 = Entry(root, textvariable=value_2, bd =5, show="*")
entry_1.pack(side = RIGHT)
entry_1.insert(0,"robin")

z=  Label(root, text="Password", fg="red")
z.pack(side = RIGHT)
entry_0 = Entry(root, textvariable=value, bd =5)
entry_0.pack(side = RIGHT)
entry_0.insert(0,"batman")

##---------------login----------------
photo0 = PhotoImage(file="login.gif")
button_0= Button (frame,  image=photo0, width=55,  command= login, height=55, bg='black', text="login", foreground ="white") 
button_0.pack()

##--------------Attach and print File------------
photo2= PhotoImage(file="icono_pdf.gif")
button_3 = Button (frame, image=photo2, width=55, height=55, command=attach_to_print, bg='black')
button_3.pack(side=LEFT)



##-----------------Exit------------------------
photo1 = PhotoImage(file="yao.gif")
button = Button(frame, image=photo1, command= exit, width=55,  height=55, bg='black', foreground ="white") 
button.pack(side= LEFT)

root.mainloop()