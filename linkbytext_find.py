from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get('http://google.com/')

## normal
# try:
#     driver.find_element_by_link_text('Gmailll')
#     print "Test passed: Element found."
#
# except Exception as e:
#     print "Test failed: ", format(e)
#
# driver.close()

# --by partial link text--
driver = webdriver.Firefox()
driver.get('http://wikipedia.org/')

try:
    driver.find_element_by_partial_link_text('Term')
    print "Test passed: Element found."

except Exception as e:
    print "Test failed: ", format(e)

driver.close()
