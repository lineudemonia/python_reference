import json
import urllib


real = 'http://python-data.dr-chuck.net/comments_256917.json'
sample = 'http://python-data.dr-chuck.net/comments_42.json'
url = real

html = urllib.urlopen(url).read()


info = json.loads(html)

#print info

total = 0


for item in info['comments']:
  
  total += item['count']
  
  
print total
'''

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']

'''