
import requests
import urllib.request
from lxml import etree
url = "http://www.baidu.com"
con = requests.get(url).text
content = urllib.request.urlopen(url).read()
content = content.decode('utf-8')
html = etree.HTML(content)
title = html.xpath('//title/text()')
print(title)
input("Press <enter>")

# pyinstaller -F main.py