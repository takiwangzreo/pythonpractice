import urllib.request as req
web = req.urlopen("https://rate.bot.com.tw/xrt?Lang=zh-TW")
rate = web.read()
print(rate)