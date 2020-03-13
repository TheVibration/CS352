import socket
import sys
import time

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

def tsserver(table,ts1ListenPort):
    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tsHostName = socket.gethostname()
        tsHostIp = socket.gethostbyname(tsHostName)
        print("[TS1]: Server host: {}".format(tsHostName))
        print("[TS1]: Server IP Address: {}".format(tsHostIp))
    except socket.error as err:
        print("socket open error: {}\n".format(err))
        exit()

    #bind
    server_binding = ('',ts1ListenPort)
    ts1.bind(server_binding)

    #listen for incoming requests
    ts1.listen(5)

    while True:
        csockid, addr = ts1.accept()
        domain = csockid.recv(100).decode('utf-8')
        
        if domain in table:
            values = table[domain]
            ipaddress = values[0]
            flag = values[1]
            string = domain + " " + ipaddress + " " + flag
            csockid.send(string.encode('utf-8'))
        else:
            csockid.send("None".encode('utf-8'))
        csockid.close()
 
if __name__ == '__main__':
    dnshash = file_to_dict("PROJ2-DNSTS1.txt")
    tsserver(dnshash,int(sys.argv[1]))
