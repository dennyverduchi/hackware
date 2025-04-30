from binascii import unhexlify
from Crypto.Util.strxor import strxor

import sys

if len(sys.argv) != 3:
    print("Usage: $ python3 script_name.py key flag")
    sys.exit(1)

key = unhexlify(sys.argv[1])
cipher = unhexlify(sys.argv[2])

print(strxor(key, cipher))
