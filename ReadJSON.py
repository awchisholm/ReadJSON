import requests
url = 'http://127.0.0.1:5000/'
re = requests.get(url)
print(re.json())
