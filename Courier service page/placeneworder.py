from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# ============================
# Launch and Login
# ============================

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
password.send_keys("21d7DsYqsEgIN1p")
print("Entered password")
time.sleep(1)

# Click login button
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
print("Clicked login button")
print("Login successful")

# ============================
# Navigate to Courier Page
# ============================

# Click on courier service
courier_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside[1]/div/ul/div[2]/p"))
)
courier_button.click()
print("Clicked on courier service")
time.sleep(5)

# Click on My Order 
myorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside[1]/div/ul/div[2]/div/li[3]"))
)
myorder_button.click()
print("Clicked on My Order")
time.sleep(10)


# ============================
# Place  New Order
# ============================



wait = WebDriverWait(browser, 10)

# 1. Click "New Order" button
new_order_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button")))
new_order_btn.click()
print("Clicked 'New Order' button")
time.sleep(8)

# 2. Click "New Parcel"
new_parcel = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[5]/div/div/div[2]/form/div[1]/div/div/div[1]/div[1]")))
new_parcel.click()
print("Clicked 'New Parcel'")
time.sleep(8)



# # 1. Select Service Provider
# service_provider_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']")))
# service_provider_dropdown.click()
# time.sleep(5)
# select_provider = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]")))
# select_provider.click()
# print("Selected service provider")
# time.sleep(5)

# # 2. Select Product Type
# product_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='package_type_id']")))
# product_type_dropdown.click()
# time.sleep(5)
# select_type = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='package_type_id']/option[3]")))
# select_type.click()
# print("Selected product type")
# time.sleep(5)

# # 3. Select Weight
# weight_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='weight']")))
# weight_dropdown.click()
# time.sleep(5)
# select_weight = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='weight']/option[4]")))
# select_weight.click()
# print("Selected weight")
# time.sleep(5)

# # 4. Select Return Address
# return_address_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='return_vendor_id']")))
# return_address_dropdown.click()
# time.sleep(5)
# select_return = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='return_vendor_id']/option[2]")))
# select_return.click()
# print("Selected return address")
# time.sleep(5)


# Step 1: Locate and click the recipient city input field
recipient_city_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='873']")))  # <-- Use actual ID from HTML
recipient_city_input.click()
recipient_city_input.send_keys("Galle")  # Type the city name
time.sleep(2)

# Step 2: Wait for suggestions to load and select one
suggested_city = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='autocomplete-results']/div")))  # Choose correct index
suggested_city.click()
print("Selected recipient city")

















