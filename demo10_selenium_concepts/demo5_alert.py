import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://nasscom.in/nasscom-membership")

# Click on calculate fee
driver.find_element(By.ID,"calculate-fee").click()

#wait for alert present
wait=WebDriverWait(driver,40)
wait.until(expected_conditions.alert_is_present())

#get the alert text and print it
actual_alert_text= driver.switch_to.alert.text
print(actual_alert_text)

driver.switch_to.alert.accept()

time.sleep(5)
driver.quit()