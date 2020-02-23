import threading
import time
import random
import sys
import socket

def client():
    try:
        #socket for client to connect to rs to search for hostname,ip,flag
        rs_clientsocket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM) 
        
        #socket for client to connect to ts if hostname isn't in rs
        #ts_clientsocket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)  
    except socket.error as err:
        print("socket open error: {} \n".format(err))
        exit()

    rsHostname = sys.argv[1]
    rsListenPort = sys.argv[2]
    tsListenPort = sys.argv[3]

    # get root server's ip
    # rsHostname is given as argument1 in command line
    rsHostip = socket.gethostbyname(rsHostname)
    # client connects to rs host machine
    rootServerBinding = (rsHostname, rsHostip)
    # connect to root server 
    rs_clientsocket.connect(rootServerBinding)
    # send message to server
    with open("PROJI-HNS.txt", "r") as f:
        for line in f:
            s.sendall(line.encode())
   """
    # get top server's hostname
    tsHostname = socket.gethostname()
    # get top server's ip
   tsHostip = socket.gethostbyname(tsHostname)
   """

