import threading
import time
import random
import sys
import socket

rsListenPort = sys.argv[1]
rsListenPort = int(rsListenPort)
#djdjdjd
def sendData(value,sock):
    sock.send(value.encode('utf-8'))

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

# go through the dictionary and find where the tshostname is
def getTS(dictionary):
    for key in dictionary:
        k = dictionary[key]
	if k[1] == "NS":
	    returnVal = key 
            break
    return returnVal

def return_dns_query(dictionary,domain):
    if domain in dictionary:
        values = dictionary[domain]
        ipaddress = values[0] 
        flag = values[1]
        return domain + " " + ipaddress + " " + flag
    else:
        return domain + " - NS"

def server():
    newDict = file_to_dict("PROJI-DNSRS.txt")

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
        data_from_client = csockid.recv(1024).decode('ascii')
        if data_from_client != "*":
	    domain_list.append(data_from_client)
	    print("[RS]: data received from client: {}".format(data_from_client))
	elif data_from_client == "*":
	    cond = False
	time.sleep(2)
        	
    time.sleep(5)
    
    #if "*" in domain_list:
        #domain_list.remove("*")	
    
    print("\n[RS] Domains received from client:")		
    domain_list = [str(r) for r in domain_list]
    print(domain_list)
    print("\n")

    #a way to send the correct string back to client
    for dn in domain_list:
        result = return_dns_query(newDict,dn.lower())
	    print("[RS] sending to client: {}".format(result))
        csockid.send(result.encode('ascii'))
	    time.sleep(3)
    csockid.send("00".encode('ascii'))

    time.sleep(1)
    tsHostName = getTS(newDict)
    csockid.send(tsHostName.encode("ascii"))
    
    #print(domain_list)
    print("\nRS DNS table as hash map:")
    print(newDict)

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    time.sleep(random.random() * 5)
    #t2 = threading.Thread(name='client', target=client)
    #t2.start()

    #time.sleep(40)
    print("Done.")


   
