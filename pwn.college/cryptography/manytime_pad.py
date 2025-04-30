from Crypto.Util.strxor import strxor
import sys

if len(sys.argv) != 2:
    print("Usage: $ python3 script_name.py ciphertext")
    sys.exit(1)
    
flag_ciphertext_hex = sys.argv[1]
flag_ciphertext = bytes.fromhex(flag_ciphertext_hex)

zero_plaintext = b"\x00" * len(flag_ciphertext)
print(f"String for the challenge:\n{zero_plaintext.hex()}")

key_hex = input("Ciphertext from the challenge (hex): ")
key = bytes.fromhex(key_hex)

flag = strxor(flag_ciphertext, key)
print(flag.decode())
