import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://paynet.co.in/")

#click on sign up
driver.find_element(By.XPATH,"//span[contains(text(),'Sign up')]").click()

driver.switch_to.window(driver.window_handles[1])
#enter full name
driver.find_element(By.ID,"name").send_keys("Balaji Dinakaran")

time.sleep(5)
driver.quit()
