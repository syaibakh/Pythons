import requests

r = requests.get('https://randomuser.me/api/?format=xml')
print(r.text)