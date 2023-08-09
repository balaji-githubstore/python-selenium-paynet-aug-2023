import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.citibank.co.in/ssjsps/forgetuseridmidssi.jsp")

#select credit card
driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

driver.find_element(By.ID,"citiCard1").send_keys("7887")
driver.find_element(By.CSS_SELECTOR,"#citiCard2").send_keys("7887")
driver.find_element(By.CSS_SELECTOR,"input[name='citiCard3']").send_keys("7887")
driver.find_element(By.CSS_SELECTOR,"[name='citiCard4']").send_keys("7887")

#20 Dec 2000

#approach 1 - not working
# driver.find_element(By.ID,"bill-date-long").send_keys("20/12/2000")

#approach 2 - automate in the same way manual testing is done
driver.find_element(By.ID,"bill-date-long").click()

select_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
select_year.select_by_visible_text("2000")

select_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
select_month.select_by_visible_text("Dec")

driver.find_element(By.LINK_TEXT,"20").click()

#approach 3 js - next demo 13
time.sleep(5)
driver.quit()