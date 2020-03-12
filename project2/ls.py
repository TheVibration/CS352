import socket
import sys
import time

def lsserver(lsListenPort, ts1HostName, ts1ListenPort, ts2Hostname, ts2ListenPort):
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    
    #bind
    server_binding = ('',lsListenPort)
    ls.bind(server_binding)

    #listen for incoming requests
    ls.listen(5)

if __name__ == '__main__':
    lsserver(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]))
