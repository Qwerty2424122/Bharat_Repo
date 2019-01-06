from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.python.org")



driver.implicitly_wait(15)

elem = driver.find_element_by_name("q")

elem.clear()
elem.send_keys("Bharat")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

driver.close()


