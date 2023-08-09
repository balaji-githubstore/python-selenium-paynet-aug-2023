import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.db4free.net/")

#click on phpMyAdmin »
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()

# print(driver.window_handles)
#switch to second tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID,"input_username").send_keys("admin")
#enter password as admin123
driver.find_element(By.ID,"input_password").send_keys("admin")
#click on login
driver.find_element(By.ID,"input_go").click()

#get the error and print in console
actual_error=driver.find_element(By.XPATH,"(//div[@role='alert'])[3]").text
print(actual_error)

driver.close()  #check which tab is closed

#switch to first tab
driver.switch_to.window(driver.window_handles[0])

print(driver.title)

time.sleep(5)
driver.quit()