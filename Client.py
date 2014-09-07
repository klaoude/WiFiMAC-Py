import socket

hote = "127.0.0.1"
port = 28960

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect((hote, port))
print("Conexion done on port {}".format(port))

cmd = b""
while cmd != b"fin":
	cmd = input("> ")
	cmd = cmd.encode()
	serv.send(cmd)
	recv = serv.recv(1024)
	print(recv)

print("closed")
serv.close()