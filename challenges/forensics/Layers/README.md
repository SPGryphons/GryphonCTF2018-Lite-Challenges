# Layers

## Question Text

I have hidden and encrypted my flag! Surely nothing can go wrong now.

Created by PotatoDrug

## Setup Guide
1. Put flag.txt into a encrypted 7z
2. Append the password to the png
3. Append the encrypted 7z archive to the png

## Distribution
layers.png `SHA1: ddf7cf371dfe58b9225492b788eb38ab21d2b33b` 

## Solution
Extract the 7z file with binwalk using `binwalk --dd=".*" layers.png` as stated [here](https://stackoverflow.com/questions/37904544/binwalk-not-extracting-files-from-binary) because `binwalk -e layers.png` doesnt work or you can just do it manually.

Use strings to find 7z password (ezpzpassword)

Flag: GCTF{tbh_i_am_a_forensics_n00b}

## Recommended Reads
* https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_format
* https://en.wikipedia.org/wiki/List_of_file_signatures
