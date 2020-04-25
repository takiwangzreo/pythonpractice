from bs4 import BeautifulSoup
import requests
url = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
soup = BeautifulSoup(url.text,"html.parser")
words = soup.select('tbody')
for word in words:
    print(word.text)