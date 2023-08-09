import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://smallpdf.com/pdf-to-word")

driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:\\Mine\\Balaji-Profile_2023_1.pdf")

time.sleep(5)
driver.quit()