#!usr/bin/python2

import time
import commands

print "Connected ips are :::: "

time.sleep(2)

print commands.getoutput("arp -a | cut -d'(' -f2 | cut -d')' -f1")

time.sleep(2)

ip= raw_input("print ip to see the port number")

print ("u selected : ")
print ip
print "connected ports are:::: "

time.sleep(2)

output = commands.getoutput('nmap -n -sS '+ip )
#print output

#print output.split()
print commands.getoutput("'nmap -n -sS '+ip'|grep -v Host | grep -v Not| grep -v PORT | grep -v MAC | grep -v Starting | grep -v Nmap | cut -d' ' -f1" )
