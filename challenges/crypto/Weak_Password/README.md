# Weak_Password

## Question Text

We intercepted this encrypted zip file from our target, he is known to use weak passwords, can you crack it for us?

*Creator - PotatoDrug*

### Hint

1. rockyou.txt probably has the password
2. I head fcrackzip is a useful tool for cracking zip files

## Setup Guide
1. Put flag.txt into a encrypted zip file with a password from rockyou.txt

## Distribution

weakpassword.zip - encrypted zip file 


## Solution
Use a tool like fcrackzip and do a wordlist attack using a common wordlist such as rockyou.txt

`fcrackzip -D -p rockyou.txt -u weakpassword.zip`

Output should be

```
PASSWORD FOUND!!!!: pw == luckyyou
```

### Flag

`GCTF{n3v3r_u5e_we4k_p4ssw0rd5}`