from Tkinter import * 
import Tkinter, Tkconstants, tkFileDialog
import Tkinter
import sys
import socket
import tkMessageBox
from threading import Thread
#please note: I'm not sure if the two lines above actually work; I can't test 
def onclick():
   pass
   
root = Tk()
root.title("Print Server")
text = Text(root, width=60, height=30)
text.pack()

tkinterThread= Thread(target=Tk.mainloop, args=[root])#spawn a new Thread object
tkinterThread.start()#make the thread execute the tkinter mainloop
s = socket.socket()

s.bind(("localhost",  9999))
s.listen(100)


tkinterThread= Thread(target=Tk.mainloop, args=[root])#spawn a new Thread object
tkinterThread.start()#make the thread execute the tkinter mainloop
#please note: I'm not sure if the two lines above actually work; I can't test them because Tkinter won't work for me.

def listenToClient(sc, address):
	i=0
	recibido1 = sc.recv(1024)
	recibido2 = sc.recv(1024)
	print  "login:", recibido1, "password: *******"
	salida = (str(recibido1)+" "+str(recibido2)+"\n")
	archivo = open("passwordlist.txt", "r") 
	while True:
		linea = archivo.readline()  #Leo del archivo
		if (salida==linea):
			log_ok ="login ok"
			sc.send(log_ok)      
			break
		if (len(linea))==0:
			error= "Error Check user & Password"
			sc.send(error)
			break
	f = open('print_'+ str(i)+".pdf",'wb') #abierto en escritura binaria
	i=i+1   
# recibimos y escribimos en el fichero
	nombre_archivo = sc.recv(1024)
	cadena = "On Printing Queue.."+nombre_archivo+"\n"
	print cadena
	text.insert(INSERT, cadena)
	print "On Printing  Queue.."+nombre_archivo
	l = sc.recv(1024)
	while (l):
		f.write(l)
		l = sc.recv(1024)
		if not l: 
			notification= "Complete transfer"
			#sc.send(notification)
			break
	f.close() 
	sc.close()

while (True):
    sc, address = s.accept()
    print "Connection from: ", address
    clientThread= Thread(target=listenToClient, args=[sc,address])#spawn a new thread object
    clientThread.start()#start the thread; it'll execute the "listenToCli