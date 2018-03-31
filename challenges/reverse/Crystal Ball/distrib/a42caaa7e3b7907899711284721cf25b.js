#!/usr/bin/env node

const HOST = '0.0.0.0';
const PORT = 5002;

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

server.on('connection', sock => {
    function a(y) {
        let x = Math.sin(y) * 10000;
        return Math.floor((x - Math.floor(x)) * 10000000000);
    }
    sock.setEncoding('utf8');
    sock.setTimeout(30000);
    sock.write(banner);
    sock.on('data', data => {
        let date = new Date();
        let b = date.getHours() + date.getMinutes();
        if (b === 0) {b = 1}
        var recieved = parseInt(data.toString('utf8').replace(/\r?\n$/, ''));
        if (recieved === a(b)) {
            sock.write('GCTF{flag}'); // redacted flag
            sock.destroy();
        } else {
            sock.write('Wrong!');
            sock.destroy();
        }
    });
    sock.on('timeout', () => {
        sock.write('sockect timeout\n');
        sock.destroy();
    });
});

console.log('Server listening on ' + HOST + ':' + PORT);
