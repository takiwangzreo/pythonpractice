from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html_youtube = request.urlopen("https://www.youtube.com/watch?v=iHUnUHA5hek&list=RDBNpcNE2-c6g&index=2")
html = html_youtube.read().decode('utf-8')
data = BeautifulSoup(html,'html.parser')
data2 = data
print(data2)

