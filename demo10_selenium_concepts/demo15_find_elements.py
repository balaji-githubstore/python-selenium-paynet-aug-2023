import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://google.com")

elements=driver.find_elements(By.XPATH,"//a")
print(elements)

print(len(elements))

# elements[1].click()
for i in range(0,len(elements)):
    print(elements[i].text)
    print(elements[i].get_attribute("href"))
    print(50*"-")

time.sleep(5)
driver.quit()