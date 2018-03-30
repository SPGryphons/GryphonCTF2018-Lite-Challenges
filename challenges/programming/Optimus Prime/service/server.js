#!/usr/bin/env node

const HOST = '0.0.0.0';
const PORT = 5001;

const net = require('net');
const server = net.createServer().listen(PORT, HOST);

const fs = require('fs');
let banner;
fs.readFile('banner.txt', {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        banner = data;
    } else {
        console.log(err);
    }
});
var numbers = require('./data.json');

function pickRandomProperty(obj) {
    var result;
    var count = 0;
    for (var prop in obj)
        if (Math.random() < 1/++count)
           result = prop;
    return result;
}

server.on('connection', sock => {
    sock.setEncoding('utf8');
    sock.setTimeout(3000); // 3 seconds timeout
    sock.write(banner);
    let level = 1;
    let num = pickRandomProperty(numbers);
    sock.write('Level ' + level.toString() + '\n' + num.toString() + '\n>');
    sock.on('data', data => {
        let reply = data.toString('utf8').replace(/\r?\n$/, '');
        if (reply === 'false' && numbers[num]) {
            sock.write(num.toString() + ' is prime!\n');
            sock.destroy();
            return;
        } else if (reply === 'true' && !numbers[num]) {
            sock.write(num.toString() + ' is not prime!\n');
            sock.destroy();
            return;
        } else if (reply !== 'true' && reply !== 'false') {
            sock.write('Invalid response!\n');
            sock.destroy();
            return;
        }
        level += 1;
        if (level === 101) { // Players have to solve 100 levels to get the flag.
            sock.write('Optimus Prime is satisfied, here is your flag GCTF{flag}\n');
            sock.destroy();
            return;
        }
        num = pickRandomProperty(numbers);
        sock.write('Level ' + level.toString() + '\n' + num.toString() + '\n> ');
    });
    sock.on('timeout', () => {
        sock.destroy();
    });
});

console.log('Server listening on ' + HOST + ':' + PORT);
