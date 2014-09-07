import socket

from tkinter import *

hote = "127.0.0.1"
port = 28961

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect((hote, port))
print("Conexion done on port {}".format(port))

cmd = ""
while cmd != "fin":
	cmd = raw_input("> ")
	serv.send(cmd)
	recv = serv.recv(1024)
	print(recv)

print("closed")
serv.close()