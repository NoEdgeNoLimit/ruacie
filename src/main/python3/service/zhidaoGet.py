#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
from libs.utils import HttpRequestUtil
from libs.utils import DataUtil
from bs4 import BeautifulSoup
from urllib import parse
import time
from collections import Counter
import datetime
import json
import logging

logging.basicConfig(filename='../LOG/' + __name__ + '.log',
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.INFO, filemode='a',
                    datefmt='%Y-%m-%d%I:%M:%S %p')

# ===============基础数据区================start
# https://zhidao.baidu.com/question/1499709145322055299.html
base_url = 'https://zhidao.baidu.com/question/'


# ===============基础数据区================end


# 入参知道页面 返回问题列表
def main():
    url_ids = DataUtil.get_url_id_by_data()


# 根据urlids 获取jsons
def get_jsons_by_url_ids(url_ids):
    jsons = []
    for id in url_ids:
        jsons.append(get_json_by_url_id(id))
    return jsons


# 根据urlid 获取json
def get_json_by_url_id(url_id):
    url_str = '%s%s%s' % (base_url, url_id, ".html")
    qajson = {
        'title': '',
        'answer': []
    }
    print(url_str)
    _, str = HttpRequestUtil.http_get_content_cookie(url_str)
    soup_html = BeautifulSoup(str, 'html.parser')
    soup_html = soup_html.select('#qb-content')[0]
    qajson['title'] = soup_html.select('.ask-title')[0].get_text()
    soup_divs = soup_html.find_all(accuse="aContent")
    print(len(soup_divs))

    for div in soup_divs:
        div.div.extract()
        qajson['answer'].append(div.get_text().strip())
    return qajson

def translate_a(str):
    str = str.replace('《','<')
    str = str.replace('》','>')
    #str = str.replace('“','<')
    #str = str.replace('”','>')
    #str = str.replace('"','')
    #str = str.replace('"','')

    str = parse.quote(str)
    print(str)
    url='https://translate.google.com/translate_a/single?client=gtx&sl=zh-CN&tl=en&dt=t&q='+str
    # url='https://translate.google.com/translate_a/single'
    # data = {
    #     'client':'gtx',
    #     'sl':'zh-CN',
    #     'tl':'en',
    #     'dt':'t',
    #     'q':qajson
    # }
    print(url)
    json_str = HttpRequestUtil.http_get_json(url)

    entext =[]

    for text in json_str[0]:
        entext.append(text[0])
    return ''.join(entext)

def json_cut_text(qajson):
    qajson['title'] = translate_a(qajson['title'] )
    answer_new = []
    for anstr in qajson['answer']:
        anstr_tmp =[]
        textArr = cut_text(anstr,2048)
        for text in textArr:
            anstr_tmp.append(translate_a(text))
        answer_new.append(''.join(anstr_tmp))
    qajson['answer'] = answer_new
    print(json.dumps(qajson))

def cut_text(text,lenth):
    textArr = re.findall('.{'+str(lenth)+'}', text)
    textArr.append(text[(len(textArr)*lenth):])
    return textArr

if __name__ == "__main__":
    # main()
    for num in range(1,2):
        qajson = get_json_by_url_id(989325443415030459)
        json_cut_text(qajson)

    #translate_a(qajson)

