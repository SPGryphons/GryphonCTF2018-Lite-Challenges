#!/usr/bin/env python3
import math, datetime, socket

def random(seed):
    x = math.sin(seed) * 10000
    return int((x - math.floor(x)) * 10000000000)

server = "127.0.0.1"
port = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to {}:{}...".format(server, port))

s.connect((server, port))
result = s.recv(4096).decode("UTF-8")
print(result)
now = datetime.datetime.now()
seed = now.hour + now.minute
s.send(str(random(seed)).encode())
result = s.recv(4096).decode("UTF-8")
print(result)