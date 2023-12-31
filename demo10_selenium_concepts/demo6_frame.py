import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://netbanking.hdfcbank.com/netbanking/")


# switch using index - option 1
# driver.switch_to.frame(0)

#switch using name or id as a String - - option 2
# driver.switch_to.frame("login_page")

#switch using xpath - - option 3
driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))

#enter userid as john123
driver.find_element(By.NAME,"fldLoginUserId").send_keys("hello123")

#click on continue
driver.find_element(By.PARTIAL_LINK_TEXT,"CONTINUE").click()

#switch to main html
driver.switch_to.default_content()

time.sleep(5)
driver.quit()