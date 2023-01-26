# ProjetoDeRedes
Projeto de Redes sobre os conceitos UDP, TCP e xFTP

xFTP Transfer File Service
(TPC1 – Redes de Computadores)

1.	Introduction
The objective of this TPC is to implement the client and server programs of a File Transfer Service. In short, this service will use a TCP connection to allow the client to send commands to the server, while file data is transferred using UDP, block by block.
Fig. 1 illustrates the interaction between a client and the server.
1.	The client connects to the server using a pre-defined TCP port (TTTP). At any given time, the server only interacts with a single client;
2.	A command shell allows the user to give the following commands:
a.	Obtain the contents of the directory where the server stores files. The user command is DIR;
b.	To transfer a file in the client file system to the server´s file system. The user command is PUT filename. The file has the same name in both file systems;
c.	To transfer a file in the server file system to the client's file system. The user command is GET filename. The file has the same name in both file systems;
d.	To finish the interaction between the client and the server. The user command is the string QUIT.
3.	After the QUIT command, the client exits and the server proceeds to handle the next client.


Fig. 1: Client/ Server interaction
 

The synopsis of the client command is:
client hostname port
The synopsis of the server command is:
server TCP_Port UDP_Port



2.	Command operation description
In the following a description of the operation of the 4 commands is given.
DIR command

 

GET command
 
Fig. 2: DIR command
 

 

Fig. 3: GET command
 
PUT command


Fig. 4: PUT Command


QUIT command
This command sends to the server, through the TCP connection the string “QUIT”. The client closes its TCP socket and quits. The server prepares to handle a new client, by calling accept().


