import socket
import os
import select
import sys

#HOSTNAME = socket.gethostbyname('linux.scs.ubbcluj.ro')
HOSTNAME = 'localhost'
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOSTNAME, PORT))
except:
    print("ERROR > Unable to connect")
    sys.exit()

s.send(' '.join(sys.argv[1:]))
data = s.recv(1024*1024)
if not data:
    print("ERROR > Disconected from chat Server")

print("RECEIVED:\n" + data);
