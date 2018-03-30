#!/usr/bin/env node

function primeNumber (n) {
    if (n === 2) return true // 2 is a special case
    if (n % 2 === 0) return false
    for (var i = 3; i <= Math.sqrt(n); i = i + 2) {
        if (!primeNumber(i)) continue // <-- recursion here
        if (n % i === 0) return false
    }
    return true
}

function pickRandomProperty(obj) {
    var result;
    var count = 0;
    for (var prop in obj)
        if (Math.random() < 1/++count)
           result = prop;
    return result;
}

let high = 1000000000;
let low = 2;
let num;
let answer;
let numbers = {2:true};
let count = 1;

while (count < 5000) {
    num = Math.floor(Math.random() * (high - low) + low);
    if (primeNumber(num)) {
        numbers[num] = true;
        count++;
    }
}
count = 0;
while (count < 5000) {
    num = Math.floor(Math.random() * (high - low) + low);
    if (!primeNumber(num)) {
        numbers[num] = false;
        count++;
    }
}

let fs = require('fs');
fs.writeFile('data.json',JSON.stringify(numbers),function(err){
    if(err) throw err;
    console.log('JSON Object written to data.json');
})

// console.log(numbers);
console.log(Object.keys(numbers).length);