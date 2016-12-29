import urllib
from bs4 import BeautifulSoup

sample = 'http://python-data.dr-chuck.net/comments_42.html'
real = 'http://python-data.dr-chuck.net/comments_256916.html'

url = sample
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')
total = 0


for tag in tags:
	total += int(tag.contents[0])

print total


