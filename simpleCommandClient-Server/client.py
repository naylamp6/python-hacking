# client.py
# python2.7

import socket

servidor = "127.0.0.1"
puerto = 5555

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
cliente.send("ls /");
respuesta = cliente.recv(4096)
print "[*] Respuesta recibida: "+respuesta
