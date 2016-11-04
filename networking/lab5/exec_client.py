import socket
import os
import select
import sys

HOSTNAME = socket.gethostbyname('linux.scs.ubbcluj.ro')
#HOSTNAME = 'localhost'
PORT = 5001
print("Connect to linux.scs.ubbcluj.ro on: %s %d" % (HOSTNAME, PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOSTNAME, PORT))
except:
    print("ERROR > Unable to connect")
    sys.exit()

s.send(' '.join(sys.argv[1:]))
data = s.recv(1024*1024)
if not data:
    print("ERROR > Disconected from exec server")
    sys.exit()

print("RECEIVED:\n" + data);
