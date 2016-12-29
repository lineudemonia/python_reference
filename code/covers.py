
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from threading import Thread
import queue 

_session = requests.session()
url_base = 'URL WAS HERE'
page = '1'
for page in range(0,100):
    print(page)
    r = _session.get(url_base + str(page))
    print(r)
    soup = BeautifulSoup(r.content)
    box = soup.find_all('div', class_='item')
    av = []
    for i in range(len(box)):
        av += [[box[i].div.img['src'], box[i].div.img['title'],box[i].find('date').text]]
    DMM_session = requests.session()
    for i in av:
        img = DMM_session.get(i[0].replace('ps','pl'),stream=True)
        with open('covers/'+i[2]+"__"+i[1][:40].replace('[^\w]','')+'.jpg','wb') as f:
            f.write(img.content)
            f.close()