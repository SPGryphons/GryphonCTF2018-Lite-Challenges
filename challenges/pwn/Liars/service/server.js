#!/usr/bin/env node

const HOST = '0.0.0.0';
const PORT = 5001;

const net = require('net');
const server = net.createServer().listen(PORT, HOST);
const BigNumber = require('bignumber.js');
const fs = require('fs');
let banner;
fs.readFile('banner.txt', {encoding: 'utf-8'}, (err,data) => {
    if (!err) {
        banner = data;
    } else {
        console.log(err);
    }
});

function isPrime1(num) {
    if (num === 1) { return false; }
    for (var i=2; i < 11; i++) {
        x = new BigNumber(i);
        if (x.exponentiatedBy(num).minus(i).mod(num).isEqualTo(0) !== true) {
            return false;
        }
    }
    return true;
}

function isPrime2(num) {
    if (num === 2) { return true; }
    if (num % 2 === 0) { return false; }
    for(let i = 3, s = Math.sqrt(num); i <= s; i += 2) {
        if (num % i === 0) { return false; }
    }
    return num !== 1;
}

server.on('connection', sock => {
    sock.setEncoding('utf8');
    sock.setTimeout(30000); // 30 seconds timeout
    sock.write(banner);
    let level = 0;
    let previous = [];
    sock.on('data', data => {
        let recieved = parseInt(data.toString('utf8').replace(/\r?\n$/, ''), 10);
        if (recieved >= 50000 || recieved <= 0 || isNaN(recieved)) {
            sock.write('Invalid number!\n');
            sock.destroy();
            return;
        }
        level += 1;
        if (isPrime1(recieved) === true && isPrime2(recieved) === false && level === 3) {
            if (previous.includes(recieved)) {
                sock.write('You already caught this liar!\n');
                sock.destroy();
                return;
            }
            sock.write('Goodjob! Here is your reward. GCTF{L14R_l14R_p4N75_0N_f1r3}\n');
            sock.destroy();
            return;
        } else if (isPrime1(recieved) === true && isPrime2(recieved) === false) {
            if (previous.includes(recieved)) {
                sock.write('You already caught this liar!\n');
                sock.destroy();
                return;
            }
            sock.write('You caught ' + level.toString() + ' liar\n');
            previous.push(recieved);
        } else {
            sock.write('That is not a liar!\n');
            sock.destroy();
            return;
        }
        sock.write('> ');
    });
    sock.on('timeout', () => {
        sock.write('sockect timeout\n');
        sock.destroy();
    });
});

console.log('Server listening on ' + HOST + ':' + PORT);
