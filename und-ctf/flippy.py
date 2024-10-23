from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(key, iv, plaintext):
    plaintext = pad(plaintext.encode(), AES.block_size) 
    # add padding
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext, 16) 
    # remove padding
    return plaintext

key = bytes.fromhex('63f835d0e3b9c70130797be59e25c00f')
iv = bytes.fromhex('00000000000000000000000000000000') 

plaintext = 'DOGECOIN transaction: 100 DOGE to BOB@myemail.gg'
# plaintext = b"puts 'LA      '" + b"\x00"
original_plaintext = plaintext
ciphertext = encrypt(key, iv, plaintext)
print(type(ciphertext))
print('[+] Ciphertext: ', ciphertext.hex())

mod_plaintext = 'DOGECOIN transaction: 100 DOGE to EVE@myemail.gg'

target_pos1 = 34 # B to E
target_pos2 = 35 # O to V
target_pos3 = 36 # B to E

mod_ciphertext = bytearray(ciphertext)

# change B to E in position 34
mod_ciphertext[target_pos1 - 16] = ord('B') ^ ciphertext[target_pos1 - 16] ^ ord('E') # xor operation
# change O to V in position 35
mod_ciphertext[target_pos2 - 16] = ord('O') ^ ciphertext[target_pos2 - 16] ^ ord('V') # xor operation
# change B to E in position 36
mod_ciphertext[target_pos3 - 16] = ord('B') ^ ciphertext[target_pos3 - 16] ^ ord('E') # xor operation

print('[+] Old ciphertext: ', ciphertext.hex())
print('[+] New ciphertext: ', mod_ciphertext.hex())

print('[-] Decrypting...')

mod_plaintext = decrypt(key, iv, mod_ciphertext)

print('[+] Original plaintext: ', original_plaintext)
print('[+] Modified ciphertext ', mod_plaintext)
