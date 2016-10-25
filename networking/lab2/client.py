import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (UDP_IP, UDP_PORT)

sock.sendto("100 200 300 500 600", server_addr)

data, server = sock.recvfrom(1024)
print("server %s responded %s" % (str(server), data))

