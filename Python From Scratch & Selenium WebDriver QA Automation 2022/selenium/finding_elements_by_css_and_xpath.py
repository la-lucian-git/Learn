import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart > li:nth-child(1) > a')
time.sleep(3)
cart.click()

my_account = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
time.sleep(3)
my_account.click()

time.sleep(3)
driver.quit()
