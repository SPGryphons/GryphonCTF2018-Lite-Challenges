# Obfuscation

## Question Text

I found this website that checks if a flag is valid!

`http://web.chal.gryphonctf.com:18133`

*Creator - PotatoDrug*

## Hints

1. https://en.wikipedia.org/wiki/Esoteric_programming_language

## Setup Guide

Run `./build.sh`

## Solution

View source and find script.js

Open script.js and you will find obfuscated javascript using jsfuck, decode it using any jsfuck decoder and you will see the source code containing the flag.

### Flag

`GCTF{an_e4sy_obfusc4ti0n}`