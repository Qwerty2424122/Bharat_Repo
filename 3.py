from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('C:/Users/New User/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(11)
driver.maximize_window()
driver.get("http://www.fb.com")
driver.find_element_by_name("email").send_keys("test12@test.com")
driver.find_element_by_name("pass").send_keys("test12")
driver.find_element_by_id("u_0_2").click()

driver.implicitly_wait(15)
driver.find_element_by_link_text("Account Settings").click()
driver.find_element_by_link_text("Log Out").click()



