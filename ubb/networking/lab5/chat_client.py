import socket
import os
import select
import sys

HOSTNAME = 'localhost'
PORT = 5000

def prompt():
	sys.stdout.write("YOU > ")
	sys.stdout.flush()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

try:
	s.connect((HOSTNAME, PORT))
except:
	print("ERROR > Unable to connect");
	sys.exit()

prompt()

while 1:
	socket_list = [sys.stdin, s]
	 
	# Get the list sockets which are readable
	read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
	 
	for sock in read_sockets:
	    #incoming message from remote server
	    if sock == s:
		data = sock.recv(4096)
		if not data :
		    print '\nDisconnected from chat server'
		    sys.exit()
		else :
		    	#print data
			sys.stdout.write("\n")
			sys.stdout.write(data)
			prompt()
	     
	    #user entered a message
	    else :
		msg = sys.stdin.readline()
		s.send(msg)
		prompt()

