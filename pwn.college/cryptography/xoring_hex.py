import sys

if len(sys.argv) != 3:
    print("Usage: $ python3 script_name.py hex1 hex2")
    sys.exit(1)

a = sys.argv[1]
b = sys.argv[2]

a_int = int(a, 16)
b_int = int(b, 16)

print(hex(a_int^b_int))
