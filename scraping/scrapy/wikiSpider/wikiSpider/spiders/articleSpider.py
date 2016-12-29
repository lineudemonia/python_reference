# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class ArticleSpider(Spider):
	name = "article"
	allowed_domains = ["en.wikipedia.org"]
	start_urls = ["http://en.wikipedia.org/wiki/Main_page", 
					"http://en.wikipedia.org/wiki/python_%28programming_languages%29"]
	# rules = [Rule(SgmlLinkExtractor(allow = ('(/wiki/)((?!:).)*$'),),
	#               callback = "parse_item", follow = True)]					

	def parse(self, response):
		item = Article()
		title = response.xpath('//h1/text()')[0].extract()
		print("Title is:", title)
		item["title"] = title
		return item
