# _*_ coding:utf-8 _*_

import requests

resp = requests.get('http://xlzd.me')
print (resp.status_code)