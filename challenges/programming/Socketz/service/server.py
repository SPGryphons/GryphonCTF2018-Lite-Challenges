#!/usr/bin/env python3 

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 18177

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(10)

def handle_client_connection(client_socket):
	buf = client_socket.recv(4096).decode()
	if buf == "\xFF"*64:
		msg = "yay! you gave me what i wanted, here's something in return \n GCTF{s0ck3tz_ar3_amaz1ng!!}"
		client_socket.send(msg.encode())
	else:
		msg = "you didn't give me what i wanted :("
		client_socket.send(msg.encode())
	client_socket.close()

while True:
	client_sock, address = server.accept()
	print("Accepted connection from {}:{}".format(address[0], address[1]))
	client_handler = threading.Thread(
		target=handle_client_connection,
		args=(client_sock,)
	)
	client_handler.start()
