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
# Filter Functionality Tests
# ============================

# ----- Filter 1: Payment Method -----
filter_bulk = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filters-menu']"))
)
filter_bulk.click()
print("Filter click done")
time.sleep(4)

payment_method_dropdown = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-payment_method_id']"))
)
payment_method_dropdown.click()
time.sleep(2)

payment_method_cash = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-payment_method_id']/option[2]"))
)
payment_method_cash.click()
print("Filter by Payment Method Successful")
time.sleep(15)

# Close filter 1
Close1 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[2]/div/span/button"))
)
Close1.click()
print("Close 1 done")
time.sleep(2)

# ----- Filter 2: Status -----
filter_bulk = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filters-menu']"))
)
filter_bulk.click()
print("Filter click done")
time.sleep(4)

status = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-status']"))
)
status.click()
time.sleep(2)

status_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-status']/option[7]"))
)
status_option.click()
print("Filter by Status Successful")
time.sleep(7)

# Close filter 2
Close2 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='flex-shrink-0 ml-0.5 h-4 w-4 rounded-full inline-flex items-center justify-center text-indigo-400 hover:bg-indigo-200 hover:text-indigo-500 focus:outline-none focus:bg-indigo-500 focus:text-white']//*[name()='svg']//*[name()='path' and contains(@stroke-linecap,'round')]"))
)
Close2.click()
print("Close 2 done")
time.sleep(2)

# ----- Filter 3: Payment Status -----
filter_bulk = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filters-menu']"))
)
filter_bulk.click()
print("Filter click done 3")
time.sleep(4)

Payment_status = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-payment_status']"))
)
Payment_status.click()
time.sleep(2)

Payment_status_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-payment_status']/option[2]"))
)
Payment_status_option.click()
print("Filter by Payment Status Successful")
time.sleep(7)

# Close filter 3
Close3 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='flex-shrink-0 ml-0.5 h-4 w-4 rounded-full inline-flex items-center justify-center text-indigo-400 hover:bg-indigo-200 hover:text-indigo-500 focus:outline-none focus:bg-indigo-500 focus:text-white']//*[name()='svg']//*[name()='path' and contains(@stroke-linecap,'round')]"))
)
Close3.click()
print("Close 3 done")
time.sleep(8)


# ============================
# Select Entry and Export
# ============================

# Click entry checkbox
entry_checkbox = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/input"))
)
entry_checkbox.click()
print("Selected first entry checkbox")
time.sleep(6)

# Click bulk action dropdown
bulk_action = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='options-menu']"))
)
bulk_action.click()
print("Clicked bulk action dropdown")
time.sleep(2)

# Click export button
export_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/button"))
)
export_button.click()
print("Clicked export button")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(5)




# Dropdown option Function to select entries per page 
def select_entries(count_xpath, label):
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='perPage']"))
    )
    dropdown.click()
    time.sleep(1)
    option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, count_xpath))
    )
    option.click()
    print(f"Selected {label} entries")
    time.sleep(7)

# Select 5 entries
select_entries("//*[@id='perPage']/option[1]", "5")

# Select 10 entries
select_entries("//*[@id='perPage']/option[2]", "10")

# Select 15 entries
select_entries("//*[@id='perPage']/option[3]", "15")

# Select 20 entries
select_entries("//*[@id='perPage']/option[4]", "20")

# Select 50 entries
select_entries("//*[@id='perPage']/option[5]", "50")

# Select 100 entries
select_entries("//*[@id='perPage']/option[6]", "100")



# ============================
# Upload Bulk Order sheet
# ============================


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
upload_input.send_keys(r"C:/Users/user/Desktop/dhl.xlsx")  # corrected file path and extension
print("File uploaded successfully")
time.sleep(15)

# Click on 'Import Sheet' button
import_sheet_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button[1]"))
)
import_sheet_button.click()
print("Clicked 'Import Sheet' button")
time.sleep(20)

# # Close button 
# import_close_button = WebDriverWait(browser, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/button"))
# )
# import_close_button.click()
print("Import Done")
time.sleep(4)


# ============================
# Print the order details  
# ============================
printbulk_details=WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[7]/div[1]/button[2]"))
)
printbulk_details.click()
print("Redirect to another page successfully")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(5)