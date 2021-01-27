#!/usr/bin/python

import socket
import struct
import binascii


UDP_IP = '127.0.0.1'
UDP_PORT = 5005

# creating a rawSocket for communications
# PF_SOCKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x08000 = IP Protocol
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
udpSocket.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = udpSocket.recvfrom(2048)
    print("received message: " + data)

# while True:
#     # read a packet with recvfrom method
#     pkt = rawSocket.recvfrom(2048) # tuple return
    
#     # Ethernet Header tuple segmentation    
#     eHeader = pkt[0][0:14]

#     # parsing using unpack
#     eth_hdr = struct.unpack("!6s6s2s", eHeader) # 6 dest MAC, 6 host MAC, 2 ethType

#     # print the receiver frame address
#     print(binascii.hexlify(eth_hdr[1]))
    
#     if binascii.hexlify(eth_hdr[1]) == b'bbbbbbbbbbbb':
#         print('Found our frame!')
#         break

