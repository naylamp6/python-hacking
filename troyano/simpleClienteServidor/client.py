# python2.7

import socket

servidor = "127.0.0.1" # La IP a conectarse
puerto = 5555 # El mismo puerto que el servidor, obviamente

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
cliente.send("HOLA SERVIDOR");
respuesta = cliente.recv(4096)
print respuesta
