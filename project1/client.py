import threading
import time
import random
import sys
import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCKET_STREAM) # creates client socket
    except socket.error as err:
        print("socket open error: {} \n".format(err))
        exit

    rsHostname = sys.argv[1]
    rsListenPort = sys.argv[2]
    tsListenPort = sys.argv[3]

    # get root server's hostname
    rsHostname = socket.gethostname()
    # get root server's ip
    rsHostip = socket.gethostbyname(rsHostname)
    # client connects to rs host machine
    rootServerBinding = (rsHostname, rsHostip)


    # get top server's hostname
    tsHostname = socket.gethostname()
    # get top server's ip
    tsHostip = socket.gethostbyname(tsHostname)
