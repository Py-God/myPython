from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.implicitly_wait(20) # gives an implicit wait for 20 seconds

browser.get('https://mail.yahoo.com')
emailElem = browser.find_element(By.ID, 'login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element(By.ID, 'login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()
# you could also use emailElem to submit if you want.
        # this code will bring out an error cuz those ids are not on the first page of yahoo.com
        # and thats also not a valid email or password for a login
