import sys
import binascii

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str)
    return ascii_str

if len(sys.argv) != 3:
    print("Usage: $ python3 script_name.py hex1 hex2")
    sys.exit(1)

a = sys.argv[1]
b = sys.argv[2]

b_hex = hex(ord(b))

a_int = int(a, 16)
b_int = int(b_hex, 16)
xor = hex(a_int^b_int)

print(hex_to_ascii(xor))
