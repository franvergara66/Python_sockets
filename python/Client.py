#! /python25/python.exe
#! -*- coding: utf-8 -*-

from Tkinter import * 
import Tkinter, Tkconstants, tkFileDialog
import Tkinter
import sys
import socket
import tkMessageBox



def add_to_print():
    # get filename		
    filename = tkFileDialog.askopenfilename(**file_opt)
    # open file on your own
    if filename:
		f= open(filename, 'rb')
		return f
		
def print_pdf():
	filename = tkFileDialog.askopenfilename(**file_opt)
    
	f= open(filename, 'rb')
	l = f.read(1024)
	while (l):
		s.send(l)
		l = f.read(1024)
		
root = Tk() 
s = socket.socket()
s.connect(("localhost",  9999))	 
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

##--------------Adjuntar documento a imprimir------------
button_3 = Button (frame, text="add to print", width=55, height=55, command=add_to_print, background='black', foreground="red")
button_3.pack(side=LEFT)

##---------Imprimir Documento--------------
photo1 = PhotoImage(file="icono_pdf.gif")
button = Button(frame, text= "print", width=55, command=print_pdf(), height=55, background='black', foreground="red") 
button.pack(side= LEFT) 

root.mainloop() 