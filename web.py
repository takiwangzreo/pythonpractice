import requests
import ssl
#requests 自帶ssl驗證 ,如果驗證失敗會報錯
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
requests.get('')
