import threading
import time
import random
import sys
import socket

rsHostname = sys.argv[1]
rsListenPort = sys.argv[2]
rsListenPort = int(rsListenPort)
tsListenPort = sys.argv[3]
tsListenPort = int(tsListenPort)

# This function is for writing to RESOLVED.txt
def writing(dnList, fileName):
    for domain in dnList:
        f = open(fileName, "a")
        f.write(domain+"\n")
    f.close()

# this functions splits the return from dn.py
def returnSplitter(lst):
    send_to_ts = []
    for val in lst:
	holder = val.split()
	send_to_ts.append(holder[0])
    return send_to_ts

def client():
    # create a socket for rs connection
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # get root server's ip
    # rsHostname is given as argument1 in command line
    rsHostip = socket.gethostbyname(rsHostname)
    print("[C]: root server's host is {} and ip is {}.".format(rsHostname,rsHostip)) 
    
    # client connects to rs host machine
    rootServerBinding = (rsHostname, rsListenPort)
    # connect to root server 
    cs.connect(rootServerBinding)
    
    # domain name list from text file
    lst = []
    # open up file and go through each line, place contents in list called lst
    with open("PROJI-HNS.txt", "r") as f:
        lines = f.readlines()
        #prish hbp45@ilab.cs.rutgers.edu
    #t(lines)
    for line in lines:
        lst.append(line.strip())
    

    #send contents on lst to server
    print("\n")
    for domainName in lst:
        print("[C] Sending domain to RS: {}".format(domainName)) #this helps with sending domainName efficiently. put time instead.
        cs.send(domainName.encode('ascii'))
   	time.sleep(2) 
    cs.send("*".encode('ascii'))	
    time.sleep(8)
    
    # return_lst is going to hold the host,ip,flag returned from rs
    return_lst = []
    print("\n")
    
    cond = True
    #this while loop begins receiving the hostname,ip,flag
    while cond:
	from_rs = cs.recv(1024).decode('ascii')
	time.sleep(2)
	if from_rs != "00":
	    print("[C] debugger: {}".format(from_rs))
	    return_lst.append(from_rs)
	elif from_rs == "00":
	    cond = False
   
    # receive the tshostname from rs.py and store it in a variable
    time.sleep(1)
    TShostname = cs.recv(1024).decode('ascii') 
    print("\n[C] TSHostName from RS is: {}".format(TShostname))

    print("\n[C] hostname,ip,flag in list:")
    return_lst = [str(r) for r in return_lst] #gets rid of u
    print(return_lst)
    
    # this list contains valid domain name mappings
    # received from rs.py with a valid A flag
    a_rslst = []
    ns_tslst = []
    for string in return_lst:
        if 'NS' not in string:
	    a_rslst.append(string)
	else:
	    ns_tslst.append(string)
    print("\n[C] list with A strings from RS:")
    print(a_rslst)	
    print("\n[C] list with NS string that need to be sent to ts.py:")
    print(ns_tslst)
	
    # this contents of this list will
    # be sent to the ts server to look at 
    # its dns name to ip mappings
    send_to_ts = returnSplitter(ns_tslst)
    print("\n[C] domain names to try in ts:")
    print(send_to_ts)

    if send_to_ts:
        #create a socket for ts connection
	cs.close()
        try:
            cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("\n[C]: Client socket for ts created")
        except socket.error as err:
            print('socket open error: {} \n'.format(err))
            exit()
    # get top server's ip
    # TShostname is the top server's hostname
    tsHostip = socket.gethostbyname(TShostname)
    print("[C]: Top Server's host is {} and ip is {}.".format(TShostname, tsHostip))
    
    # client connects to ts host machine
    topServerBinding = ('ilab1.cs.rutgers.edu',tsListenPort)

    # connect to top server
    cs2.connect(topServerBinding)

    #send contents on lst to server
    print("\n")
    for domainName in send_to_ts:
        print("[C] Sending domain to TS: {}".format(domainName)) #this helps with sending domainName efficiently. put time instead.
        cs2.send(domainName.encode('ascii'))
   	time.sleep(2) 
    cs2.send("*".encode('ascii'))	
    time.sleep(8)

if __name__ == "__main__":
    #t1 = threading.Thread(name='server', target=server)
    #t1.start()

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    #time.sleep(40)
    print("Done.")
    
