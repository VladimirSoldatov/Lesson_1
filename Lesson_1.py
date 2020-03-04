
import requests
import json
print('Hello world')
url = 'https://cbr-xml-daily.ru/dayly.js'
response = requests.get(url)
data = json.loads(response.text)
print(data)