#!/usr/bin/env python3
import socket, threading, os, sys, pattern

HOST = "0.0.0.0"
PORT = 50000
SERVERADDR = (HOST, PORT)
TIMEOUT = 3

class Client:
	#Initialize with socket obj and address of client
	def __init__(self, conn, addr):
		self.conn = conn
		self.addr = addr
		print("New Connection\n" + "=" * 40\
			+ "\nIPAddr:{:>33}\nPort:{:>35}\n".format(self.addr[0], self.addr[1])
			+ "=" * 40 + "\n")

	#Closing action client
	def close(self, message = "Normal Exit"):
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
			buff = self.conn.recv(bufferSize).decode()

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
	client.send("Find your way out of the Maze :)\n"
		+ "{:20}HOW TO PLAY\n".format("")
		+ "=" * 51 + "\n"
		+ "1. A 50 x 50 maze will be generated containing blo-\n   cks ▓ and ░.\n"
		+ "2. The initial position of the player is marked by\n   the \"@\" symbol\n"
		+ "3. ▓ indicate walls that are should not be touched\n   ░ indicates path that can be taken.\n"
		+ "4. There are 10 mazes to complete\n"
		+ "5. Players have 3 seconds to complete the maze.\n"
		+ "\nExample:\n"
		+ "▓▓▓▓▓▓▓▓▓\n"
		+ "▓▓▓▓▓▓▓▓▓\n"
		+ "▓▓▓▓▓▓▓▓▓\n"
		+ "▓▓▓▓▓▓▓▓▓\n"
		+ "▓▓▓▓▓▓▓▓▓\n"
		+ "▓▓▓░░░░░░\n"
		+ "▓▓▓@▓▓▓▓▓\n"
		+ "▓▓▓▓▓▓▓▓▓\n"
		+ "▓▓▓▓▓▓▓▓▓\n"
		+ "Solution: \"up right right right right right\"\n\n"
		+ "HIT ENTER TO CONTINUE")
	client.receive()
	client.conn.settimeout(TIMEOUT)
	newline = ""

	for i in range(1, 11):
		maze = pattern.Maze(50)
		client.send("\nLevel " + str(i) + ":\n" + maze.getMaze() + "\nSolution: ")
		response = client.receive()

		if response != maze.getSolution():
			client.send("Ehh, try again next time!\n")
			client.close()

		newline += "\n"

	client.send("Nicely done! The flag's GCTF{7H3_GL4D3}")
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