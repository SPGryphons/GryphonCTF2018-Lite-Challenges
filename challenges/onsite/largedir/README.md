# largedir

## Question Text
I lost the flag in the large dir. Please help me find it.

`cd ~/largedir`

*Creator - @Inifinitide*

## Setup Guide
Run the script in the [generate](../generate) directory for onsite challenges

## Solution
This challenge will require the challenge [`Save My Cat`](../Save\ My\ Cat) and [`Secure Shell`](../Secure\ Shell) to be completed

Since players are running from a rbash environment, the most efficient way is to use the `find` command.
Using the command, `find ~/largedir -type f`, players will be able to see where the file is located.
Now all that needs to be done is to cat the file found.

A simple way to do this in one command is `cat $(find ~/largedir -type f)`

### Flag
GCTF{f1nd_is_m0r3_us3fu1_th4n_gr3p}

## Recommended Reads
* https://www.binarytides.com/linux-find-command-examples/
