#!/usr/bin/env python
import sys

def usage():
    print(f"Usage: {sys.argv[0]} <encrypt>/<decrypt> <text> <offset>")
    sys.exit(1)

def encrypt():
    return ''.join(chr(ord(i)+offset) if ord(i)+offset <= ord('Z') else
                   chr(ord(i)+offset-26) for i in text)

def decrypt():
    return ''.join(chr(ord(i)-offset) if ord(i)-offset >= ord('A') else
                   chr(ord(i)-offset+26) for i in text)

if len(sys.argv) != 4:
    usage()

task = sys.argv[1]
text = sys.argv[2].upper()
offset = int(sys.argv[3]) % 26 # if offset is entered > 26


if task == "encrypt":
    print(encrypt())
elif task == "decrypt":
    print(decrypt())
else:
    usage()


