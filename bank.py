from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = request.urlopen("https://rate.bot.com.tw/xrt?Lang=zh-TW")
print(url.read().decode('utf-8'))


