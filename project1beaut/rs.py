import threading
import time
import random
import sys
import socket

rsListenPort = sys.argv[1]
rsListenPort = int(rsListenPort)

def server():
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[RS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    # get root server host name
    rsServerHost = socket.gethostname()
    print("[RS]: root server name is {}".format(rsServerHost))
    
    # get root server ip address
    rsHostip = socket.gethostbyname(rsServerHost)
    print("[RS] root server ip is {}".format(rsHostip))
    
    #bind host,port
    rs.bind((rsServerHost,rsListenPort))

    #root server listen
    rs.listen()

    # accept incoming connections
    csockid, addr = rs.accept()
    print("[RS]: Got a connection request from a client at {}\n".format(addr))

    #create a list temporarily to hold domain names from client
    domain_list = []
    
    while True:
        data_from_client = csockid.recv(1024).decode('utf-8')
        if not data_from_client:
            break
        print("[RS]: data received from client: {}".format(data_from_client))
        domain_list.append(data_from_client)
    
    #try sending test message to server after receiving domain names
    #to salman abu khan, this is where the problem begins. why isn't this message
    #being sent and successfully received at the client side? if this can be
    #successfully implemented we can send the actual return string back to
    #the client from the root server
    csockid.send("from server hi".encode('utf-8'))

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    #time.sleep(random.random() * 5)
    #t2 = threading.Thread(name='client', target=client)
    #t2.start()

    time.sleep(5)
    print("Done.")


   
