#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	THIS LOOKS AT QINGDAO's WEBSITE."""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# GET BS OBJECT OF PAGE
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

# GET ALL INTERNAL LINKS
def getInternalLinks(bsObj, includeUrl):
	#找出所有以"/"开头的链接
	internalLinks = []
	for link in bsObj.find_all("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] != None and link.attrs["href"] not in internalLinks:
			internalLinks.append(link.attrs["href"])
	return internalLinks

# GET ALL EXTERNAL LINKS	
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = ()
	#找出所有http开头并且不含当前url的链接
	for link in bsObj.find_all("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs["href"] != None and link.attrs["href"] not in externalLinks:
			externalLinks.append(link.attrs["href"])
	return externalLinks
		
# HELPER FUNCTION
def splitAddress(address):
	addressParts = address.replace("http//", "").split("/")
	return addressParts

get Random

allExtLinks = set()
allIntLinks = set()

url = "http://www.qingdao.gov.cn/n172/"
bsObj = getPage(url)
internalLinks = getInternalLinks(bsObj, splitAddress(url)[0])
for link in internalLinks:
	if link not in allIntLinks:
		print("Next link is:", link)
		allIntLinks.add(link)

print(allIntLinks)		