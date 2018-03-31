#!/usr/bin/env python3
import socket, threading, os, sys, binascii, re

HOST = "0.0.0.0"
PORT = 50000
SERVERADDR = (HOST, PORT)
TIMEOUT = 10

#Client object
class Client:
	#Initialize with socket obj and address of client
	def __init__(self, conn, addr):
		self.conn = conn
		self.addr = addr
		clientList.append(self)
		print("New Connection\n" + "=" * 40\
			+ "\nIPAddr:{:>33}\nPort:{:>35}\n".format(self.addr[0], self.addr[1])
			+ "=" * 40 + "\n")
		self.conn.settimeout(5)

	#Closing action client
	def close(self, message = "Normal Exit"):
		clientList.remove(self)

		if hasattr(self, "err"):
			message = self.err

		try:
			self.conn.shutdown(socket.SHUT_RDWR)
		except OSError: #Assume client alr closed conn.
			pass

		self.conn.close()
		print("Ended Connection\n" + "=" * 40\
			+ "\nIPAddr:{:>33}\nPort:{:>35}\nStatus: {:}\n".format(self.addr[0], self.addr[1], message)
			+ "=" * 40 + "\n")

		sys.exit()

	#Function to send information to client
	def send(self, message):
		try:
			self.conn.sendall(message.encode())
		# Assume connection was terminated on client side, thus send failed.
		except BrokenPipeError:
			self.close("Sending failed, client dropped\n{:8}connection.".format(""))

	#Receiving data from client
	def receive(self, rawBool = False, bufferSize = 1024):
		try:
			buff = self.conn.recv(bufferSize)
			
			if not rawBool:
				buff = buff.decode()
			else:
				buff = binascii.hexlify(buff)


			print("Client Data Sent\n" + "=" * 40\
			+ "\nIPAddr:{:>33}\nPort:{:>35}\nData: {:}\n".format(self.addr[0], self.addr[1], buff.strip())
			+ "=" * 40 + "\n")

			return buff
		except socket.timeout:
			self.send("Connection timed out!")
			self.close("Connection timed out!")
		except ConnectionResetError:
			self.err = "Receiving failed, client dropped\n{:8}connection.".format("")
			return None

def handler(client):
	client.send("Want the invitation? Gimme the secret code!\n")
	response = client.receive(True)

	response = [response[i:i+2] for i in range(0, len(response), 2)]

	mem = [int(i, 16) for i in response[40:43]]

	if mem == [177, 5, 64] and len(response) == 44:
		client.send("It seems you got the code right!\n")
		client.send("\n{:6}PARTY OF THE YEAR INVITATION\n".format("")
			+ "=" * 40
			+ "\n{:12}Congratulations!\n\n".format("")
			+ "  Use this to gain access to the party\n"
			+ " " * 7 + "GCTF{4W3S0M3_L177L3_P4R7Y}\n"
			+ "=" * 40 + "\n")
	else:
		client.send("Heh, not the right code.\nNo invitation for you blehhhh :)\n")

	client.close()

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(SERVERADDR)
	server.listen(5)

	os.system("cls" if os.name == "nt" else "clear")
	print("Server has started.\n")

	while True:
		try:
			conn, addr = server.accept()
			client = Client(conn, addr)
			threading.Thread(target = handler, args = (client,)).start()
		except KeyboardInterrupt:
			print("\nWaiting for all clients to finish tasks.\n"
				"Please do not forcefully interrupt.\n")
			break

	for i in threading.enumerate():
		if i != threading.current_thread():
			i.join()

	server.close()

if __name__ == "__main__":
	main()