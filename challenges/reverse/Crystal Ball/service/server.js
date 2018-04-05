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
    function random(s) {
        let x = Math.sin(s) * 10000;
        return Math.floor((x - Math.floor(x)) * 10000000000);
    }
    sock.setEncoding('utf8');
    sock.setTimeout(30000); // 30 seconds timeout
    sock.write(banner);
    sock.on('data', data => {
        let date = new Date();
        let seed = date.getHours() + date.getMinutes();
        if (seed === 0) {seed = 1}
        var recieved = parseInt(data.toString('utf8').replace(/\r?\n$/, ''));
        if (recieved === random(seed)) {
            sock.write('GCTF{PreD1C71ng_7HE_fU7URE_W17h_My_7rU57Y_crY574l84ll}');
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
