import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
browser.get('http://archive.dojotoolkit.org/nightly/checkout/dijit/tests/form/test_CheckBox.html')

for i in range(20):
    try:
        browser.find_element_by_xpath(".//*[contains(text(), 'cb7: normal checkbox.')]").click()
        print "element found and clicked ^^)"
        break
    except NoSuchElementException as e:
        print "retry"
        time.sleep(1)
else:
    print "Test Failed"

browser.close()
