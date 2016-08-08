import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://google.com/')

def searching(key):
    search = browser.find_element_by_id("lst-ib")
    search.send_keys(key)
    search.send_keys(Keys.RETURN)
    time.sleep(6)
    search.clear()
    time.sleep(2)

searching("python 2")
searching("Python 3")
searching("elefant")

browser.close()
