""" Mouse and keyboard actions using selenium"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://nasscom.in/about-us/contact-us")
actions=ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Membership']")).perform()
driver.find_element(By.XPATH,"//a[text()='Members Listing']").click()
time.sleep(5)
driver.quit()