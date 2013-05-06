#+----------------------------------+
#| Client TCP/IP                    |
#+----------------------------------+
import socket
s = socket.socket()

#invoco el metodo connect del socket pasando como parametro la tupla IP , puerto
s.connect(("localhost", 9999))

while True:
  mensaje = raw_input("Mensaje a enviar: ")

  #invoco el metodo send pasando como parametro el string ingresado por el usuario
  s.send(mensaje)
  if mensaje == "by":
    break

print "adios"

#cierro socket
s.close()