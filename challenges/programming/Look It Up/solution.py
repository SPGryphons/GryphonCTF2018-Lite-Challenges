#!/usr/bin/env python3
import socket

def recvuntil(s, target):
    buf = ''
    output = ''
    while buf != target:
        buf = s.recv(1).decode('UTF-8')
        if buf == '':
            return output
        output += buf
    return output

def parse(recieved):
    tmp = [x.split(',') for x in recieved.split('\n')[1:]]
    target = int(tmp.pop()[0][:-1])
    l = []
    for line in tmp:
        l.append((range(int(line[0]), int(line[1])+1), line[2]))
    return (l, target)

def compareRange(r, t):
    if t in r:
        return 0
    elif t < r[0]:
        return 1
    else:
        return 2

def interpolation_search(sorted_list, to_find):
    low = 0
    high = len(sorted_list) - 1

    print(sorted_list[low][0][0])
    while sorted_list[0][low] <= to_find and sorted_list[0][high] >= to_find:
        mid = int(low + ((to_find - sorted_list[0][low]) * (high - low))
               / (sorted_list[0][high] - sorted_list[0][low]))
              # out of range is possible
        if sorted_list[0][mid] < to_find:
            low = mid + 1
        elif sorted_list[0][mid] < to_find:
            high = mid - 1
        else:
            return mid
    if sorted_list[0][low] == to_find:
        return low
    return None

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

def main():
    server = "127.0.0.1"
    port = 18173

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to {}:{}...".format(server, port))

    s.connect((server, port))
    for i in range(10):
        p = recvuntil(s, ':')
        tmp = parse(p)
        print('Outer: {}'.format(i))
        s.sendall(interpolation_search(tmp[0], tmp[1]).encode())
        for i in range(9):
            print('Inner: {}'.format(i+2))
            s.sendall(interpolation_search(tmp[0], int(recvuntil(s, ':')[:-1])).encode())

if __name__ == '__main__':
    main()
