from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from io import StringIO
from PIL import Image
driver = webdriver.Chrome('C:/Users/New User/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("yes it is done")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.set_page_load_timeout(11)


#driver.maximize_window()
screenshot = driver.get_screenshot_as_png();

size = (0, 0, 680, 400)
image = Image.open(StringIO.StringIO(screen))
region = image.crop(size)
region.save('sample_screenshot_3.jpg', 'JPEG', optimize=True, quality=95)
driver.close()