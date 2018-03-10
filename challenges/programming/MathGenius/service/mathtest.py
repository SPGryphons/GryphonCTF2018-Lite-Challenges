#! /usr/bin/env python3
import socket, threading
from random import *
PORT= 30152
start='''Welcome to the Genius Math Test. Answer 20 questions correctly to get the flag\nPress any button to start\n'''

def question(con,addr):
	
	
	try:	
		con.sendall(start.encode())
		con.settimeout(20)
		startTest=con.recv(100)
		con.settimeout(5)
		if startTest:
			for i in range(20):
				i=i+1
				x=randint(2,pow(3,i))
				y=randint(2,pow(3,i))
				buf='Level '+str(i)+'\n'+str(x)+' x '+str(y)+' => '
				con.sendall(buf.encode())
				Answer=x*y
				userAns=con.recv(100)
				try:
					if Answer!=int(userAns):
						con.sendall("Wrong answer\n".encode())
						con.close()
						return
				except ValueError:
					con.sendall("Invalid Input\n".encode())
					con.close()
				except socket.timeout:
					con.sendall("Too Slow Kid\n".encode())
					con.close()
			
			con.sendall("GCTF{G3N1u5_K1Dz}\n".encode())
			con.close()
	except socket.timeout:
		con.sendall("\nYou are too slow\n".encode())
		con.close()



serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0',PORT))
serversocket.listen(5)
print("Server started")
while(1):
	con,addr=serversocket.accept()
	#con.settimeout(5)
	print("A new connection to ",addr)
	threading.Thread(target = question,args = (con,addr)).start()
	


question(con)
