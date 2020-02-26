import threading
import time
import random
import sys
import socket

rsListenPort = sys.argv[1]
rsListenPort = int(rsListenPort)

def sendData(value,sock):
    sock.send(value.encode('utf-8'))
    
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
    rs.listen(5)

    # accept incoming connections
    csockid, addr = rs.accept()
    print("[RS]: Got a connection request from a client at {}\n".format(addr))

    #create a list temporarily to hold domain names from client
    domain_list = []

    cond = True   
    while cond:
        data_from_client = csockid.recv(2048).decode('utf-8')
	domain_list.append(data_from_client)
	print("[RS]: data received from client: {}".format(data_from_client))
	time.sleep(1)
	csockid.send(data_from_client.encode('utf-8'))
	time.sleep(1)
	#echo data_from_client back to client
	
        if data_from_client == "0":
            cond = False
    time.sleep(5)
	
    print("\n")		
    print(domain_list)
    csockid.sendall("hi from server!".encode('utf-8'))
    print("IM TRYING TO SEND TO CLIENT")
    #csockid.send("hi".encode('utf-8'))
    #print("[RS] Tester tried sending to client.")

    # these can be deleted just to test sending and receiving with single vals
    #data = csockid.recv(1024).decode('utf-8')
    #print("[RS] Message received from client: {}".format(data))
    #csockid.send(data.encode('utf-8'))

    #try sending test message to server after receiving domain names
    #to salman abu khan, this is where the problem begins. why isn't this message
    #being sent and successfully received at the client side? if this can be
    #successfully implemented we can send the actual return string back to
    #the client from the root server
    
    #msg = "Hi from server"
    #csockid.send(msg.encode('utf-8'))

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    time.sleep(random.random() * 5)
    #t2 = threading.Thread(name='client', target=client)
    #t2.start()

    #time.sleep(40)
    print("Done.")


   
