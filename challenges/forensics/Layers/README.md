# Layers

## Question Text

I have hidden and encrypted my flag! Surely nothing can go wrong now.

*Creator - PotatoDrug*

### Hint

1. https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_format
2. You should probably open the file in a hex editor.

## Setup Guide
1. Put flag.txt into a encrypted 7z
2. Append the password to the png
3. Append the encrypted 7z archive to the png

## Distribution
- layers.png
  - SHA1: `c3be2f9763a7f3ab90bb2c628a17f576` 
  - PNG file containing hidden data

## Solution
First you have to realize there is additional data in the png file, png files use `IEND`  to mark the image end, so you can append additional data after `IEND` and it will not affect how the image looks. Open the image in a hexeditor and you will realize there is additional data after `IEND`.

The first piece of data is `Password: ezpzpassword` which will be useful later on.

Next we see some unreadable data, we can use a tool such as binwalk with `binwalk --dd=".*" layers.png` as stated [here](https://stackoverflow.com/questions/37904544/binwalk-not-extracting-files-from-binary) because `binwalk -e layers.png` doesn't work, to extract it out. It will tell us that it has found a 7z file.

The 7z zip is encrypted but we can use the password we found earlier to decrypt it and get the flag.

 You can also extract the 7z file manually by copying out the data that starts from the 7z file header which starts with `37 7A BC AF 27 1C`.

### Flag

`GCTF{tbh_i_am_a_forensics_n00b}`