import random
import string
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
driver.get('https://www.dominospizza.es')
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/header[1]/div/section[1]/nav[1]/div[2]/span[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='btnRegistrar']").click()


time.sleep(3)
#nombre:
usr = driver.find_element_by_name("nombre")
usr.send_keys("pipe")
time.sleep(1)
#apellido
ape = driver.find_element_by_name("apellido")
ape.send_keys("elpepe")
time.sleep(1)

#1
cor = driver.find_element_by_id("day")
cor.send_keys("04")
time.sleep(1)
#2
cor = driver.find_element_by_id("month")
cor.send_keys("09")
time.sleep(1)
#3
cor = driver.find_element_by_id("year")
cor.send_keys("1998")
time.sleep(1)
#telefono
tel = driver.find_element_by_name("tlf")
tel.send_keys("923849103")
time.sleep(1)



#email
cor = driver.find_element_by_name("email")
cor.send_keys("marcelo.luengo@mail.udp.cl")
time.sleep(1)

#contraseña
contr = driver.find_element_by_name("password")
contr.send_keys("osaiopgato300")
time.sleep(1)
#confirmarcontraseña
cof = driver.find_element_by_name("repeat_password")
cof.send_keys("osaiopgato300")
time.sleep(1)

#driver.find_element_by_xpath("//*[@id=registrarme']").click()
#driver.find_element_by_xpath("//*[@id='submit-registrarme']").click()
cof.send_keys(Keys.ENTER)

time.sleep(2)
