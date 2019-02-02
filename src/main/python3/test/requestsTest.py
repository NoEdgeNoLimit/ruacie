#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
#请求模块处理
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get("http://ajd.bfgho.com/")
r.encoding='utf-8'
print(r.text)
print(r.status_code)
print(r.url)
print(r.content)
print(r.encoding)
#print(r.json())
print(r.headers)

#上传
#upload_files = {'file': open('report.xls', 'rb')}
#r = requests.post(url, files=upload_files)

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
# 此处分别演示了传递cookie与获取cookie
# 但由于域不同，获取到的cookie列表不会包含元素
print(r.cookies)
