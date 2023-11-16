from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.implicitly_wait(20) # gives an implicit wait for 20 seconds

browser.get('http://inventwithpython.com')
linkElem = browser.find_element(By.LINK_TEXT, 'cat')
print(type(linkElem))
linkElem.click()

"<class 'selenium.webdriver.remote.webelement.WebElement'"