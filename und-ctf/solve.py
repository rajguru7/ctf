# The fixed 16 bytes of the PNG file (PNG signature + IHDR chunk header)
png_fixed_header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52'

# Load the encrypted file contents (we will use the first 16 bytes of the ciphertext)
with open('flag.png.enc', 'rb') as enc_file:
    encrypted_data = enc_file.read()

# Extract the first 16 bytes of the ciphertext
ciphertext_header = encrypted_data[:16]

# XOR the first 16 bytes of the plaintext (fixed PNG header) with the ciphertext to derive the keystream
keystream = bytes([p ^ c for p, c in zip(png_fixed_header, ciphertext_header)])

# Display the derived keystream
keystream

