from socket import *
import sys
from getDirFiles import get_dir_files
import time

msgOK = "OK"
msgERROR = "ERROR"

serverName = "localhost"
serverPort = 26000

serverSocket = socket(AF_INET,SOCK_STREAM)   # create xFTP welcoming socket
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print("Server is running")

def main(args):
    while True:
        connSocket, addr = serverSocket.accept()    # waits for incoming requests:
                                                    # new socket created on return
        print("Connected by: ", str(addr))

        sentence = connSocket.recv(2048).decode()    # read a sentence of bytes
                                                     # received from client
            
        sentences = sentence.split(";")

        print("Data from connected user: ", sentence) # display received sentence

        if "DIR" in sentences[0]:
            #receives the DIR
            address = os.getcwd()+"\\teste"
            
            list_files = get_dir_files(address)
            
            for file in list_files:
                address_file = address+"\\"+file
                connSocket.send(address_file.encode())
                print("enviou", address_file)
                time.sleep(1)
            else:
                connSocket.send("fim".encode())
                       
        elif "GET" in sentences[0]:
     
            try:
                arquivo = open(sentences[1], 'r')
                connSocket.send(msgOK.encode())  
            except: 
                connSocket.send(msgERROR.encode())  
                
        elif "QUIT" in sentences[0]:
            pass

            
if __name__ == '__main__':
    import sys
    from socket import *
    import socket
    import os
    sys.exit(main(sys.argv))