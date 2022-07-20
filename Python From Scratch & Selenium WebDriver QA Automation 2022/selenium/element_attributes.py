from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

# Placeholder
search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
placeholder = search_field.get_attribute('placeholder')
if placeholder != 'Search products…':
    raise Exception("Placeholder string not valid! Expected: 'Search products…'")
# pdb.set_trace()

# Selected tab
account = driver.find_element(By.CSS_SELECTOR, 'li.page-item-9')
account.click()

nav_items = driver.find_elements(By.CSS_SELECTOR, 'ul.nav-menu li')
for item in nav_items:
    item_class = item.get_attribute('class')
    if 'current_page_item' in item_class:
        print(f"The selected tab is: {item.text}.")
# pdb.set_trace()
