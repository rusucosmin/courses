import socket
import os
import select
import sys

HOSTNAME = 'scs.ubbcluj.ro'
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

