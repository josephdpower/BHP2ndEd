#book exercise
# looks similar to TCP version
# added line 16 so the fucking thing actually works

import socket

target_host = "127.0.0.1"
target_port = 9997

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## original code didn't work; adding .bind() from this SO thread
# https://stackoverflow.com/questions/37191612/issue-with-receiving-response-from-127-0-0-1-with-udp-client-in-python

client.bind((target_host, target_port))

# send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))

# receive something
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()