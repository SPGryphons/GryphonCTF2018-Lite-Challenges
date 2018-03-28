# Disallowed

## Question Text

I set up my website so that robots can't steal away my flag!

Created by PotatoDrug

## Setup Guide
Run `./build.sh`

## Solution
The name of the file containing the flag is in robots.txt, browse to it to get the flag.

```
User-agent: * 
Disallow: /f4ce14af2704da2ff9e5c0b059b683b4bfd3ee00.txt
```

**Flag:** GCTF{r0b0ts\_4r5\_n0\_m4tch\_4\_me}
