import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# --refresh page--
driver = webdriver.Firefox()
driver.get('http://google.com')

time.sleep(3)
driver.refresh()
time.sleep(2)
driver.close()
