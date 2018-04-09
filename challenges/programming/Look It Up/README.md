# Look It Up

## Question Text
Each person has their own integer range and I would like to know who owns which integer.

You have to answer 100 queries for me **within 1 second each**, however the list will change every 10 queries.

When you first enter the program, the first line will be the number of names, _N_.  
Followed by _N_ lines of comma-separated values, _X_, _Y_, and _Z_, being start of range (inclusive), end of range (inclusive) and name respectively.  
Then a number, _Q_, will appear. This is when you key in the name that owns the number _Q_.  
When you get the query right, a new _Q_ will appear again and you would have to answer it 9 more times.  
_N_ will appear again after 10 successful queries, requiring you to refresh your list.  
Answering it wrongly or too slowly and the connection will close.  

**Note**: The names used may be repeated in each list.

`prog.chal.gryphonctf.com:18173`

**Sample Input:**
```
13
0,4,ESSIX
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
97,108,MASIEJCZYK
40:
```

**Sample Output:**
```
PAMPERIN
```

*Creator - Deathline75*

## Setup Guide
Do `sudo bash build.sh`

## Solution
Fastest way I found was to use binary search to find the answer in O(log N) time. Do not print out the table data as it will cause your program to time out.

Example solution is in solutions folder.

### Flag
`GCTF{71m3_c0mpl3x17y_w0n7_570p_m3}`


