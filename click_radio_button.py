import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
browser.get('https://www.zkoss.org/zkdemo/input/radio_button')

for i in browser.find_elements_by_xpath('//*[@type=\'radio\']'):
    i.click()

time.sleep(6)

browser.close()
