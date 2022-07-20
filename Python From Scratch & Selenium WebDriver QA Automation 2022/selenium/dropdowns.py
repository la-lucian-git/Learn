from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pdb
import time

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Duke/Documents/Learn/Python%20From%20Scratch%20&%20Selenium%20WebDriver%20QA%20Automation%'
           '202022/selenium/drop_down_example.html')

# Variant 1
my_dropdown = driver.find_element(By.ID, 'age-range-select')
dropdown_obj = Select(my_dropdown)
dropdown_obj.select_by_index(3)
time.sleep(1.5)
dropdown_obj.select_by_value('21-40')
time.sleep(1.5)

all_options = dropdown_obj.options
for option in all_options:
    print(option.text)
# pdb.set_trace()

# Variant 2
time.sleep(3)
dropdown_button = driver.find_element(By.ID, 'dropdownMenuButton')
dropdown_button.click()
time.sleep(1)  # Wait for element to be visible
my_option = driver.find_element(By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[2]/a')
my_option.click()

