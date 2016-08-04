

import requests
import json
import sqlite3



url = 'https://sj.teambookapp.com/api/users?per_page=1000'
r = requests.get(url, headers={'Authorization': 'Token token=56e4d2697115a9bcda5c3b28e6076f3c'})
value= json.loads(r.text)
for row in value:
	print (row)

with open("Output.txt", "w") as jsontext:
    jsontext.write((value))











