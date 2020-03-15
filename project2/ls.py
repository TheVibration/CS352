import socket
import sys
import time

def client(socketName, domain, tsHostName, tsListenPort):
    try:
        socketName = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("socket open error: {}\n".format(err))

    #get ts ip
    tsHostIp = socket.gethostbyname(tsHostName)

    #bind
    server_binding = (tsHostIp, tsListenPort)
    socketName.connect(server_binding)

    #send to ts
    socketName.send(domain.encode('utf-8'))

    #receive from ls
    mapping = socketName.recv(100).decode('utf-8')

    #close ts
    socketName.close()
    
    return mapping

def lsserver(lsListenPort, ts1HostName, ts1ListenPort, ts2HostName, ts2ListenPort):
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsHostName = socket.gethostname()
        lsHostIp = socket.gethostbyname(lsHostName)
        print("[LS]: Server host name is {}".format(lsHostName))
        print("[LS]: Server host ip is: {}".format(lsHostIp))
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    
    #bind
    server_binding = ('',lsListenPort)
    ls.bind(server_binding)

    #listen for incoming requests
    ls.listen(5)
    
    from_clientpy = []
    final = []

    while True:
        csockid, addr = ls.accept()
        
        domain = csockid.recv(100).decode('utf-8')
        if domain != "close":
            from_clientpy.append(domain)
            print("[LS]: Received: {}".format(domain))

            #***************************************
            val = client("ts1",domain,ts1HostName,ts1ListenPort)
            if val != "None":
                final.append(val)
                csockid.send(val.encode('utf-8'))
                csockid.close()
            else:
                val = client("ts2",domain,ts2HostName,ts2ListenPort)
                final.append(val)
                csockid.send(val.encode('utf-8'))
                csockid.close()
        else:
            csockid.send("closing".encode('utf-8'))
            csockid.close()
            ls.close()
            break

if __name__ == '__main__':
    lsserver(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]))

