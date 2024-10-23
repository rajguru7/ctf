# UND CTF

## crypto

**Flippy**

* decrypt is taking the IV from the message
* encrypt provides the first 16bytes as the iv
* every decrypt process must be preceded by encrypt process to get the correct iv.
* For each encrypt packet the iv will be different
* the input to encrypt is sanitized
* the input to decrypt is not sanitized

[How you can use padding oracle attack](https://book.hacktricks.xyz/crypto-and-stego/padding-oracle-priv)


Turns out complete padding oracle is not required as I already have the
decryption for any given ciphertext using the encrypt function. What I need to
do next is the extension of the padding oracle attack. I just need to flip some
bits to introduce a space in the plaintext to print the FLAG value. I also have
control over the IV to counter the modifications I make in the ciphertext.

[Why you can encrypt chosen plaintext](<https://crypto.stackexchange.com/questions/29706/creating-own-ciphertext-after-a-padding-oracle-attack/50050#50050>)

Payload I want to send: `p FLAG`

So this will be encrypted to two blocks of 16 bytes each.


Payload I will send: `psFLAG`
To counter the padding 

ruby has null bytes in strings that it counts when encrypting.
python does not have null bytes in strings.

Python script to send the payload:









---
