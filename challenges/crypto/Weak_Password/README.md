# Weak_Password

## Question Text

We intercepted this encrypted zip file from our target, he is known to use weak passwords, can you crack it for us?

Hint: rockyou.txt probably has it

Created by PotatoDrug

## Setup Guide
1. Put flag.txt into a encrypted zip file with a password from rockyou.txt

## Distribution

weakpassword.zip `SHA1: 8339623049f0d4cb9ae067b048be8967c50020fe`


## Solution
Use a tool like fcrackzip and do a wordlist attack using rockyou.txt

`fcrackzip -D -p rockyou.txt -u flag.zip`

Flag: GCTF{n3v3r_u5e_we4k_p4ssw0rd5}
