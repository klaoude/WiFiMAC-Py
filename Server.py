import socket

hote = ''
port = 28960

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((hote, port))
tcp.listen(5)
print("Server running on port {}".format(port))

client, info = tcp.accept()

cmd = b""
while cmd != b"fin":
	cmd = client.recv(1024)
	print(cmd.decode())
	client.send(b"done !")

print("closed")
client.close()
tcp.close()