#+----------------------------------+
#| Server TCP/IP                    |
#+----------------------------------+
import socket
#Creo el objeto socket
s = socket.socket()

#Invoco al metodo bind, pasando como parametro una tupla con IP y puerto
s.bind(("localhost", 9999))

#Invoco el metodo listen para escuchar conexiones con el numero maximo de conexiones como parametro
s.listen(3)

#El metodo accept bloquea la ejecucion a la espera de conexiones
#accept devuelve un objeto socket y una tupla Ip y puerto
sc, addr = s.accept()
print "Recibo conexion de " + str(addr[0]) + ":" + str(addr[1])
addr_2= s.accept()
while True:

  #invoco recv sobre el socket cliente, para recibir un maximo (segun parametro) de 1024 bytes
  recibido = sc.recv(1024)
  if recibido == "by":
    break
  print "Recibido:", recibido

  #Envio la respuesta al socket cliente
  sc.send(recibido)

print "adios"

#cierro sockets cliente y servidor
sc.close()
s.close()