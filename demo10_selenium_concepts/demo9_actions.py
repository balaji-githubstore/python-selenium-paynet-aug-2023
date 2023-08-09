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

#mouse hover on Become a member
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Become a Member']")).perform()

driver.find_element(By.XPATH,"//a[text()='Membership Benefits']").click()
#click on element - click to apply online

#TEXT FOR LINK TEXT OR PARTIAL LINK TEXT - ADD BASED ON UI FONT
# driver.find_element(By.LINK_TEXT,"CLICK TO APPLY ONLINE").click()

driver.find_element(By.XPATH,"//a[text()='Click to Apply Online']").click()
time.sleep(5)
driver.quit()
