import requests
import sys
from tqdm import tqdm

http_stat_200 = 200
http_stat_302 = 302

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <url.txt>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "r") as file:
        raw_urls = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"Error: file '{file_path}' not found.")
    sys.exit(1)
    
f = open("http-status-out.txt", "a")

for base_url in tqdm(raw_urls, desc="Scanning URLs"):
    https = f"https://{base_url}" if not base_url.startswith("http") else base_url
    http = f"http://{base_url}" if not base_url.startswith("http") else base_url

    for url in [https, http]:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == http_stat_200 or response.status_code == http_stat_302:
                f.write(f"{url} ### {response.status_code}\n")
                # print(f"{url}: HTTP {response.status_code}")
            break
        except requests.exceptions.RequestException:
            continue

    # else:
    #     print(f"{base_url}: No valid connection with http or https.")

f.close()
