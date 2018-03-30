#!/usr/bin/env python3
import socket

server = "127.0.0.1"
port = 5001

def getNumer(str):
    return int(str.split('\n')[1])

def is_prime(num):
    if num < 2:
        return False
    elif num != 2 and num % 2 == 0:
        return False
    else:
        return all (num % i for i in range(3, int(num**0.5)+1))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to {}:{}...".format(server, port))

s.connect((server, port))
result = s.recv(4096).decode("UTF-8")
while True:
    result = s.recv(4096).decode("UTF-8")
    print(result)
    if 'GCTF{' in result:
        break
    if is_prime(getNumer(result)):
        s.send(str("true").encode())
    else:
        s.send(str("false").encode())
