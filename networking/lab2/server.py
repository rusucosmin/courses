import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("> Starting server at %s:%d ..." % (UDP_IP, UDP_PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("> Started server!")

while True:
    data, addr = sock.recvfrom(1024)
    print("client %s sent: %s" % (str(addr), data))
    response = ""
    data = data.split()
    if len(data) != 2:
        response = "please send me two numbers"
    else:
        response = int(data[0]) + int(data[1])
    sock.sendto(str(response), addr)
