import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
browser.get('http://google.com')

time.sleep(2)
browser.set_window_size(1024,768)

time.sleep(2)
print "the size is", browser.get_window_size()

time.sleep(2)
browser.maximize_window()
print "the size is", browser.get_window_size()

time.sleep(2)
browser.close()
