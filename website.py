# robot for python
# selenium is a robot from python , webdriver is from selenium
from selenium import webdriver
# different network has different driver , you should download it on website
driver = webdriver.Chrome('/Users/wangweiteng/Downloads/chromedriver-2')
# mac has problem on open website screen but window doesn't have
driver.fullscreen_window()
driver.get('http://youtube.com')
# some place ban automatic so sometime will doesnt' work
driver.find_element_by_id()
#quit use to close the chrome , close use to close pagination
driver.quit()
