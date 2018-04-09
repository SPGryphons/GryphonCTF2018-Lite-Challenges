#!/usr/bin/env python3
import socket
PORT = 18173


def binary_search(table, query):
    index = int(len(table) / 2)
    partition = int(len(table) / 2)

    while True:
        #print(query, index, table[index][0], partition)
        partition = max(1, int(partition / 2))
        if int(table[index][0]) <= query and query <= int(table[index][1]):
            #print(table[index][2])
            return table[index][2]
        elif int(table[index][0]) > query:
            index = index - partition
        else:
            index = index + partition


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost', PORT))
for i in range(10):
    raw_data = ''
    while 1:
        data = client.recv(1024).decode()
        if not data:
            break
        raw_data += data
        if data.strip().endswith(':'):
            break
    #print(raw_list)
    raw_data = raw_data.splitlines()
    table_data = [i.split(',') for i in raw_data[1:-1]]
    for j in range(10):
        q = 0
        if j == 0:
            q = int(raw_data[-1].split(':')[0])
        else:
            q = int(client.recv(1024).decode().split(':')[0])

        a = binary_search(table_data, q)
        print('{}: {}'.format(q, a))
        client.sendall('{}\n'.format(a).encode())

print('FLAG:', client.recv(1024).decode().strip())
