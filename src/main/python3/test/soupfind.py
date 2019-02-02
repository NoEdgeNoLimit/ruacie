#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests

html_str = """<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie<div id ="11"> niaho</div></a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>"""

soup = BeautifulSoup(html_str,'html.parser')
link = soup.a
print(type(soup))
print(link)
print(link.next_sibling.next_sibling)
print("------------------")
for sibling in soup.a.next_siblings:
    print(repr(sibling))
print("------------------")
for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))