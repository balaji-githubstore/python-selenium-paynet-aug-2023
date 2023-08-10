import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(30)

driver.get("https://www.facebook.com/")

wait=WebDriverWait(driver,40)

# driver.find_element(By.LINK_TEXT,"Create new account").click()
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Create new account"))).click()

# driver.find_element(By.NAME,"firstname").send_keys("john")
wait.until(expected_conditions.visibility_of_element_located((By.NAME,"firstname"))).send_keys("john")

#enter lastname as wick
# driver.find_element(By.NAME,"lastname").send_keys("wick")
wait.until(expected_conditions.visibility_of_element_located((By.NAME,"lastname"))).send_keys("john")

print(driver.title)
driver.quit()