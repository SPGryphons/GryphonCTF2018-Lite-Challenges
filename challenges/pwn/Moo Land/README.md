# Moo Land

## Question Text

I found some talking cows!

`nc <server> <port> `

Created by PotatoDrug

## Setup Guide
Run `./build.sh`

## Solution
There is no input sanitization at all so you can execute whatever commands you want by using a semicolon.

`hi;ls` will show you flag.txt, `hi;cat flag.txt` will give you the flag.

**Flag:** GCTF{wh4t\_d0es\_the\_c0w\_s4y}