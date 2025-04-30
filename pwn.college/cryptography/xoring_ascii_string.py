from Crypto.Util.strxor import strxor

import sys

if len(sys.argv) != 3:
    print("Usage: $ python3 script_name.py string1 string2")
    sys.exit(1)

a = sys.argv[1]
b = sys.argv[2]

print(strxor(a.encode(), b.encode()))
