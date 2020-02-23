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
    print("[rs]: root server name is {}\n".format(rsServerHost))
    
    # get root server ip address
    rsHostip = socket.gethostbyname(rsServerHost)
    print("[rs] root server ip is {}\n".format(rsHostip))
    
    #bind host,port
    rs.bind((rsServerHost,rsListenPort))

    #root server listen
    rs.listen()

    # accept incoming connections
    csockid, addr = rs.accept()
    print("[rs]: Got a connection request from a client at {}".format(addr))
    
    with csockid:
        print("Connected by ", csockid)
        while True:
            data_from_client = csockid.recv(1024).decode("ascii")
            print("[rs]: data received from client: {}".format(data_from_client))
            if not data_from_client:
                break
"""
if __name__ == "__main__":
    t1 = threading.Thread(name="server", target=server)
    t1.start()

    time.sleep(random.random() * 5)

    time.sleep(5)
    print("Finished")
"""
