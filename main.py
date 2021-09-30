#!python3

import requests
import json

x = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/hello')

y = json.dumps(x.text)

word = json.loads(y)
print(word[0])
