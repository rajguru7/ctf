from itertools import cycle

# Read the ciphertext from the file
with open("ct", "rb") as ct_file:
    ct = ct_file.read()

key = bytes(x ^ y for x, y in zip(b"uiuctf{", ct[:7]))

print(key)

# try all alphabets for the 8th byte

for i in range(256):
    try_key = key + bytes([i])
    flag = bytes(x ^ y for x, y in zip(ct, cycle(try_key)))
    print(flag)

