## Assembly

AT&T-style disassembly or Intel-style disassembly
Since the instructions don't have length suffixes and the registers are not
prefixed with %, we're talking about Intel-style, where destination comes first.

When `leave` is called:

```
mov esp,ebp --> Intel-style
mov %ebp, %esp --> AT&T-style
```
<https://visualgdb.com/gdbreference/commands/set_disassembly-flavor>


push and pop affect the stack pointer as well.

```
~/ctf/osiris_recruit/pwn/por/src [main]✗ $ gcc main.c -no-pie -fno-stack-protector -z execstack -o main
~/ctf/osiris_recruit/pwn/por/src [main]✗ $ checksec main
[*] '/home/killua/ctf/osiris_recruit/pwn/por/src/main'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX unknown - GNU_STACK missing
    PIE:      No PIE (0x400000)
    Stack:    Executable
    RWX:      Has RWX segments
```


Trying to understand the meaning of ABI:

<https://stackoverflow.com/questions/2171177/what-is-an-application-binary-interface-abi#:~:text=An%20application%20binary%20interface%20(ABI)%20is%20similar%20to%20an%20API,or%20at%20the%20OS%20level.>


