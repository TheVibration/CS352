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
    
    # domain name list from text file
    lst = []
    # open up file and go through each line, place contents in list called lst
    with open("PROJI-HNS.txt", "r") as f:
        lines = f.readlines()
        #print(lines)
    for line in lines:
        lst.append(line.strip())
    
    #send contents on lst to server
    print("\n")
    for domainName in lst:
        print(domainName)
        rs_clientsocket.send(domainName.encode('utf-8'))
    
    # receive from the rs.py server
    #data_from_server = rs_clientsocket.recv(1024)
    #print("[C] Data received from server: {}".format(data_from_server.decode('utf-8'))

    #rs_clientsocket.sendall("HELLLLLLOOOOOOO".encode())
    #rs_clientsocket.sendall("WORLDDDDDD".encode())
