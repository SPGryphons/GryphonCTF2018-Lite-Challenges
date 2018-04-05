# Disallowed

## Question Text

I set up my website so that robots can't steal away my flag!

`http://web.chal.gryphonctf.com:18132`

*Creator - PotatoDrug*

## Setup Guide
Run `./build.sh`

## Solution
The name of the file containing the flag is in robots.txt, browse to it to get the flag.

```
User-agent: * 
Disallow: /f4ce14af2704da2ff9e5c0b059b683b4bfd3ee00.txt
```

### Flag

`GCTF{r0b0ts_4r5_n0_m4tch_4_me}`