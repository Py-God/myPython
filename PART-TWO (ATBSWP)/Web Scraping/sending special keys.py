from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.implicitly_wait(20)
browser.get('http://nostarch.com')

htmlElem = browser.find_element(By.TAG_NAME, 'html')
htmlElem.send_keys(Keys.END)    # scrolls to the bottom
htmlElem.send_keys(Keys.HOME)   # scrolls to the top