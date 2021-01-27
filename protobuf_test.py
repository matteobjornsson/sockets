import udp_pb2


udp = udp_pb2.Header()
udp.src_port = 5000
udp.dst_port = 6000

print(udp)

f = open("message", "wb")
f.write(udp.SerializeToString())
f.close()

udp2 = udp_pb2.Header()
f = open('message', "rb")
udp2.ParseFromString(f.read())
f.close()

print(udp2)


