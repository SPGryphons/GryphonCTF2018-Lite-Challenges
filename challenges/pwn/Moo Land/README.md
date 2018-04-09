# Moo Land

## Question Text

I found some talking cows!

`nc pwn.chal.gryphonctf.com 18151 `

*Creator - PotatoDrug*

## Setup Guide
Run `./build.sh`

## Solution
There is no input sanitization at all so you can execute whatever commands you want by using a semicolon.

`hi;ls` will show you flag.txt, `hi;cat flag.txt` will give you the flag.

### Flag

`GCTF{wh4t_d0es_the_c0w_s4y}`