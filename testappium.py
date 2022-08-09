from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

print("This script is tested on virtual device created by LDplayer and Appium and only test with fresh user.")

desired_cap = {
	"uuid" : "emulator-5554",
	"platformName" : "Android",
	"appPackage" : "com.ldmnq.launcher3",
	"appActivity" : "com.android.launcher3.Launcher"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
time.sleep(20)

#Open Application
App = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='VSee Messenger Beta')
App.click()
time.sleep(5)

#Input Email
Email = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/loginEmailEdit')
Email.send_keys("cuongnguyenhuu80@gmail.com")
time.sleep(5)

#Input Password
Password = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/loginPasswordEdit')
Password.send_keys("TestLogin123")
time.sleep(5)

#Press Sign in
Login = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/loginSignInBut')
Login.click()
time.sleep(5)

#Press contact
CheckContact = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/itemContactListLayout')
CheckContact.click()
time.sleep(5)

#Press Chat button
Message = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Chats')
Message.click()
time.sleep(5)

#Start chat . This step only use at the first time start chat.
StartChat = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/empty_text_view_2')
StartChat.click()
time.sleep(5)

# Choose contact in list
Choosecontact = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/itemContactListLayout')
Choosecontact.click()
time.sleep(5)

# Press Done
Done = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/action_done')
Done.click()
time.sleep(5)

#Input content chat
TypingChat = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/chatEditText')
TypingChat.send_keys("Test Send Message")
time.sleep(5)

#Send message
Sendmessage = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='com.vsee.vsee.beta:id/chatSendBut')
Sendmessage.click()
time.sleep(5)


driver.close()


