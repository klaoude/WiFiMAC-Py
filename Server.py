import socket

hote = ''
port = 28961

gui = False
ju = False
cle = False

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((hote, port))
tcp.listen(5)
print("Server running on port {}".format(port))

client, info = tcp.accept()

cmd = b""
while cmd != b"fin":
	cmd = client.recv(1024)
	print(cmd.decode())
	if(cmd == "stop gui" and gui == True):
	    client.send(b"connexion of guillaume stop !")
	    gui = False
	elif(cmd == "stop gui" and gui == False):
	    client.send(b"connexion of guillaume is already stop !")
	elif(cmd == "start gui" and gui == False):
	    client.send(b"connexion of guillaume start !")
	    gui = True
	else:
	    client.send("error")

print("closed")
client.close()
tcp.close()