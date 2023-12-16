#book exercise
# looks similar to TCP version
# test using nc 
# $ nc -l 127.0.0.1 997

import socket

target_host = "127.0.0.1"
target_port = 9997

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))

# receive something
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()