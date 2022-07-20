"""
Demo page: page_with_slow_image.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('file:///C:/Users/Duke/Documents/Learn/Python%20From%20Scratch%20&%20Selenium%20WebDriver%20QA%20Automation%'
           '202022/selenium/page_with_slow_image.html')

my_image = driver.find_element(By.ID, 'the_slow_image')
my_image.click()
print('-' * 75)
print("Found image.")
print('-' * 75)
