# Liars

## Question Text

There has been some liars sneaking through my program can you catch 3 of them for me?

`nc pwn.chal.gryphonctf.com 18154`

*Creator - PotatoDrug*

### Hints
1. Liar numbers?

## Setup Guide

Run `./build.sh`

## Distribution
- liars.js `69bc64163f45250e1f4d9ec7465490d6`
    - Redacted source code for the service

## Solution
```javascript
function a(num) {
    if (num === 1) { return false; }
    for (var i=2; i < 11; i++) {
        x = new BigNumber(i);
        if (x.exponentiatedBy(num).minus(i).mod(num).isEqualTo(0) !== true) {
            return false;
        }
    }
    return true;
}
```

Function a is **Fermat primality test** which has false positives when a Carmichael number is passed in.

```javascript
function b(num) {
    if (num === 2) { return true; }
    if (num % 2 === 0) { return false; }
    for(let i = 3, s = Math.sqrt(num); i <= s; i += 2) {
        if (num % i === 0) { return false; }
    }
    return num !== 1;
}
```

Function b is just a standard test for prime numbers.

So to get the flag we have to send 3 different Carmichael numbers within the range of 0 and 50000 to the service, the lowest 3 are `561, 1105, 1729`.

### Flag
`GCTF{L14R_l14R_p4N75_0N_f1r3}`

## Recommended Reads
* https://www.youtube.com/watch?v=jbiaz_aHHUQ
* https://en.wikipedia.org/wiki/Carmichael_number
* https://en.wikipedia.org/wiki/Fermat_primality_test
