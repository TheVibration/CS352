Harsh Patel hbp45
Salman Ashraf sha45

1.) The first thing to do was to give each interface an associated IP address. This was done using the "ip addr" command. I implemented this by doing [hostname] ip addr add [IP Address] dev [Interface_Name]. There were 4 total for each host and 4 for r1 because it has 4 interfaces.
In order to set up default routes for the host, it's understood this is the default route which the packets on the host towards the router & this was done by [hostname] ip route add default via [IP_Address] dev [Interface]. Lastly creating the forwarding table for the router was straight forward and simple because we want packets that have a certain destination going to the correct port or interface. This is similar as the last step, and the command used was the same as before except it was r1 and no longer default. After this I could test by using ping and traceroute.

2.) There aren't any issues or functions that aren't working.

3.) One issue I faced was learning how to transfer files from Windows host to virtualbox mininet guest machine. I learned to I had to mess around with the network section of the mininet virtual machine and I was able to use scp to transfer what I needed. Afterwards it was just able googling and reading up on the "ip addr" and "ip route" commands.

4.) I learned that life without DHCP is very hard. This was a relatively small network, therefore for a large network in a time before DHCP which helps give each host an IP Address automatically among other great things, I can imagine a system administrator wanting to pull his/her hair out. I also learned that it's not complicated to setup a small network within my house, if I have a couple laptops lying around, I can connect it to ports on my router and assign each laptop interface a specific IP and I can set my own routing table which is cool.


