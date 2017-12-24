import re
import subprocess

with open('jay.txt', 'r', encoding='utf8') as file:
    text = file.read()

pics = re.findall('<img.+?src\s*=\s*"(.+?)">', text)
# print(pics)
for url in pics:
    subprocess.call(('wget %s -P pics' % url).split(' '))

