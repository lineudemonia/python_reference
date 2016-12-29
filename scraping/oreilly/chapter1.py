'''
CRAWLS A WEBSITE WITH ERROR HANDLING
'''

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getPage(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html, "lxml")
	except HTTPError as e:
		return None
	return bsObj			

def getTitle(bsObj):
	return bsObj.body.h1

def getNames(bsObj):
	return bsObj.findAll("")

def getLinks(bsObj):
	global pages
	try:
		print(bsObj.h1.get_text())
	except AttributeError:
		print("Some of the attributes are missing")	

url = "https://www.cbinsights.com/search/deals/?isVCBacked=true&invStages=Seed%20%2F%20Angel%2CSeries%20A%2CSeries%20B%2CSeries%20C&inds=61%2C147&limit=25&offset=0&displayType=table"
bsObj = getPage(url)
if bsObj == None:
	print("Title couldnt be found")
else:
	print(bsObj)

	# print(links)			

	# print(len(links))
	# courses = bsObj.find_all("data-course-summary", id=re.compile("(nd)(0-9)*"))
	# for course in courses:
	# 	print(course.attrs)
	# nameList = []
	# for name in getNames(bsObj):
	# 	# Get text removes all the tags in the found list
	# 	if name.get_text() not in nameList and name.get_text() != "":
	# 		nameList.append(name.get_text())
	# print(nameList)			
	#print(getTitle(bsObj))


	''' Get level 1 sub info under <table id="giftList">

	for child in bsObj.find("table", {"id":"giftList"}).children:
		print(child)

	'''
	
	''' Sibling test
	for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
		print(sibling)
	'''
	
	'''
	Find all attributes in tags

	images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})	
	for image in images:
		print(image.attrs)
	'''

	'''
	FIND ALL VALID WIKI LINKS ON CURRENT PAGE

	pages = []
	for link in bsObj.find("div", {"id": "bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$")):
		#if "href" in link.attrs and link["href"] == re.compile("^(/wiki/)((?!:).)*$"):
		pages.append(link["href"])
	print(len(pages))
	'''
