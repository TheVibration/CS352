import threading 
import time
import random
import socket
import sys

rsListenPort = sys.argv[1]

def socket():
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[rs]: root server created")
    except:
        print("socket open error: {}\n".format(err))
        exit()
    
    # get root server host name
    rsServerHost = socket.gethostbyname()
    print("[rs]: root server name is {}\n".format(rsServerHost))
    # get root server ip address
    rsHostip = socket.gethostbyname(rsServerHost)
    print("[rs] root server ip is {}\n".format(rsHostip))
    
    #bind host,port
    rs.bind(rsHostip,rsListenPort)

    #root server listen
    rs.listen()

    # accept incoming connections
    csockid, addr = rs.accept()
    print("[rs]: Got a connection request from a client at {}".format(addr))
