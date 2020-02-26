import threading
import time
import random
import sys
import socket

tsListenPort = sys.argv[1]
tsListenPort = int(tsListenPort)

def server():
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[TS]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n',format(err))
        exit()

    # get top server host name
    tsServerHost = socket.gethostname()
    print("[TS]: top server name is {}".format(tsServerHost))

    # get top server ip address
    tsHostip = socket.gethostbyname(tsServerHost)
    print("[TS] root server ip is {}".format(tsHostip))
  
    # bind host,port
    rs.bind((tsServerHost, tsListenPort))

    # top server listens
    ts.listen(5)

    # accept incoming connections
    csockid, addr = ts.accept()
    print("[RS]: Got a connection request from a client at {}\n".format(addr))

if __name__ == "__main__":
    t3 = threading.Thread(name='server', target=server)
    t3.start()

    time.sleep(random.random() * 5)
    print("Done.")

