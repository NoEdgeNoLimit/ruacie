from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.baidu.com').text
soup = BeautifulSoup(html, 'html.parser')
list = soup.select('#head .head_wrapper')
for div1 in list:
    print(div1)
    print(type(div1))
    print(div1.div.div.attrs['class'])
