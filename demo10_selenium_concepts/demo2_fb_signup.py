import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.facebook.com/")   #wait for page load to complete

#find_element will check for presence of element in 0.5s
#click on create new account
driver.find_element(By.LINK_TEXT,"Create new account").click()

#enter firstname as john
driver.find_element(By.NAME,"firstname").send_keys("john")

#enter lastname as wick
driver.find_element(By.NAME,"lastname").send_keys("wick")

#enter password as welcome123
driver.find_element(By.ID,"password_step_input").send_keys("welcom123")

#click on radio button - Custom
driver.find_element(By.XPATH,"//input[@value='-1']").click()

#dob - 20 Dec 2000
select_day=Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text("20")

select_month=Select(driver.find_element(By.ID,"month"))
select_month.select_by_visible_text("Dec")
# select_month.select_by_value("12")
# select_month.select_by_index(11)

#select year as 2000
select_year=Select(driver.find_element(By.ID,"year"))
select_year.select_by_visible_text("2000")

driver.find_element(By.NAME,"websubmit").click()
time.sleep(5)
driver.quit()