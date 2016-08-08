from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# --click by link text--
driver = webdriver.Firefox()
driver.get('http://google.com/')

elm = driver.find_element_by_link_text('O nas')
driver.implicitly_wait(5)
elm.click()
