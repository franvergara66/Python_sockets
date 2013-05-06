#! /python25/python.exe
#! -*- coding: utf-8 -*-

from Tkinter import * 
import Tkinter, Tkconstants, tkFileDialog
import Tkinter
import sys


class Exit_Button(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.widget1()

def salir():
    root.destroy()
    
def set_value():
    value.set("Password Invalido")



def adjuntar():
    # get filename
    filename = tkFileDialog.askopenfilename(**file_opt)
    # open file on your own
    if filename:
      return open(filename, 'r')

def iniciar_sesion():	
	login = value.get()
	password = value_2.get()
	print login, password
	
	  
	  
root = Tk() 

# define options for opening or saving a file
file_opt = options = {}
options['defaultextension'] = '' # couldn't figure out how this works
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




z=  Label(root, text="Password", fg="red")
z.pack(side = RIGHT)
entry_0 = Entry(root, textvariable=value, bd =5)
entry_0.pack(side = RIGHT)

##---------------iniciar Sesion----------------
photo0 = PhotoImage(file="login.gif")
button_0= Button (frame,  image=photo0, width=55,  command= iniciar_sesion, height=55, bg='black', text="login", foreground ="white") 
button_0.pack()

##--------------Adjuntar documento a imprimir------------
photo2= PhotoImage(file="pdf.gif")
button_3 = Button (frame, image=photo2, width=55, height=55, command=adjuntar, bg='black')
button_3.pack(side=LEFT)

##---------Imprimir Documento--------------
photo1 = PhotoImage(file="icono_pdf.gif")
button = Button(frame, image=photo1, width=55,  height=55, bg='black', text="Imprimir", foreground ="white") 
button.pack(side= LEFT) 

##-----------------Salir------------------------
photo3 = PhotoImage(file="yao.gif")
button_1 = Button(frame, image=photo3, width=55, command=salir, height=55, bg='black', text="Salir", foreground ="white") 
button_1.pack()





root.mainloop() 