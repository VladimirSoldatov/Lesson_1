
import requests
import json
print('Hello world')
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
print(data)