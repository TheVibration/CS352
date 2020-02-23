import threading
import time
import random
import sys
import socket

rsHostname = sys.argv[1]
rsListenPort = sys.argv[2]
rsListenPort = int(rsListenPort)
tsListenPort = sys.argv[3]
tsListenPort = int(tsListenPort)

        #socket for client to connect to rs to search for hostname,ip,flag
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as rs_clientsocket: 
    #socket for client to connect to ts if hostname isn't in rs
    #ts_clientsocket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)  
    
    # get root server's ip
    # rsHostname is given as argument1 in command line
    rsHostip = socket.gethostbyname(rsHostname)
    print("[C]: root server's host is {} and ip is {}.".format(rsHostname,rsHostip)) 
    
    # client connects to rs host machine
    rootServerBinding = (rsHostname, rsListenPort)
    # connect to root server 
    rs_clientsocket.connect(rootServerBinding)
    
    # send message to server
    with open("PROJI-HNS.txt", "r") as f:
        for line in f:
            rs_clientsocket.sendall(line.encode())

    #rs_clientsocket.sendall("HELLLLLLOOOOOOO".encode())
    #rs_clientsocket.sendall("WORLDDDDDD".encode())
    """
    # get top server's hostname
    tsHostname = socket.gethostname()
    # get top server's ip
   tsHostip = socket.gethostbyname(tsHostname)
    """

