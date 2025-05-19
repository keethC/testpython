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
# Navigate to Bulk Order Page
# ============================

# Click on courier service
courier_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside[1]/div/ul/div[2]/p"))
)
courier_button.click()
print("Clicked on courier service")
time.sleep(5)

# Click on Dashboard
Dashboard_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside[1]/div/ul/div[2]/div/li[1]/a"))
)
Dashboard_button.click()
print("Clicked on Dashboard")
time.sleep(5)

# Click on courier service again
courier_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside[1]/div/ul/div[2]/p"))
)
courier_button.click()
print("Clicked on courier service")
time.sleep(5)

# Click on Bulk Upload
Bulk_order_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//aside[@class='z-20 flex-shrink-0 hidden w-64 overflow-y-auto bg-primary-500 md:block']//span[@class='ml-4'][normalize-space()='Bulk Upload']"))
)
Bulk_order_button.click()
print("Clicked on bulk order")
time.sleep(5)



# ============================
# Upload Invalid Bulk Order sheet
# ============================

## 1) blank COLLECTION AMOUNT

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/blank COLLECTION AMOUNT.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested blank COLLECTION AMOUNT  ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)








## 2) Blank Payment method

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/blank Payment method.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()

print("Clicked on 'Closed' button")
print("Successfully Tested Blank Payment method  ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)








## 3) Blank WEIGHT

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Blank WEIGHT.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested Blank WEIGHT")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)










## 4) Inalid SENDER ADDRESS 

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Inalid SENDER ADDRESS.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested Inalid SENDER ADDRESS   ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)










## 5) Invalid RECEIVER ADDRESS

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid RECEIVER ADDRESS.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested Invalid RECEIVER ADDRESS ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)











## 6) Invalid RECEIVER CITY

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid RECEIVER CITY.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested Invalid RECEIVER CITY  ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)














## 7) Invalid RECEIVER CONTACT NUMBER

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid RECEIVER CONTACT NUMBER.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested  Invalid RECEIVER CONTACT NUMBER ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)












## 8) Invalid RECEIVER NAME

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid RECEIVER NAME.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested  Invalid RECEIVER NAME ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)









## 9) Invalid SENDER CITY

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid SENDER CITY.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested  Invalid SENDER CITY ")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)












## 10) Invalid SENDER CONTACT NAME

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid SENDER CONTACT NAME.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested  Invalid SENDER CONTACT NAME")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)











## 11) Invalid SENDER CONTACT NUMBER

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid SENDER CONTACT NUMBER.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested  Invalid SENDER CONTACT NUMBER")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)







## 12) Invalid SENDER NAME

# Click on 'New Bulk Order' button
new_bulkorder_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[1]/button[1]"))
)
new_bulkorder_button.click()
print("Clicked on 'New Bulk Order' button")
time.sleep(4)

# Click on service provider dropdown
service_provider_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']"))
)
service_provider_dropdown.click()
time.sleep(1)

# Select the vendor from the dropdown
vendor_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='package_vendor_id']/option[2]"))
)
vendor_option.click()
print("Selected service provider")
time.sleep(3)

# Upload file
upload_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)
upload_input.send_keys(r"C:/Users/user/Desktop/invalid/Invalid SENDER NAME.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
print("Import Successfully ")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Clicked on 'Closed' button")
print("Successfully Tested  Invalid SENDER NAME")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(8)




