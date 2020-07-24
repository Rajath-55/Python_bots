from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = '/home/rajath/Desktop/chromedriver'
driver = webdriver.Chrome(PATH)
URL = 'https://www.amazon.in'

driver.get(URL)
print(driver.title)
# print(driver.page_source)

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("iPhone 11")
search.send_keys(Keys.RETURN)
time.sleep(10)
try:
    spans = driver.find_elements_by_name('span')
    print(spans)
except:
    driver.quit()



