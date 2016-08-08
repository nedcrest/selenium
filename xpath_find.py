from selenium import webdriver
import time
#http://google.com/


# driver = webdriver.Firefox()
# driver.get('http://google.com/')
#
# ids = driver.find_elements_by_xpath('//*[@href]')
#
# for ii in ids:
#     print ii.get_attribute('href')
#
# time.sleep(4)
# driver.close()

# --find link by xpath class--
driver = webdriver.Firefox()
driver.get('http://google.com/')

try:
    driver.find_elements_by_xpath("//a[@class='_Gs']")
    print "TEst passed: link text class by XPath found"

except Exception as e:
    print "Exception found", format(e)

driver.close()

# --Get all Class elements XPath--
# driver = webdriver.Firefox()
# driver.get('http://google.com/')
#
# id = driver.find_elements_by_xpath('//*[@class]')
#
# for i in id:
#     print i.get_attribute('class')
#
# driver.close()
