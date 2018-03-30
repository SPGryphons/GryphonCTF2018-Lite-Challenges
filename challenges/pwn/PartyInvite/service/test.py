import socket, threading, os, sys, re

HOST = "localhost"
PORT = 8091
SERVERADDR = (HOST, PORT)
TIMEOUT = 10

clientList = []
fileList = {} #{cityName:'f' - free, 'u' used}

#Client object
class Client:
	#Initialize with socket obj and address of client
	def __init__(self, conn, addr):
		self.conn = conn
		self.addr = addr
		clientList.append(self)
		print("New Connection\n" + "=" * 40\
			+ "\nIPAddr: {:>32}\nPort: {:>34}\n".format(self.addr[0], self.addr[1])\
			+ "=" * 40 + "\n")
		self.conn.settimeout(5)

	#Closing action client
	def close(self, message = "Normal Exit"):
		clientList.remove(self)

		if hasattr(self, "err"):
			message = self.err

		if hasattr(self, "city"):
			if hasattr(self, "writeSuccess"):
				if self.writeSuccess:
					try:
						os.remove(self.city + ".txt")
					except OSError:
						pass

					os.rename(self.city + ".int.txt", self.city + ".txt")
				message += "\nType: Upload"
			else:
				message += "\nType: Report"
			message += "\nCity: " + self.city
			fileList[self.city] = 'f'

		try:
			self.conn.shutdown(socket.SHUT_RDWR)
		except OSError: #Assume client alr closed conn.
			pass

		self.conn.close()
		print("Ended Connection\n" + "=" * 40\
			+ "\nIPAddr: {:>32}\nPort: {:>34}\nStatus: {:}\n".format(self.addr[0], self.addr[1], message)\
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
	def receive(self, bufferSize = 1024):
		try:
			buff = self.conn.recv(bufferSize).decode()
			return buff
		except socket.timeout:
			self.send("Connection timed out!")
			self.close("Connection timed out!")
		except ConnectionResetError:
			self.err = "Receiving failed, client dropped\n{:8}connection.".format("")
			return None