# Look It Up

## Question Text
Each person has their own integer range and I would like to know who owns which integer.

You have to answer 100 queries for me **within 1 second each**, however the list will change every 10 queries.

The first line given will be the number of names in this list, _`N`_.  
Followed by _`N`_ lines of comma-separated values, _`X`_, _`Y`_, and _`Z`_ being start of range (inclusive), end of range (inclusive) and name of the person respectively.  
The subsequent 10 lines are integers, _`Q`_, that require you to translate _`Q`_ to the name _`Z`_.  
After 10 queries are answered, the whole process will repeat 9 extra times, starting with the integer _`N`_.  
Answering it wrongly or too slowly and the connection will close.  

**Note**: The names used may be repeated in each list.

`prog.chal.gryphonctf.com:18173`

**Input from Server (The arrows do not appear when you connect):**
```
13  <----- N
0,4,ESSIX  <------- X,Y,Z
5,12,NEUMEYER
13,26,OBERLOH
27,31,POYDRAS
32,38,LIONTOS
39,43,PAMPERIN
44,53,ARMIGER
54,58,SAPARA
59,67,KRAIG
68,78,VARNADOE
79,86,SHVEY
87,96,DEDIOS
97,108,ARMIGER
40:   <------- Q
13: 
41: 
... (Repeat 7 more times)
```

**Your Answer:**
```
PAMPERIN
OBERLOH
PAMPERIN
...
```

*Creator - Deathline75*

## Setup Guide
Do `sudo bash build.sh`

## Solution
Fastest way I found was to use binary search to find the answer in O(log N) time. Do not print out the table data as it will cause your program to time out.

Example solution is in solutions folder.

### Flag
`GCTF{71m3_c0mpl3x17y_w0n7_570p_m3}`


