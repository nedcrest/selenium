from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get('http://google.com')

elm = driver.find_element_by_link_text('O nas')
driver.implicitly_wait(10) #or time.sleep(8)
elm.click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(2)
driver.close()
