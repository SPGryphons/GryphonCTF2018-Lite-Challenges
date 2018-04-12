# Git Good

## Question Text

Challenge description and how to play (if applicable).

This is another paragraph.

*Creator - PotatoDrug*

## Distribution
- Git Good.zip
    - SHA1: `b2d1abd39c53bde4619a865a14e744e14aab18cd`
    - zip file containing local git repo

## Solution
The flag is in the previous commit of the git repo so `git log` to view the previous commits

```
commit b50f51476ec50b6629bfb2a7948fc196e8adfe59
Author: PotatoDrug <zhy.david@gmail.com>
Date:   Thu Apr 12 11:53:55 2018 +0800

    Added flag.jpg

commit bd4ae22d2783cd96893270e2dfd134d2418368df
Author: PotatoDrug <zhy.david@gmail.com>
Date:   Thu Apr 12 11:52:20 2018 +0800

    Inital commit
```

`git checkout bd4ae22d2783cd96893270e2dfd134d2418368df` to view repo at the initial commit and you can do a `cat flag.txt` to get the flag.

### Flag
`GCTF{917_1S_SuPER_uSeFUl_so_rmb_7o_uSE_17}`

## Recommended Reads
* https://try.github.io
