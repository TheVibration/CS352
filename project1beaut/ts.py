import threading
import time
import random
import sys
import socket

tsListenPort = sys.argv[1]
tsListenPort = int(tsListenPort)

def file_to_dict(fileName):
    
    f = open(fileName, "r")

    lst = []
    dic = {}

    for line in f:
        for word in line.split():
            lst.append(word)

    counter = 0
    for entry in lst:
        if counter == 0:
            currentKey = entry.lower()
            values = []
            counter = counter + 1
        elif counter == 1:
            values.append(entry)
            counter = counter + 1
        elif counter == 2:
            values.append(entry)
            dic[currentKey] = values
            counter = 0
    
    f.close()
    return dic

def return_dns_query(dictionary,domain):
    if domain in dictionary:
        values = dictionary[domain]
        ipaddress = values[0] 
        flag = values[1]
        return domain + " " + ipaddress + " " + flag
    else:
        return domain + " - Error:HOST NOT FOUND"

def server():
    # turn PROJI-DNSTS.txt into dictionary
    newDict = file_to_dict("PROJI-DNSTS.txt")
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
    ts.bind((tsServerHost, tsListenPort))

    # top server listens
    ts.listen(5)

    # accept incoming connections
    csockid, addr = ts.accept()
    print("[RS]: Got a connection request from a client at {}\n".format(addr))

    #create a list temporarily to hold domain names from client
    domain_list = []

    # receive the NS flagged domain names
    # from the client
    cond = True   
    while cond:
        data_from_client = csockid.recv(1024).decode('ascii')
        if data_from_client != "*":
	    domain_list.append(data_from_client)
	    print("[TS]: data received from client: {}".format(data_from_client))
	elif data_from_client == "*":
	    cond = False
	time.sleep(2)

    print("\n[TS] Domains received from client:")		
    domain_list = [str(r) for r in domain_list]
    print(domain_list)
    print("\n")


if __name__ == "__main__":
    t3 = threading.Thread(name='server', target=server)
    t3.start()

    time.sleep(random.random() * 5)
    print("Done.")

