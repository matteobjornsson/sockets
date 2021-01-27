#!/usr/bin/python

import socket
import struct
import binascii
from datetime import datetime

# creating a rawSocket for communications
# PF_SOCKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x08000 = IP Protocol
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# deciding interface - packet sniffing and then injection
rawSocket.bind(("enp0s3", socket.htons(0x0800)))

# create a ethernet packet
packet = struct.pack("!6s6s2s", 
            binascii.unhexlify('aaaaaaaaaaaa'), 
            binascii.unhexlify('bbbbbbbbbbbb'), 
            binascii.unhexlify('0800'))
# 6 dest address, 6 source address and 2 for ethtype = IP
# ip header fields

ip_ihl = 5
ip_ver = 4
ip_tos = 0
ip_tot_len = 0 #kernel will fill the total correct length
ip_id = 54321 # id of this packet
ip_frag_off = 0
ip_ttl = 255
ip_proto = socket.IPPROTO_UDP
ip_check = 0
ip_saddr = socket.inet_aton ('127.0.0.1')
ip_daddr = socket.inet_aton ('127.0.0.1')
ip_ihl_ver = (ip_ver << 4) + ip_ihl

# ip header
ip_header = struct.pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

now = datetime.now()
# UDP header fields
data = 'hello from udp' + str(now)
sport = 4441
dport = 5005
length = 8 + len(data)
checksum = 0

# UDP header
udp_header = struct.pack('!HHHH', sport, dport, length, checksum)

# inject a random string after the header
rawSocket.send(packet + ip_header + udp_header + data.encode('utf8'))
