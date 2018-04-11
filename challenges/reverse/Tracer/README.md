# Tracer

## Question Text

Help Tracer recover her flag!

*Creator - PotatoDrug*

### Hints
1. Can Tracer trace library calls?

## Distribution
- tracer
    - SHA1: `ef86d0d10c9b55f59b97a9b92dd6d641e0cd5e8c`
    - ELF 64-bit LSB executable

## Solution
If we do a `objdump -d tracer` at the Global Offset Table we can see strcmp is used.

```
0000000000400590 <strcmp@plt>:
  400590:       ff 25 aa 0a 20 00       jmpq   *0x200aaa(%rip)        # 601040 <_GLOBAL
_OFFSET_TABLE_+0x40>
  400596:       68 05 00 00 00          pushq  $0x5
  40059b:       e9 90 ff ff ff          jmpq   400530 <_init+0x20>
```

We use `ltrace` to get the flag by running `ltrace ./tracer` to intercept and print the library calls of the program and get the flag from there.

```
__libc_start_main(0x4006a6, 1, 0x7fffebd61588, 0x400860 <unfinished ...>
printf("Someone recover our flag!\n> "Someone recover our flag!
)              = 28
fgets(> a
"a\n", 29, 0x7fc8fa1f48e0)                     = 0x7fffebd613f0
strcmp("a\n", "GCTF{r3v3R5IN9_i5_C4nc3R0Uz}")        = 26
puts("That's not my flag :("That's not my flag :(
)                        = 22
+++ exited (status 0) +++
```

### Flag
`GCTF{r3v3R5IN9_i5_C4nc3R0Uz}`
