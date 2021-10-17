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
driver.find_element_by_xpath("//*[@id='loginPopup']/div[3]/div[1]/a[1]").click()
time.sleep(3)
#nombre:
usr = driver.find_element_by_id("name")
usr.send_keys("Juan")
time.sleep(1)
#apellido
ape = driver.find_element_by_id("surname")
ape.send_keys("Lima")
time.sleep(1)
#email
cor = driver.find_element_by_id("email")
cor.send_keys("ma.luengo3@gmail.com")
time.sleep(1)
#telefono
tel = driver.find_element_by_id("phone")
tel.send_keys("71088589")
time.sleep(1)
#contraseña
contr = driver.find_element_by_id("pass")
contr.send_keys("marce123")
time.sleep(1)
#confirmarcontraseña
cof = driver.find_element_by_id("passConfirmation")
cof.send_keys("marce123")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[9]/div/form/div[2]/span/input").click()
time.sleep(2)
