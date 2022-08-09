from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("This script is using to login Gmail and send mail . Can't use this script to log out or login with web mail is logged ")

driver = webdriver.Chrome(executable_path="C:\Webdriver\chromedriver.exe")
time.sleep(5)

driver.get("http://www.gmail.com")
time.sleep(5)

#Input User Name
driver.find_element(By.NAME,"identifier").send_keys("TestLoginVsee123@gmail.com")
time.sleep(5)

# Press Next
driver.find_element(By.ID,"identifierNext").click()
time.sleep(5)

#Input Password
driver.find_element(By.NAME,"password").send_keys("TestLogin123")
time.sleep(5)

# Press Next
driver.find_element(By.ID,"passwordNext").click()
time.sleep(5)

# Compose mail
driver.find_element(By.CLASS_NAME,'T-I.T-I-KE.L3').click()
time.sleep(5)

# Input To Address
driver.find_element(By.NAME,"to").send_keys("cuongnguyenhuu80@outlook.com")
time.sleep(5)

#Input Title
driver.find_element(By.NAME,"subjectbox").send_keys("Cau 1: Test selenium Chrome")
time.sleep(5)

#Input Content
driver.find_element(By.ID,":9b").send_keys("Test_IMAP")
time.sleep(5)

#Press Send
driver.find_element(By.ID,":7v").click()
time.sleep(5)

driver.close()


