import socket
import binascii

HOST = 'host5.metaproblems.com'
PORT = 7040
# HOST = 'localhost'
# PORT = 1234

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

def receive_until(s, end_marker):
    data = b""
    while not data.endswith(end_marker):
        chunk = s.recv(1024)
        # print(chunk)
        if not chunk:
            break
        data += chunk
    return data

def send_and_receive(s, message, end_marker=b'> '):
    s.sendall(message)
    return receive_until(s, end_marker)

def encrypt_message(s, message):
    send_and_receive(s, b'1\n', b': ')  # Select the encryption option
    print(f"Encrypting: {message}")
    response = send_and_receive(s, message + b'\n')
    encrypted_message = response.split(b"Encrypted message: ")[1].split()[0]
    print("encrypted_message:", encrypted_message)
    print("len(encrypted_message):", len(encrypted_message))
    return encrypted_message

def decrypt_message(s, encrypted_message):
    send_and_receive(s, b'2\n', b': ')  # Select the decryption option
    response = send_and_receive(s, encrypted_message + b'\n')
    return response

def xor_strings(s1, s2):
    return ''.join(chr(a ^ b) for a, b in zip(s1, s2))

def xor_bytes(b1, b2):
    return bytes([a ^ b for a, b in zip(b1, b2)])

def flip_iv(iv_hex, original_payload, desired_payload):
    iv = binascii.unhexlify(iv_hex)
    original_bytes = original_payload.encode()
    desired_bytes = desired_payload.encode()

    # flipped_iv = xor_strings(iv, xor_strings(original_bytes, desired_bytes))
    payload = b"\x00" * (16 - len(original_bytes)) + xor_bytes(original_bytes, desired_bytes)
    # flipped_iv = xor_bytes(iv, xor_bytes(original_bytes, desired_bytes))
    flipped_iv = xor_bytes(iv, payload)
    
    print("len(flipped_iv):", len(flipped_iv))
    return binascii.hexlify(flipped_iv).decode()

def main():
    # Connect to the server
    s = connect()
    receive_until(s, b'> ')

    # Step 1: Encrypt a benign payload that we can modify later
    initial_payload = b"puts 'AAAAAAAAA'"  # We want to execute eval("puts '
    initial_payload = b"AAAAAAAAA"  # We want to execute eval("puts '
    encrypted_hex = encrypt_message(s, initial_payload)

    # initial_payload = "puts 'LA'"
    
    # Split the ciphertext into IV and the encrypted message
    # iv_hex = encrypted_hex[:32]  # First 32 hex characters (16 bytes) for IV
    # ciphertext_hex = encrypted_hex[32:]  # The rest is the ciphertext
    # encrypted_bytes = binascii.unhexlify(encrypted_hex)
    encrypted_bytes = binascii.unhexlify(encrypted_hex)

    mod_ciphertext = bytearray(encrypted_bytes)

    # Step 2: Flip bits in the IV to create a new command 
    desired_payload = b"puts        FLAG"  # We want to execute eval("puts 'FLAG'")
    # new_iv_hex = flip_iv(iv_hex, initial_payload, desired_payload)

    p1 = 21 # '  
    p2 = 22 # A  
    p3 = 23 # A  
    p4 = 24 # A
    p5 = 25 # A
    p6 = 26 # A
    p7 = 27 # A
    p8 = 28 # A F
    p9 = 29 # A L
    p10 = 30 # A A
    p11 = 31 # ' G


    mod_ciphertext[p1 - 16] = ord("'") ^ mod_ciphertext[p1 - 16] ^ ord(' ') # xor operation
    mod_ciphertext[p2 - 16] = ord('A') ^ mod_ciphertext[p2 - 16] ^ ord(' ') # xor operation
    mod_ciphertext[p3 - 16] = ord('A') ^ mod_ciphertext[p4 - 16] ^ ord(' ') # xor operation
    mod_ciphertext[p4 - 16] = ord('A') ^ mod_ciphertext[p4 - 16] ^ ord(' ') # xor operation
    mod_ciphertext[p5 - 16] = ord('A') ^ mod_ciphertext[p5 - 16] ^ ord(' ') # xor operation
    mod_ciphertext[p6 - 16] = ord('A') ^ mod_ciphertext[p6 - 16] ^ ord(' ') # xor operation
    mod_ciphertext[p7 - 16] = ord('A') ^ mod_ciphertext[p7 - 16] ^ ord(' ') # xor operation
    mod_ciphertext[p8 - 16] = ord('A') ^ mod_ciphertext[p8 - 16] ^ ord('F') # xor operation
    mod_ciphertext[p9 - 16] = ord('A') ^ mod_ciphertext[p9 - 16] ^ ord('L') # xor operation
    mod_ciphertext[p10 - 16] = ord("A") ^ mod_ciphertext[p10 - 16] ^ ord('A') # xor operation
    mod_ciphertext[p11 - 16] = ord("'") ^ mod_ciphertext[p11 - 16] ^ ord('G') # xor operation

    # Step 3: Submit the modified IV + original ciphertext for decryption
    # modified_encrypted_hex = new_iv_hex + ciphertext_hex
    # modified_encrypted_hex = mod_ciphertext.hex().encode()
    modified_encrypted_hex = binascii.hexlify(mod_ciphertext)
    # print("new_iv_hex:", new_iv_hex)
    # print("ciphertext_hex:", ciphertext_hex)
    response = decrypt_message(s, modified_encrypted_hex)

    # print(f"Modified encrypted hex: {modified_encrypted_hex}")
    # print("len(modified_encrypted_hex):", len(modified_encrypted_hex))
    print(response)  # This should contain the flag

    # Close the connection
    s.close()

if __name__ == "__main__":
    main()

