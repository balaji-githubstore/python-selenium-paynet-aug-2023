from selenium import webdriver

d=webdriver.Edge()
d1=webdriver.Edge()

d.get("https://www.facebook.com/")
d1.get("https://google.com")
print(d.title)
print(d.current_url)

print(d.page_source)

d.quit()

d1.quit()
