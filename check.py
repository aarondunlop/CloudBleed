#!/bin/python
import os
from io import BytesIO
from urllib2 import urlopen
from zipfile import ZipFile

password_file='/tmp/password.csv'
site_file='/tmp/list.csv'
site_list='https://github.com/pirate/sites-using-cloudflare/archive/master.zip'
pw_list = []
sites = []

if not os.path.isfile(site_file):
    urlobj = urlopen(site_list)
    with ZipFile(BytesIO(urlobj.read())) as zf:
        zf.extract('sites-using-cloudflare-master/sorted_unique_cf.txt', '/tmp/')
        os.rename('/tmp/sites-using-cloudflare-master/sorted_unique_cf.txt', '/tmp/list.csv')

with open(site_file, 'r') as f:
    for line in f.readlines():
        sites.append(line.rstrip())
f.close()

with open(password_file, 'r') as f:
    for line in f.readlines():
        newline=line.split(',')[0].replace('http://','').replace('www.', '').lower().rstrip()
        pw_list.append(newline)
f.close()

result=sorted(list(set(pw_list) & set(sites)))
print(result)
