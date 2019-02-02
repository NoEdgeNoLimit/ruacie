#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests

req=requests.get('https://zhidao.baidu.com/question/1946854105289289668.html?sort=11&rn=5&pn=10#wgt-answers')
#byte_html=requests.get('https://zhidao.baidu.com/question/1946854105289289668.html?sort=11&rn=5&pn=10#wgt-answers').content
#str_html=str(byte_html,'gbk')
if req.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(req.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = req.apparent_encoding
    # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    global encode_content
    encode_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；

soup_html=BeautifulSoup(encode_content,'html.parser')
print(type(soup_html))
#获取标题
soup_title=soup_html.select('#body .ask-title')[0].string
soup_context=soup_html.select('#body .con.conTemp.conSamp')[0].string
print(soup_title)
print(soup_context)
soup_text = soup_html.select('.bd.answer')
for div1 in soup_text:
    print(div1.find('alog-action="qb-zan-btnbestbox"'))

    #去除无用标签
    div1.div.extract()
    print(div1.get_text())
#    for children in div1.children:
#        print(children)



