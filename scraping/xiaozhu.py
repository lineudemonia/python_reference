# _*_ encoding: utf-8 _*_

from bs4 import BeautifulSoup
import requests

first_url = 'http://bj.xiaozhu.com/xicheng-305-9999yuan-duanzufang-9/?startDate=2016-07-01&endDate=2016-07-04'
urls = ['http://bj.xiaozhu.com/xicheng-duanzufang-p{}-8/?startDate=2016-07-01&endDate=2016-07-04'.format(str(i)) for i in range(1,9)]



headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

data = []	

def get_housing(url):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text, 'lxml')
	# print(soup)
	# 成功连接
	info = []
	descs = soup.select('div.result_btm_con.lodgeunitname > div > a > span')
	prices = soup.select('div.result_btm_con.lodgeunitname > span.result_price > i')
	addresses = soup.select('div.result_btm_con.lodgeunitname > div > em')

	for desc, price, address in zip(descs, prices, addresses):
		data = {
			'desc': desc.get_text(),
			'price': price.get_text(),
			'address': list(address.stripped_strings)
		}
		info.append(data)


	for item in info:
		item['address'][0] = item['address'][0][:2]
		if len(item['address']) < 3: continue
		item['address'][2] = item['address'][2].strip('-').strip()
		
	return info	



for url in urls:
	data += get_housing(url)

total = 0
for item in data:
	print(item)
	total+=int(item['price'])

average = total / len(data)
print ('总房数:', len(data))
print ('平均房价:', average)
