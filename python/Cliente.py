import socket
import Tkinter
import tkMessageBox

s = socket.socket()

#invoco  el metodo connect del socket pasando como parametro la tupla IP , puerto
s.connect(("localhost",  9999))
mensaje1 = raw_input("login: ")
mensaje2 =raw_input("password: ")
s.send(mensaje1)
s.send(mensaje2)
recibido = s.recv(1024)
tkMessageBox.showinfo("ERROR", recibido)


while  True:
 mensaje = raw_input("Mensaje  a enviar: ")

#invoco  el metodo send pasando como parametro el string ingresado por el  usuario
 s.send(mensaje)
 if  mensaje == "by":
	break

print  "adios"

s.close()
