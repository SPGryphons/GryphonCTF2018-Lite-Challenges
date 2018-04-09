#! /usr/bin/env python3
import socket
import re
PORT=18171
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('prog.chal.gryphonctf.com',PORT))
c=client.recv(256)
print(c.decode())
client.sendall("n".encode())
while 1:
	c=client.recv(256).decode()
	if "GCTF" in c:
		print(c)
		break
	print(c)
	num=re.findall(r'\d+', c)
	answer=eval(num[1])*eval(num[2])
	client.sendall(str(answer).encode())
