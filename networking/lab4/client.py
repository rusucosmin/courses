import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (UDP_IP, UDP_PORT)

l = [1, 2, 3, 4, 5];

sock.sendto(str(len(l)), server_addr)
data, server = sock.recvfrom(1024)
print("server %s responded %s" % (str(server), data))

new_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
new_server_addr = (UDP_IP, int(data))

for x in l:
    sock.sendto(str(x), new_server_addr)

new_data, new_server = sock.recvfrom(1024)
print("server %s responded %s" % (str(new_server), new_data))

