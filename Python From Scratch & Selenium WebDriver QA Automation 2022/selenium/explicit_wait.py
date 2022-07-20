"""
Demo page: page_with_slow_image.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('file:///C:/Users/Duke/Documents/Learn/Python%20From%20Scratch%20&%20Selenium%20WebDriver%20QA%20Automation%'
           '202022/selenium/page_with_slow_image.html')

# my_image = driver.find_element(By.ID, 'the_slow_image')
# my_image = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, 'the_slow_image')))
my_image = wait.until(ec.visibility_of_element_located((By.ID, 'the_slow_image')))

# if my_image.is_displayed():
#     print("Pass!")
# else:
#     print("Failed!")

print('-' * 75)
print("Found image")
print('-' * 75)
