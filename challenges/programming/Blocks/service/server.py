#!/usr/bin/env python3
import socket, threading, os, sys, binascii, random

HOST = "0.0.0.0"
PORT = 50000
SERVERADDR = (HOST, PORT)
TIMEOUT = 5

#Client object
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
	def receive(self, bufferSize = 1024):
		try:
			buff = self.conn.recv(bufferSize).decode()

			print("Client Data Sent\n" + "=" * 40\
			+ "\nIPAddr:{:>33}\nPort:{:>35}\nData: {:}\n".format(self.addr[0], self.addr[1], buff.strip())
			+ "=" * 40 + "\n")

			return buff
		except socket.timeout:
			self.send(neh(True))
			self.close("Connection timed out!")
		except ConnectionResetError:
			self.err = "Receiving failed, client dropped\n{:8}connection.".format("")
			return None

def neh(timeFactor = False):
	if timeFactor:
		return "Oops, time's up!\n"

	opps = [
		"Oops, looks like you got it wrong...",
		"That doesn't look right, does it? Hmmm, you failed blehhh.",
		"Gotta try again next time...",
		"Heh, need more practice eh?",
		"Uhoh... Not right my boi"
	]

	selection = random.randint(0, len(opps) - 1)

	return opps[selection] + "\n"

def praise():
	praises = {
		"Awesome job!",
		"Great work :)",
		"You're burning through tis hmm",
		"Hehe, itz easy eh?",
		"Godlike!"
	}

	selection = random.randint(0, len(praises) - 1)

	return praises[selection] + "\n"

def generate(sides):
	pattern = ""
	count = 0

	for i in range(sides):
		for i in range(sides):
			if random.randint(-1,1) == 0:
				pattern += "O"
			else:
				pattern += "#"
				count += 1
		pattern += "\n"

	pattern += "\n"
	return (pattern, count)

def handler(client):
	client.send("Welcome to Blocks:\n\n"
		+ "{:20}HOW TO PLAY\n".format("")
		+ "=" * 51 + "\n"
		+ "1. A pattern of equal height and width will be gen-\n   erated containing blocks of either # or O.\n"
		+ "2. Count the number of # in each pattern.\n"
		+ "3. Send the value back to the server within 5 seco-\n   nds.\n"
		+ "4. There are a total of 50 levels\n"
		+ "5. The height and width of the pattern doubles eve-\n   ry 10 levels\n\n"
		+ "HIT ENTER TO CONTINUE")
	client.receive()
	client.conn.settimeout(TIMEOUT)

	sides, run = 2, 1

	for i in range(0, 5):
		for i in range(0, 10):
			pattern, count = generate(sides)
			client.send("\nLevel {:}:\n\n".format(run) + pattern)
			response = client.receive()

			try:
				if int(response) != count:
					client.send(neh())
					client.close()
				else:
					client.send(praise())
			except ValueError:
				client.send("Only integer values accepted!\n")
				client.close()
			run += 1
		sides *= 2

	client.send("You actually managed to get through this. Not bad :)\n"
		+ "GCTF{I_K1LL3D_1T_1N_BL0CK5}\n")

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