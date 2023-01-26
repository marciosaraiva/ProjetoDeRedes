from socket import *
import time
SSIZE = 2048
CHUNK = 512
msgQUIT = "QUIT"
msgDIR = "DIR"
msgGET = "GET"
msgPUT = "PUT"
msgACK = "ACK"
msgOK = "OK"
serverName = "localhost"            # server name
serverPort = 18000                  # socket server port number

def dir_command(clientSocket):
    print("Execute command DIR") # debug print
    
    clientSocket.send(msgDIR.encode())  

    while True:
        returnMessage = clientSocket.recv(2048).decode()  # receive response
               
        if "fim" in returnMessage:
            break # send user's sentence
        else:
            print("recebeu", returnMessage, "\n")
    

def get_command(clientSocket, fname):
    
    print("Execute command GET file:", fname ) # debug print
    
    clientSocket.send((msgGET+";"+fname).encode()) 
    
    while True:
        returnMessage = clientSocket.recv(2048).decode()  # receive response
        
        print("recebeu", returnMessage, "\n")
        
        if msgOK in returnMessage:
            with open(fname,'r') as file: # open the fileserver 
                conteudo = file.read()
                print(conteudo, "\n")
            break
                
        else:
            print("Arquivo nao encontrado\n")
            break
  
    
def put_command(clientSocket, fname, fcontent):
    print("Execute command PUT file:", fname ) # debug print
    
    clientSocket.send((msgGET+";"+fname).encode()) 
    
    while True:
        returnMessage = clientSocket.recv(2048).decode()  # receive response
        
        print("recebeu", returnMessage, "\n")
        
        if msgOK in returnMessage:
            with open(fname,'a+') as file: # open the fileserver 
                file.write("\n"+fcontent)
            break
                
        else:
            print("Arquivo nao encontrado\n")
            break

def quit_command(clientSocket):
    print("Execute command QUIT") # debug print
    
    clientSocket.send(msgQUIT.encode())
    time.sleep(2)
    clientSocket.close()

def main(args):
    
    """
    if (len(args) > 2):
        serverName = args[1]
        serverPort1 = int(args[2])
    else:
        print("Invalid arguments main")
        sys.exit(1)
    """
    
    while True:
        # create TCP socket
        clientSocket = socket(AF_INET,SOCK_STREAM)
        # open TCP connection
        clientSocket.connect(("localhost", serverPort))
        
        line = input("> ")
        cmdLine = line.split()
        cmd = cmdLine[0]
        cmd = cmd.upper()
        nargs = len(cmdLine)    
    
        if cmd == "DIR":
            if nargs != 1:
                print("Invalid arguments")
            else:
                dir_command(clientSocket)            

        elif cmd == "GET":
            if nargs != 2:
                print("Invalid arguments")
            else:
                filename = cmdLine[1]
                get_command(clientSocket,filename)
            
            
        elif cmd == "PUT":
            if nargs != 3:
                print("Invalid arguments")
            else:
                filename = cmdLine[1]
                filecontent = cmdLine[2]
                put_command(clientSocket, filename, filecontent)
 
        elif cmd == "QUIT":
            print("enviou a facada")
            clientSocket.send(msgQUIT.encode())
            break

        else:
            print("Command not found")
  
        #clientSocket.close()
        #print("Client shutting down")
        
    return 0

if __name__ == '__main__':
    import sys
    from socket import *
    sys.exit(main(sys.argv))
