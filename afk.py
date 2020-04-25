from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
afk_html = request.urlopen('https://m.wanyx.com/shoujigonglue/360969.html')
data = afk_html.read().decode('utf-8')
soup = BeautifulSoup(data,'html.parser')
tag_name = 'p'
afk = soup.select(tag_name)
for i in afk:
    print(i)