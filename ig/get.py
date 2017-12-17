import requests
import re
import subprocess

res = requests.get('https://www.instagram.com/airi_kijima/')
pics = re.findall('https://[^"]+_n\.jpg', res.text)
for url in pics:
    subprocess.call(('wget %s -P pics' % url).split(' '))

