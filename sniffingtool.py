import sys
import argparse
from scapy.all import scapy

parser = argparse.ArgumentParser()

parser.add_argument("-ip", "--ipadd", help="IP Address/Subnet Mask")
args = parser.parse_args()

if not args.ipadd:
    print("Invalid Syntax")
    print("Use --help or -h for options.")
    sys.exit(1)
else:

    arp_request = scapy.layers.l2.ARP(pdst= args.ipadd)
    broadcast_frame = scapy.layers.l2.Ether(dst="ff:ff:ff:ff:ff:ff")
    final_request = broadcast_frame/arp_request
    results_ans = scapy.layers.l2.srp(final_request, timeout=2, verbose=False)[0]
    
    results = []
    for i in range(0,len(results_ans)):

        clients = {"ip":results_ans[i][1].psrc," mac":results_ans[i][1].hwsrc}
        results.append(clients)
    for i in range(len(results)):
        print(results[i])
