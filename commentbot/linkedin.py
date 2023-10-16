# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:32:57 2023

@author: c.samanja09
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/")
time.sleep(3)
driver.maximize_window()

email=driver.find_element(By.ID,"session_key")
password = driver.find_element(By.ID,"session_password")
submit = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/section[1]/div[1]/div[1]/form[1]/div[2]/button[1]")
email.send_keys("cart.samanja09@gmail.com")
password.send_keys("Sam#Carta32")
submit.click()
time.sleep(10)




driver.get('https://www.linkedin.com/newsletters/gates-notes-6651495472181637121/')    
driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(10)
all_buttons=driver.find_elements(By.TAG_NAME,"button")
comment=[btn for btn in all_buttons if btn.text=='Comment']
print(len(comment))

time.sleep(5)

if comment[0].is_enabled():
   comment[0].click()
   commentbox=driver.find_element(By.XPATH,"//div[@aria-label='Text editor for creating content']")
   commentbox.send_keys('Great!')
   time.sleep(10)
   postbtn=driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[3]/div[2]/div[1]/div[1]/main[1]/section[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[2]/form[1]/div[2]/button[1]')

   postbtn.click()

   time.sleep(5)
else:
    print('Not possible')
    
    
print('Automation Complete')
driver.quit()
    
