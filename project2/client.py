import socket
import sys
import time
import threading

def lsclient(domain, lsHostName,lsListenPort):
    try:
        lscs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    
    # get ls ip
    lsHostIp = socket.gethostbyname(lsHostName)

    #bind
    server_binding = (lsHostIp,lsListenPort)
    lscs.connect(server_binding)

    #send to ls
    lscs.send(domain.encode('utf-8'))

    #receive from ls
    mapping = lscd.recv(1024).decode('utf-8')

    #close lscs
    lscs.close()

    return mapping

if __name__ == "__main__":
    with open('RESOLVED.txt', 'w+') as f:
        with open('PROJ2-HNS.txt', 'r') as domains:
           lines = domains.read().splitlines()
           for line in lines:
               f.write(lsclient(line.lower(),sys.argv[1],int(sys.argv[2]) + "\n"))
