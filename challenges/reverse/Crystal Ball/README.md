# Crystal Ball

## Question Text

I found this crystal ball, I believe I can predict the future now muhahaha.

The redacted source code of the service running is given to you, you have to figure out what to send to the service to get the flag.

`nc <server> <port>`

Created by PotatoDrug

## Setup Guide
Run `./build.sh`

## Distribution
Distribute all the contents inside `distrib` folder to the users

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
let date = new Date();
let b = date.getHours() + date.getMinutes();
```

This is basically get the current hour in 24 hours format and adding it with current minute. For example if time now is 23:12 then b will be 35.

Using 35 as the value of b.

```
sin35 x 10000 = -4281.82669496151				(Math.sin(y) * 10000)
floor of -4281.82669496151 = -4281
-4281.82669496151 - -4281 = 0.82669496151		((x - Math.floor(x))
0.82669496151 x 10000000000 = 8266949615.1		((x - Math.floor(x)) * 10000000000)
floor of 8266949615.1 = 8266949615				(Math.floor((x - Math.floor(x)) * 10000000000))
```

So if 35 was given to function a, it will return 8266949615.

```javascript
if (recieved === a(b)) {
    sock.write('GCTF{flag}'); // redacted flag
    sock.destroy();
}
```

What this part does is it compares if what you sent is equal to the return value of function a. Since we know the operations function a does and we also know what the value of b will be, we can calculate the value required to get the flag and send it to the server. The reset of the code is handling the connections and stuff so you can just ignore them.

Sample solution script in solution folder. You can use a calculator to solve it too.

Flag: GCTF{PreD1C71ng\_7HE\_fU7URE\_W17h\_My\_7rU57Y\_crY574l84ll}