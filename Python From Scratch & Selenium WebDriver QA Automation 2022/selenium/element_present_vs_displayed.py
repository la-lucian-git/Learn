"""
Demo pages: present_vs_displayed.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = 'file:///C:/Users/Duke/Documents/Learn/Python%20From%20Scratch%20&%20Selenium%20WebDriver%20QA%20Automation%' \
      '202022/selenium/present_vs_displayed.html'
driver.get(url)

my_button_1 = driver.find_element(By.ID, 'btn1')
my_button_2 = driver.find_element(By.ID, 'btn2')
my_button_3 = driver.find_element(By.ID, 'btn3')
my_button_4 = driver.find_element(By.ID, 'btn4')

print('-' * 75)
print(f"My button 1 text is: {my_button_1.text}.")


print('-' * 75)
print(f"My button 2 text is: {my_button_2.text}.")


print('-' * 75)
print(f"My button 3 text is: {my_button_3.text}.")

# Empty string button not visible but present
print('-' * 75)
print(f"My button 4 text is: {my_button_4.text}.")
# pdb.set_trace()

print('-' * 75)
if my_button_4.is_displayed():
    my_button_4.click()
else:
    raise Exception("Button 4 is not displayed!")



