#!/usr/bin/env python

import sys
import os
import subprocess


def main():
    if len(sys.argv) != 3:
        print("Usage: {} <binary> <input>".format(sys.argv[0]))
        sys.exit(1)

    binary = sys.argv[1]
    input_string = sys.argv[2].encode()

    if not os.path.exists(binary):
        print("Binary {} not found".format(binary))
        sys.exit(1)


    proc = subprocess.Popen([binary], stdin=subprocess.PIPE)
    proc.communicate(input=input_string)

if __name__ == "__main__":
    main()
