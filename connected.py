import time
import commands

print "finding connected ip..please wait"

time.sleep(2)

print commands.getoutput("arp -a | cut -d'(' -f2 | cut -d')' -f1")


print "Going back to startup program"

time.sleep(2)

execfile('start.py')


