hbp45 sha45

1.How our DNS Program Runs:

* note to TA's/grader's, it will take approximately 55 seconds for the program to run, therefore that is when the RESOLVED.txt will appear

Our implementation will discuss the Client, Root Server, and Top Level server. 

Client Side:

To run client file, run command:
python client.py rsHostName rsPort tsPort.

What our client side file does:

The client is defined in the client() function. Inside the client method, we initially set up all the sockets to connect to and from the client. Afterwards, we parse the requested domain names we need to look up from the PROJI-HNS.txt file and store them on a list. These names are then sent to the RS server to be mapped to an IP. The client then waits for the mapped data to be received, containing the Hostname, IP, and Flag in that order. We then sift through the different domain name mappings returned to us by RS and separate these mappings by NS flags and A flags respectively. If there any elements in the NS flag lists, we would send them off to the TS server. In the end when the client has heard back from the RS and/or TS server, it takes the mappings sent back to it and writes it to an output file called RESOLVED.txt


Root Server:

To run rs file, run command:
python rs.py rsPortNumber

What our RS file does:

The root server is defined in the server() function. After initially setting up the sockets to listen for incoming requests, the root server parses the PROJI-DNSRS.txt file and creates a dictionary with the domain name as the key, and a list as its value. The list contains two items. It contains the IP address mapping of the given domain name, and the corresponding flag. 

After receiving incoming requests from the client, it stores the incoming domain name requests on a list. It then traverses through the list, and gets the correct mapping for each domain name on the list through the dictionary and sends it back to the client for further use.

Top Server:

To run ts file run command:
python ts.py tsPortNumber 

The top server is defined in the server() function. After the initial set up of the server, the top server parses PROJI-DNSTS.txt file and stores the domain names in the same way the root server does. If the incoming requests map to a domain name on the ts server, then the proper hostname IP and flag are sent back to client. Otherwise an error is sent back.

2. There are no known errors in our code.

3. Some of the problems we faced with developing code for this project dealt with making sure that the data being sent to and from the server reached properly each other properly. In particular, the domains being sent to the server would get jumbled so something like google.com would show up as oogle.com. To fix that we noticed that the time.sleep() function fixed this issue. This allowed for there to be sufficient time for the data to fully transmit to the server before continuing on to the next iteration. Other than that, in general debugging took the most time since little things like missing parentheses would break our code and we would spend a lot of time trying to find out what was wrong because the error messages weren’t clear.

4. In this project, we learned about how the DNS works in real life. The project allowed us to create an intuitive solution to the DNS mapping problem and overall lead to a deeper understanding of DNS, sockets, and networks. 
