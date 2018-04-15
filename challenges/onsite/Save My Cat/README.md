# Save My Cat

## Question Text
I lost my cat! Help me find it please!!!

*Creator - PotatoDrug*

## Setup Guide
Run the script in the [generate](../generate) directory for onsite challenges

## Solution
This challenge will the challenge [`Secure Shell`](../Secure%20Shell) to be completed.

Players are supposed cat the file `flag`. However, if they try to display its contents using `cat flag`, `I have your cat flag` will be displayed instead.
This is because an alias for cat is set to `echo I have your cat`. 
So, to display the flag using the cat command, the player will need to remove the alias using `unalias cat`.

### Flag
`GCTF{jU57_5AY1n9_1_PR3F3r_D092}`

## Recommended Reads
* http://www.linfo.org/alias.html
