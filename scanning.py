#!/usr/bin/python2

import time
import commands

print commands.getoutput('tcpdump -D |grep -v usb | grep -v nf | grep -v any | cut -d. -f2')

nic= raw_input(" type NIC name from above list to check ip ")

output = commands.getoutput('ifconfig '+nic)

print output.split()

print "finding ip..please wait"

time.sleep(2)

print output.split()[5]

print "Going back to startup program"

time.sleep(2)

execfile('start.py')




