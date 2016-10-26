import socket
import sys

#UDP_IP = "127.0.0.1"
UDP_IP = socket.gethostbyname("linux.scs.ubbcluj.ro")
print(UDP_IP)
UDP_PORT = 2222

l = sys.argv[1:]
print(l)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (UDP_IP, UDP_PORT)

sock.sendto(str(len(l)), server_addr)
data, server = sock.recvfrom(1024)
print("server %s responded %s" % (str(server), data))

new_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
new_server_addr = (UDP_IP, int(data))

for x in l:
    new_sock.sendto(str(x), new_server_addr)

new_data, new_server = new_sock.recvfrom(1024)
print("server %s responded %s" % (str(new_server), new_data))

