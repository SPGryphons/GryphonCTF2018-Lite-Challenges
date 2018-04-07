#!/usr/bin/env python2
import random

random.seed('Spam')
flag = 'lovely_wonderful_spammy_python'
dontskip = set()
charset = 'abcdefghijklmnopqrstuvwxyz_'
last_num = 0
for char in flag:
    for i in xrange(last_num, 1000000):
        tmp = random.randint(0,26)
        if charset[tmp] == char:
            dontskip.add(i)
            last_num = i + 1
            break
print(sorted(dontskip))
print(max(dontskip)+1)
