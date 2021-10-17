import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
driver.get('https://www.dominospizza.cl')
time.sleep(3)
driver.find_element_by_xpath("//*[@id='iniciaSesion']").click()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='loginPopup']/div[3]/div[2]/div/div[3]/span/span/u").click()
time.sleep(3)

psw = driver.find_element_by_id("email_reset_password")
psw.send_keys("ma.luengo3@gmail.com")


driver.find_element_by_xpath("//*[@id='submit-reset-password']").click()


















