import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
driver.get('https://www.dominospizza.es')
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/header[1]/div/section[1]/nav[1]/div[2]/span[1]").click()

usr = driver.find_element_by_id("txtUser")
usr.send_keys("marcelo.luengo@mail.udp.cl")
time.sleep(3)



psw = driver.find_element_by_id("txtPass")
psw.send_keys("osaiopgato300")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='btnLoginMenu']").click()
time.sleep(3)
