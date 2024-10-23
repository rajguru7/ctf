#!/usr/bin/env python
import socket
import sys
import time

if len(sys.argv) != 6:
    print("Usage: %s <host> <port> <start> <end> <step>" % sys.argv[0])
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
start = int(sys.argv[3])
end = int(sys.argv[4])
step = int(sys.argv[5])
buffer = []

for i in range(start, end, step):
    buffer.append(b"A" * i + b"\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

for string in buffer:
    data = s.recv(1024)
    if not data:
        print("[-] Connection closed.")
        break
    print(data)

    print("\nFuzzing with %s bytes" % len(string))
    
    s.send(string)
    time.sleep(2)

s.close()

