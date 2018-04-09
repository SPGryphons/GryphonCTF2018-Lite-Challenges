#!/usr/bin/env python3
import socket, threading, random
PORT = 18173
NAMES = []
MAX_VALUES = [100, 1000, 10000, 100000, 1000000, 10000000, 50000000, 100000000, 500000000, 1000000000]
INTERVALS = [10, 25, 50, 100, 500, 1000, 10000, 10000, 10000, 10000]

def client(con, addr):
    try:
        for i in range(10):
            con.settimeout(10)
            max_value = 0
            values = []
            while max_value < MAX_VALUES[i]:
                min_value = max_value
                max_value += INTERVALS[i] + random.randrange(-INTERVALS[i] // 2, INTERVALS[i] // 2)
                values.append((min_value, max_value - 1, random.choice(NAMES)))
            con.sendall('{}\n'.format(len(values)).encode())
            for v in values:
                con.sendall('{},{},{}\n'.format(v[0], v[1], v[2]).encode())
            con.settimeout(1)
            for j in range(10):
                q = random.choice(values)
                con.sendall('{}: '.format(random.randint(q[0], q[1])).encode())
                client_ans = con.recv(1024)
                if client_ans.decode().strip() != q[2]:
                    con.sendall('\nWrong Answer\n'.encode())
                    con.close()
                    return
        con.sendall('GCTF{71m3_c0mpl3x17y_w0n7_570p_m3}\n'.encode())
        print('{} HAS GOTTEN THE FLAG'.format(addr[0]))
    except socket.timeout:
        con.sendall('\nTime Limit Exceeded\n'.encode())
        con.close()


if __name__ == '__main__':
    print('READING NAMES...')
    with open('names.txt') as f:
        for line in f:
            NAMES.append(line.strip())

    print('STARTING SERVER...')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('0.0.0.0', PORT))
    serversocket.listen(5)
    print('SERVER STARTED')

    while True:
        con, addr = serversocket.accept()
        print('CONNECTION FROM:', addr)
        threading.Thread(target=client, args=(con, addr)).start()
