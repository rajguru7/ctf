import sys

class rot13:
    def encode(arg):
        print(arg)
        arg = list(arg)
        for i in range(len(arg)):
            n = ord(arg[i])
            if ((n >= 65 and n <= 77) or (n >= 97 and n <= 109)):
                arg[i] = chr(n + 13)
            elif ((n >= 78 and n <= 90) or (n >= 110 and n <= 122)):
                arg[i] = chr(n - 26 + 13)
        return "".join(arg)

#print(rot13.encode("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"))
print(rot13.encode(sys.stdin.read()))
