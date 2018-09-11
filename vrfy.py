#!/usr/bin/python

#Written By: Cooper Wiegand

#*** WARNING ***
#Use on a host without prior authorization may be illegal
#use responsibly and with caution.

import socket
import sys
if len(sys.argv) != 3:
	print "Usage: vrfy.py <ip> <username>"
	sys.exit(1)

# Create a Socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect=s.connect((sys.argv[1],25))

# Receive the banner
banner=s.recv(1024)
if "220" not in banner:
	exit(2)
print banner

# VRFY a user
s.send('VRFY ' + sys.argv[2] + '\r\n')
result=s.recv(1024)
if "250" not in result:
	exit(3)
print result

# Close the socket
s.close()
