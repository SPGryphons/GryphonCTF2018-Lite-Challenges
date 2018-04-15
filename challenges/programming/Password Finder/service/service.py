#!/usr/bin/env python3
import socket
import threading
import random

PASSWORD_COUNT = 50
PORT_NUMBER = 12345 
TIMEOUT = 120

FLAG = "GCTF{1_st0l3_th3_l15t}"

wordList = []

def getPassword():
    with open("results.txt", "r") as file1:
        for line in file1:
            wordList.append(line[:-1]) 
            #[:-1] excludes newline char
    
def userInput(conn,tm=TIMEOUT):
    try:
        conn.settimeout(tm)
        answer = conn.recv(8192).decode()
        return answer
    except:
        conn.sendall('\nTimeout.\n'.encode())
        conn.close()
        exit()
        
def service(conn,addr):
    try:
        usedWordList = []
        conn.sendall("pls gif 50 passwords, newline character delimited.\n".encode())
        counter = 0
        while counter < PASSWORD_COUNT:
            answer = userInput(conn)
            passList = answer.split("\n")
            for i in passList:
                if i in wordList and i not in usedWordList:
                    counter=counter+1
                    usedWordList.append(i) 
            conn.sendall(("You currently have "+str(counter)+" valid passwords\n").encode())
        conn.sendall(("\n\n\nGreat Job! Flag: "+FLAG+"\n").encode())
        conn.close()
    except socket.error:
	    print('Client may have closed connection.')
	    conn.close()
    except Exception as e:
        print("???"+e)
        conn.close()

def main():
    serverSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    getPassword()
    
    try:
        serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSock.bind(('0.0.0.0', PORT_NUMBER))
        serverSock.listen(5)
        print('Socket listening on port',PORT_NUMBER)
        while True:
                sessionSock = serverSock.accept()
                t = threading.Thread(target=service,args=sessionSock)
                t.start()
                
    except KeyboardInterrupt:
        print('\nShutting down...')
    except socket.error:
	    print('Socket error')
    except Exception as e:
        print('Some error:\n'+e)
        
    finally:
        serverSock.close()
        
if __name__ == "__main__":
    main()
