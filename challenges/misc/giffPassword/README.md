# Password Finder

## Question text

I made a list of strong passwords to use for this shady website. However, someone mixed in weak passwords into my list!

Please help me find my strong passwords for me. They consist of:

- They contain alphanumeric characters. `123abc...`
- The password contains both uppercase and lowercase letters `aAbB...`
- They contain special characters `(!@#$%^...)`
- They are at least more than 15 characters long.
- They are up to 20 characters long, because the website requesting for my password has a length limit :(
- They don't consist of spaces. 

Enter my passwords with `nc` at ?????? (to be updated?)

*Creator - @IncompententDev*

### Hints
1. Regex, lookahead!

## Setup Guide
1. Build docker image: `./build.sh` in service
2. Run docker image: `./run.sh` in service

## Distribution
- password.txt
    - SHA1: `b938e0a4f2bb6f2b028fc99b3f83398ee4743099`
    
## Solution

Lookaheads in regex do not consume characters. Hence, the regex just needs to search for the presence of the following category of characters, followed by strings that are between 15 to 20 characters long.

- Uppercase and lowercase letters: `(?=.*[A-Z](?=.*[a-z])`
- Numbers: `(?=.*\d)`
- Special characters: ``(?=.*[~!@#$%^&*_\-+=`|\(){}\[\]:;\"'<>,.?/])``
- 15 to 25 characters long: `.{15,20}`
- Exclude spaces: `(?!.*\ )`

The `.*` searches for any number of characters preceding the token of interest (eg upper case letter, lower case letter)

The combined regex would be: 

    ^(?!.*[\ ])(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[~!@#$%^&*_\-+=`|\(){}\[\]:;\"'<>,.?/]).{15,20}$

Working solution in `solution/regexr.py`, run using python 3. Make sure `password.txt` is in the same directory, results generated in `results.txt`.
