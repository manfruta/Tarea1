import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
driver.get('https://www.dominospizza.cl')
time.sleep(3)
driver.find_element_by_xpath("//*[@id='iniciaSesion']").click()

usr = driver.find_element_by_id("user_email")
usr.send_keys("ma.luengo3@gmail.com")
time.sleep(3)



psw = driver.find_element_by_id("user_password")
psw.send_keys("marce123")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='submit-login']").click()