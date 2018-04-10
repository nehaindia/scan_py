#!/usr/bin/python2

from time import sleep

print "**********************************************************************************"
print "*************************NET SCANNING********************************************"
print "**********************************************************************************"
options='''
Press 1 to check your own IP
Press 2 to check connected IP
Press q to quit
'''

print options

print "**********************************************************************************"

choice=raw_input() #for taking input from user

if choice == '1':
	execfile('scanning.py')
elif choice == '2':
	execfile('connected.py')
elif choice == 'q':
	exit()
else :
	print "Incorrect Choice"
	exit()

