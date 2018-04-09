#!/usr/bin/env python3
import socket, threading, os, sys, binascii, re

HOST = "prog.chal.gryphonctf.com"
PORT = 18175
SERVERADDR = (HOST, PORT)
TIMEOUT = 5
# Arbitarily large buffer size
BUFFSIZE = 65536

def main():
	# Make socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(SERVERADDR)
	sock.settimeout(TIMEOUT)
	# Since first text is just rules,
	# receive and send smth to continue
	sock.recv(BUFFSIZE)
	sock.sendall("\n".encode())

	while True:
		response = sock.recv(BUFFSIZE).decode()

		if not response:
			break

		if re.search("Level", response):
			count = response.count("#")
			sock.sendall(str(count).encode())
		else:
			print(response)

if __name__ == "__main__":
	main()