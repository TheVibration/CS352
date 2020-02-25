import threading 
import time
import random
import socket
import sys

rsListenPort = sys.argv[1]
rsListenPort = int(rsListenPort)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as rs:
    
    print("[rs]: root server created")
    
    # get root server host name
    rsServerHost = socket.gethostname()
    print("[rs]: root server name is {}".format(rsServerHost))
    
    # get root server ip address
    rsHostip = socket.gethostbyname(rsServerHost)
    print("[rs] root server ip is {}".format(rsHostip))
    
    #bind host,port
    rs.bind((rsServerHost,rsListenPort))

    #root server listen
    rs.listen()

    # accept incoming connections
    csockid, addr = rs.accept()
    print("[rs]: Got a connection request from a client at {}".format(addr))
   
    #create a list temporarily to hold domain names from client
    domain_list = []
    print("Connected by ", addr)
    print("\n")
    
    msg = "tester"
    msg2 = "tester2"
    csockid.send(msg.encode('utf-8'))
    csockid.send(msg2.encode('utf-8'))
    while True:
        data_from_client = csockid.recv(1024).decode('utf-8')
        print("[rs]: data received from client: {}".format(data_from_client))
        domain_list.append(data_from_client)

        if not data_from_client:
            break

    #for domain in domain_list:
        #csockid.send(domain.encode('utf-8'))
    

    #this was created because for some reason
    #the last value the server is receiving from
    #the client is ''. so this loop goes through
    #the domain_list and removed that ''.
    counter = 0
    for domain in domain_list:
        if domain == '':
            del domain_list[counter]
        else:
            counter = counter+1

    print("\n")
    print(domain_list)

"""
if __name__ == "__main__":
    t1 = threading.Thread(name="server", target=server)
    t1.start()

    time.sleep(random.random() * 5)

    time.sleep(5)
    print("Finished")
"""
