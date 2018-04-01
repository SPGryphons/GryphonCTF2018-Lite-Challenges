# HelloWorld2

## Question Text
This time I learnt Java, see whether you can find the things I hid inside my program
Use `java 9d86a4c0098fa72c35b824382cc8a380` to run the program 

### Hint
Same same but different

*Creator - Chuan Kai (@exetr)*

## Setup Guide
1. Run `javac HelloWorld2.java`

## Distribution
1. Distribute contents inside `distrib` folder

## Solution
1. Using a Java decompiler, such as [JD-GUI](http://jd.benow.ca/), the code can be decompiled
2. It can be seen that the flag is *obfuscated* so the user needs to use the charset and corresponding positions of the array to recover the flag
3. This can be done through adding a print statement and recompiling, alternatively users can also apply some elbow grease to get back the flag
### Flag
`GCTF{TH1S_0N3_V3RY_H4RD_T0_F1LL}`
