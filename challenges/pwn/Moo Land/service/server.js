#!/usr/bin/env nodejs

const HOST = '0.0.0.0';
const PORT = 5000;

var net = require('net');
var server = net.createServer().listen(PORT, HOST);

var fs = require('fs');
var banner;
fs.readFile('banner.txt', {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        banner = data;
    } else {
        console.log(err);
    }
});
var exec = require('child_process').exec;

server.on('connection', sock => {
    // console.log('CONNECTED: ' + sock.remoteAddress + ':' + sock.remotePort);
    sock.setEncoding('utf8');
    sock.write(banner);
    sock.on('data', data => {
        var recieved = data.toString('utf8').replace(/\r?\n$/, '');
        if (recieved === 'exit') {
            sock.destroy();
        } else {
            exec('cowsay ' + recieved, (error, stdout, stderr) => {
                sock.write(stdout + '\n> ');
            });
        }
    });
});

console.log('Server listening on ' + HOST + ':' + PORT);