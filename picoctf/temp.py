import sys

flag=list(sys.stdin.readline())

print(flag)

flag = [ord(i) for i in flag]
ans = []
for i in range(len(flag)):
    ans.append(chr(flag[i] >> 8))
    ans.append(chr(flag[i] - (ord(ans[i*2]) << 8)))
print(''.join(ans))
