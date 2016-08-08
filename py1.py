from selenium import webdriver

driver = webdriver.Firefox() #.Chrome()
driver.get('http://google.com')

try:
    driver.find_element_by_class_name('gb_P')
    print 'Test Pass: CLASS FOUND'

except Exception as e:
    print 'Exception found',format(e)

driver.close()
