# Crystal Ball

## Question Text

I found this crystal ball, I believe I can predict the future now muhahaha.

The redacted source code of the service running is given to you, you have to figure out what to send to the service to get the flag.

`nc rev.chal.gryphonctf.com 18211`

*Creator - PotatoDrug*

## Setup Guide
Run `./build.sh`

## Distribution
- crystallball.js  
  - SHA1: `887f2306427e7b521206e5b35df73fb3837b712d`
  - source code for the service of this challenge

## Solution
Let us go through the code required to solve this challenge.

```javascript
function a(y) {
    let x = Math.sin(y) * 10000;
    return Math.floor((x - Math.floor(x)) * 10000000000);
}
```

What this function does is takes in parameter y and does all the math operations on it. 

`*` basically means multiply, `Math.sin` returns the sine of the given number in radians which you should have learned in secondary school.

```javascript
Math.floor( 45.95); //  45
Math.floor( 45.05); //  45
Math.floor(  4   ); //   4
Math.floor(-45.05); // -46 
Math.floor(-45.95); // -46
```

What `Math.floor()` does is it returns the largest integer less than or equal to the given value.

```javascript
ntpClient.getNetworkTime("pool.ntp.org", 123, (err, date) => {
    if(err) {
        console.error(err);
        return;
    }
    let b = JSON.stringify(date).match(/T\d\d:\d\d/)[0].substring(1).split(':').map(Number).reduce((a, b) => a + b, 0);
```

This code is connecting to a NTP server on port 123 and setting b to the sum of the hour and minute from the NTP server. One thing to note is NTP servers always respond with UTC time.

Using 35 as the value of b.

```
sin35 x 10000 = -4281.82669496151               (Math.sin(y) * 10000)
floor of -4281.82669496151 = -4281
-4281.82669496151 - -4281 = 0.82669496151       ((x - Math.floor(x))
0.82669496151 x 10000000000 = 8266949615.1      ((x - Math.floor(x)) * 10000000000)
floor of 8266949615.1 = 8266949615              (Math.floor((x - Math.floor(x)) * 10000000000))
```

So if 35 was given to function a, it will return 8266949615.

```javascript
if (recieved === a(b)) {
    sock.write('GCTF{flag}'); // redacted flag
    sock.destroy();
}
```

What this part does is it compares if what you sent is equal to the return value of function a. Since we know the operations function a does and we also know what the value of b will be, we can calculate the value required to get the flag and send it to the server. The rest of the code is handling the connections and stuff so you can just ignore them.

Sample solution script in solution folder. You can use a calculator to solve it too.

### Flag

`GCTF{PreD1C71ng_7HE_fU7URE_W17h_My_7rU57Y_crY574l84ll}`