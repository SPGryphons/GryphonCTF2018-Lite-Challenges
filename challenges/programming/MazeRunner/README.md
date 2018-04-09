# Maze Runner

## Question Text
Can you get out of this madness? Find your way out and get the flag!

`nc pwn.chal.gryphonctf.com 18174`

*Created - Noans*

## Setup Guide
1. Run `build.sh` in `service` folder.

## Solution
Make a program to find the way out of the maze.  
The python program is in `solution` folder.

The algorithm in the solution is as such:
1. Find the starting position of the player.
2. Start by surveying blocks north, east, south and west of current position of player.
3. Find block that is that is a path and "move" to the block
4. Once on next block, start surveying blocks based on move made:   
    If the player moves up, the next blocks to be surveyed is the block north, east and west of the player; if the player moves left, the next blocks to be surveyed are north, south and west of the player.
5. Move to block that is a path and continue survey.
6. Finish once exit of maze is found.

The algorithm tracks all moves made and sends them to the server for each maze received.

### Flag
`GCTF{H3h_I'M_S4F3}`