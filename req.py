import requests
from bs4 import BeautifulSoup

session = requests.Session()
session.post('http://workspace.nw/#', {
     'username': 'Basil12',
     'password': '',
     'remember': 1,
})

res = requests.get('http://workspace.nw/index.php?do=static&page=nwlink#')
#print(res)

print(res.headers['content-type'])
#print(res.text)
#data = unicode(res.text, 'utf-8')

#print(data)
print(res.text.encode('utf-8'))
#print(res.text.encode('utf-8'))
print(type(res.text))