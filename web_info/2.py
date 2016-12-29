import urllib
from bs4 import BeautifulSoup

sample = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
real = 'http://python-data.dr-chuck.net/known_by_Prasheeta.html'
times = 7
position = 18

url = real




for time in range(times):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	url = tags[position-1].get('href', None)
	print 'Retrieving:', url
