#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
count = 0
base_url = "https://zhidao.baidu.com"

s = requests.session()


def http_get_content_cookie(url):
    global count
    if count >= 15:
        count = 0
        resetCookie()
    req = s.get(url, headers=headers)
    count += 1
    return encode_utf_8(req)


# 不重置cookie
def http_get_content(url):
    req = requests.get(url, headers=headers)
    return encode_utf_8(req)


def http_get_json(url):
    req = requests.get(url, headers=headers)
    return req.json()


def http_post_json(url, data):
    req = requests.post(url, headers=headers, data=data)
    return req.json()


def encode_utf_8(req):
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = req.apparent_encoding
    # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    global encode_content
    encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
    return req, encode_content


# main 方法

def resetCookie():
    s.cookies.clear()
    s.get(base_url, headers=headers)
    print("重置cookie")


if __name__ == "__main__":
    req, str = http_get_content_cookie(
        "https://zhidao.baidu.com/question/1946854105289289668.html?sort=11&rn=5&pn=10#wgt-answers", {})
    print(str)
