from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = '/home/rajath/Desktop/chromedriver'
driver = webdriver.Chrome(PATH)
URL = 'https://techwithtim.net'


driver.get(URL)
link = driver.find_element_by_link_text('Python Programming')
link.click()
try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials')))
    element.click()
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'sow-button-19310003'))) 
    element.click()
    driver.back()
    driver.back()
    driver.back()
except:
    driver.quit()













































# print(driver.title)
# # print(driver.page_source)

# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)
# try:
#     main = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID, 'main')))
# except:
#     driver.quit()

# print(main.text)
# articles = main.find_elements_by_tag_name('article')
# for article in articles:
#     header = article.find_element_by_class_name("entry-summary")
#     print(header.text)
# time.sleep(20)
# driver.quit()

