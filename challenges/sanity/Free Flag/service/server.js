#!/usr/bin/env node

const HOST = '0.0.0.0';
const PORT = 5003;

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
    sock.setEncoding('utf8');
    sock.write(banner);
    sock.destroy();
});

console.log('Server listening on ' + HOST + ':' + PORT);
