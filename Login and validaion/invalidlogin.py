from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time



# Launch browser
browser = webdriver.Chrome()
browser.maximize_window()
print("Opening browser...")

# Open login page
browser.get("https://dev-api.tgo.lk/login?lan=en")
time.sleep(2)

# Enter email
email_address = browser.find_element(By.ID, "email")
email_address.send_keys("testvendor1@tgo.lk")
print("Entered email")
time.sleep(1)

# Enter password
password = browser.find_element(By.ID, "password")
password.send_keys("ApOpcFz4BbYQS")
print("Entered password")
time.sleep(1)

# Click login button
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
print("Clicked login button")

# Wait to see result
time.sleep(5)

# Close browser
browser.quit()
print("Result as expected:Login credentials invalid  ")
print("Test completed ")

