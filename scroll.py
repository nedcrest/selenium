from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://wikipedia.org/')

elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(8)
elm.send_keys(Keys.HOME)
time.sleep(3)
driver.close()
