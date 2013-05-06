from Tkinter import * 
import Tkinter, Tkconstants, tkFileDialog
import Tkinter
import sys
import socket
import tkMessageBox
import cPickle as pickle
root = Tk() 
frame = Frame(root) 
frame.pack(side=LEFT) 
frame.master.title("Servidor de impresion")

s = socket.socket()
s.bind(("localhost",9999))
s.listen(10) # Acepta hasta 10 conexiones entrantes.
sc, address = s.accept()
print address
f = open('file_.txt','wb')
# recibimos y escribimos en el fichero
l = sc.recv(1024)
while (l):
	f.write(l)
	l = sc.recv(1024)
f.close()

 
sc.close()
s.close()
