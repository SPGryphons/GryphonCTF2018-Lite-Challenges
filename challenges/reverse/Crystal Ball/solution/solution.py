#!/usr/bin/env python3
import math, socket, ntplib, re, datetime
from time import ctime

def random(seed):
    x = math.sin(seed) * 10000
    return int((x - math.floor(x)) * 10000000000)

server = "127.0.0.1"
# port = 18211
port = 5002

x = ntplib.NTPClient()
# print(datetime.datetime.utcfromtimestamp(x.request('pool.ntp.org').tx_time))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to {}:{}...".format(server, port))

s.connect((server, port))
result = s.recv(4096).decode("UTF-8")
print(result)
seed = sum(list(map(int, re.search(r'\d\d:\d\d:', str(datetime.datetime.utcfromtimestamp(x.request('pool.ntp.org').tx_time))).group(0)[:-1].split(':'))))
# Alternative without using ntp server
# seed = sum(map(int, datetime.datetime.utcnow().strftime("%H:%M").split(':'))))
s.send(str(random(seed)).encode())
result = s.recv(4096).decode("UTF-8")
print(result)