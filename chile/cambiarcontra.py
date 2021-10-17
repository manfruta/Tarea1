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
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[6]/nav/ul/span/li[1]/a[1]/u").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[9]/div[2]/div/div[1]/a").click()
time.sleep(2)


npas = driver.find_element_by_id("new_password")
npas.send_keys("marce123")
time.sleep(2)

confpas = driver.find_element_by_id("confirm_new_password")
confpas.send_keys("marce123")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='edit_user_455427']/div/div[3]/div/div[2]/input").click()









