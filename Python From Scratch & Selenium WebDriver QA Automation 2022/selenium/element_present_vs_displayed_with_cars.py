"""
Demo pages: present_vs_displayed_example_with_cars.html
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

url = 'file:///C:/Users/Duke/Documents/Learn/Python%20From%20Scratch%20&%20Selenium%20WebDriver%20QA%20Automation%' \
      '202022/selenium/present_vs_visible_example_with_cars.html'
driver.get(url)

# Element present but not displayed
series_6 = driver.find_element(By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')
# series_6.click() # Error: element not intractable

# Element present but not displayed
series_6_presence = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                              '#bmw-models > input[type=checkbox]:nth-child(7)')))

# Commenting the line below will cause the script to fail because 6-series will not be visible
driver.find_element(By.ID, 'bmw').click()
series_6_clickable = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                            '#bmw-models > input[type=checkbox]:nth-child(7)')))
