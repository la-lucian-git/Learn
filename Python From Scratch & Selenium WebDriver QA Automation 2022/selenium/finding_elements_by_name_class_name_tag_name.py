from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

# By class name
product = driver.find_element(By.CLASS_NAME, 'product')
products = driver.find_elements(By.CLASS_NAME, 'product')

# By name
order_by = driver.find_element(By.NAME, 'orderby')

# By tag
all_links = driver.find_elements(By.TAG_NAME, 'a')

print(product)
print("-" * 75)
print(products)
print("-" * 75)
print(order_by.text)
print("-" * 75)
print(f"Number of all links[a tag] is: {len(all_links)}")
