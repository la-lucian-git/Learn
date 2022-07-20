from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

cart = driver.find_element(By.LINK_TEXT, 'Cart')
account = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')

print('-' * 75)
print(cart.text)
print('-' * 75)
print(account.text)
print('-' * 75)
