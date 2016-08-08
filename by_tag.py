from selenium import webdriver

driver = webdriver.Firefox() #.Chrome()
driver.get('http://google.com')

try:
    driver.find_element_by_tag_name('form')
    print 'Test Pass: TAG NAME FOUND'

except Exception as e:
    print 'Exception found',format(e)
