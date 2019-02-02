#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#https://translate.google.cn/translate_a/single?client=gtx&sl=auto&dj=1&ie=UTF-8&oe=UTF-8&q=test
#https://translate.google.com/translate_a/single?client=gtx&sl=zh-CN&tl=en&dt=t&q=%E5%A4%A7%E5%AE%B6nihaohello%E4%B8%AD%E5%9B%BD%E5%B9%B4
#[[["Everyone nihaohello chinese year","大家nihaohello中国年",null,null,3]],null,"zh-CN"]
import re
from libs.utils import HttpRequestUtil
from libs.utils import DataUtil
from bs4 import BeautifulSoup
from urllib import parse
import time
from collections import Counter

import logging

logging.basicConfig(filename='../LOG/save.log',
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.INFO, filemode='a',
                    datefmt='%Y-%m-%d%I:%M:%S %p')

# ===============基础数据区================start
cid_set = {
    'https://zhidao.baidu.com/list?cid=114',  # 心里分析
    'https://zhidao.baidu.com/list?cid=115',  # 医疗卫生
    'https://zhidao.baidu.com/list?cid=103',  # 法律法规
    'https://zhidao.baidu.com/list?cid=104',  # 社会民生
    'https://zhidao.baidu.com/list?cid=105',  # 科学教育
    'https://zhidao.baidu.com/list?cid=109',  # 电子数码
    'https://zhidao.baidu.com/list?cid=110',  # 电脑网络
    'https://zhidao.baidu.com/list?cid=106101',  # 健康生活-烹饪
    'https://zhidao.baidu.com/list?cid=106104',  # 健康生活-烹饪
    'https://zhidao.baidu.com/list?cid=106105',  # 健康生活-烹饪
    'https://zhidao.baidu.com/list?cid=106106',  # 健康生活-烹饪
    'https://zhidao.baidu.com/list?cid=106106',  # 体育运动-武术
    'https://zhidao.baidu.com/list?cid=108102',  # 文化艺术-工艺品
    'https://zhidao.baidu.com/list?cid=108106',  # 文化艺术-时尚
    'https://zhidao.baidu.com/list?cid=111103',  # 娱乐休闲-收藏
    'https://zhidao.baidu.com/list?cid=111104',  # 娱乐休闲-旅游
}
# 存储的关键词列表
global_key_word_set = set()
global_key_word_list = []
# 获取问题链接正则表达式
zd_re_link = re.compile("zhidao\.baidu\.com/question/\d+\.html")
zd_re_link_num = re.compile('.+zhidao\.baidu\.com/question/(\d+)\.html')
# 首页地址
index_url = "https://zhidao.baidu.com/"
cookies = {}
# url id
url_id_set = set()


# ===============基础数据区================end


# 入参知道页面 返回问题列表
def main():
    index_hot_key = get_index_hot_url()
    global_key_word_set.update(set(index_hot_key))
    for url in cid_set:
        global_key_word_set.update(set(get_index_cid_url(url)))
        # time.sleep(0.5)
    # global_key_word_set.update(set(get_index_cid_url("https://zhidao.baidu.com/list?cid=105")))
    # print(global_key_word_set)
    print("检索到" + global_key_word_set.__len__().__str__() + "个关键词")
    for key_word in global_key_word_set:
        serch_key_word_page(key_word)
    print("获取到" + url_id_set.__len__().__str__() + "个url_id")
    # 保存抓取id
    DataUtil.save_url_id_to_data(url_id_set)


# 获取首页热点问题
def get_index_hot_url():
    _, str = HttpRequestUtil.http_get_content_cookie(index_url)
    soup_html = BeautifulSoup(str, 'html.parser')
    get_key_word(soup_html)
    return get_key_word(soup_html)


# 获取类目cid 返回关键词
def get_index_cid_url(cid_url):
    default_url = '%s%s' % (cid_url, '&type=default')
    highScore_url = '%s%s' % (cid_url, '&type=highScore')
    hot_url = '%s%s' % (cid_url, '&type=hot')
    feed_url = '%s%s' % (cid_url, '&type=feed')
    list_url = [default_url, highScore_url, hot_url, feed_url]

    key_word_list = []
    for url in list_url:
        print(url)
        _, str = HttpRequestUtil.http_get_content_cookie(url)
        soup_html = BeautifulSoup(str, 'html.parser')
        key_word_list.extend(get_key_word(soup_html))
    return key_word_list


def get_key_word(soup_html):
    key_word_list = []
    for tag in soup_html.find_all(href=zd_re_link):
        if tag.string != None:
            # 替换换行符
            key_word_list.append(tag.string.replace("\n", ""))
    print(key_word_list.__len__())
    return key_word_list


# 自动翻页
def serch_key_word_page(key_word):
    # %E8%BF%99%E7%A7%8D%E5%9B%BE%E7%89%87%E7%94%A8%E6%89%8B%E6%9C%BA%E6%80%8E%E4%B9%88%E5%88%B6%E4%BD%9C
    base_url = "https://zhidao.baidu.com/search?word="
    key_word = parse.quote(key_word)
    url = '%s%s' % (base_url, key_word)
    # 自动翻页 5页.
    for num in range(0, 5):
        try:
            tmp_url = ('%s%s%s' % (url, "&pn=", (num * 10)))
            serch_key_word(tmp_url)
        except:
            logging.exception(url + '异常' + num.__str__())  # exception代表打印时也会打印出系统错误提示语句


# 自动搜索关键词
def serch_key_word(url):
    _, str = HttpRequestUtil.http_get_content_cookie(url)
    soup_html = BeautifulSoup(str, 'html.parser')
    # soup_html = soup_html.find(id="wgt-list")
    soup_html = soup_html.find_all(class_='dl')
    # 过滤赞大于1的标签
    for tag in soup_html:
        temtag = tag.find(class_='ml-10 f-black')
        if temtag:
            num = temtag.get_text().strip()
            print(int(num))
            if int(num) >= 1:
                a_tag = tag.find(href=zd_re_link)
                print(a_tag['href'])
                # print(re.match(zd_re_link_num, a_tag['href']).group(1))
                url_id_set.add(re.match(zd_re_link_num, a_tag['href']).group(1))

if __name__ == "__main__":
    #main()
    serch_key_word_page('《啥是佩奇》好在哪里?')
