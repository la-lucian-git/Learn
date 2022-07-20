from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Example 1 - Login Attempt:
driver.get('http://demostore.supersqa.com/my-account')

user_name = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
submit_button = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3)'
                                                     ' > button')

user_name.send_keys('demo')
password.send_keys('demo')
submit_button.click()

# Example 2 - Search in store, hit key
driver.get('http://demostore.supersqa.com')
search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('hoodie')
# Just to demo
time.sleep(3)
search_field.send_keys(Keys.ENTER)

# Example 3
driver.get('http://demostore.supersqa.com/my-account')
user_name = driver.find_element(By.ID, 'username')

user_name.send_keys('demo')
time.sleep(3)
user_name.send_keys(Keys.TAB)


