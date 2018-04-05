# Obfuscation 2

## Question Text

I brought my obfuscation skills to the next level!

`http://web.chal.gryphonctf.com:18134`

*Creator - PotatoDrug*

## Setup Guide
Run `./build.sh`

## Solution
This challenge requires knowledge of using developer tools to debug javascript. Recommended to solve using chrome, anti-debugging seems to freeze firefox.

The site should be downloaded locally for easier debugging.

The first step to solving this challenge is to prettify the code.

### Intended Solution

After that you will realize that the code is anti-debugging, so you have to find the code that is doing the anti-debugging and remove it. The code that is commented out below is the anti-debugging code.

```javascript
function _0x53371c(_0x15ac37) {
    function _0x5c3fce(_0x24cb85) {
        if (typeof _0x24cb85 === GCTF_0x51fa('0x12', 'D8t6')) {
            return function(_0x41a4a3) {}
            [GCTF_0x51fa('0x13', 's0sf')](GCTF_0x51fa('0x14', 'Eg!]'))[GCTF_0x51fa('0x15', 'a(#m')](GCTF_0x51fa('0x16', 'mOmk'));
        } else {
            if (('' + _0x24cb85 / _0x24cb85)[GCTF_0x51fa('0x17', 'KT66')] !== 0x1 || _0x24cb85 % 0x14 === 0x0) {
                // (function() {
                //     return !![];
                // }
                // [GCTF_0x51fa('0x18', 'o#lo')](GCTF_0x51fa('0x19', 'J5il') + GCTF_0x51fa('0x1a', 'CZkU'))[GCTF_0x51fa('0x1b', 'Co6h')](GCTF_0x51fa('0x1c', 'mOmk')));
            } else {
                // (function() {
                //     return ![];
                // }
                // [GCTF_0x51fa('0x18', 'o#lo')](GCTF_0x51fa('0x1d', '1Ljt') + GCTF_0x51fa('0x1e', 'phi@'))[GCTF_0x51fa('0x1f', '1Ljt')](GCTF_0x51fa('0x20', ']PE^')));
            }
        }
        _0x5c3fce(++_0x24cb85);
    }
    try {
        if (_0x15ac37) {
            return _0x5c3fce;
        } else {
            _0x5c3fce(0x0);
        }
    } catch (_0x53317d) {}
}
```

Then we look into the most interesting function called checkFlag(), which has an if statement to check if what you entered is the flag. We can then get the flag by entering `GCTF_0x51fa('0xa', 'K#8j')` in the console which will give us the flag.

```javascript
function checkFlag() {
    var _0x1b8069 = document[GCTF_0x51fa('0x7', 'J5il')](GCTF_0x51fa('0x8', 'N[t['));
    if (_0x1b8069[GCTF_0x51fa('0x9', 't!Gj')] === GCTF_0x51fa('0xa', 'K#8j')) {
        alert(GCTF_0x51fa('0xb', '16v4'));
    } else {
        alert(GCTF_0x51fa('0xc', ']PE^'));
    }
}
```

### Alternative Solution

The anti-debugging code doesn't run in chrome if when you first visit the page you do not have developer tools open. You can then open developer tools and the anti-debugging tool will not run, so you can skip the first part and get the flag directly  using `GCTF_0x51fa('0xa', 'K#8j')`. If you click on the submit button or refresh the page with developer tools open the anti-debugging code will work again.

### Flag

`GCTF{n0t_s0_s1mple_0bfusc4t10n}`

## Recommended Reads
* https://developers.google.com/web/tools/chrome-devtools/javascript/
