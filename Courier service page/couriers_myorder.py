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
# Filter Functionality Tests
# ============================

# ----- Filter 1: Payment Method -----
filter_my = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filters-menu']"))
)
filter_my.click()
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
    EC.element_to_be_clickable((By.XPATH, "//button[@class='flex-shrink-0 ml-0.5 h-4 w-4 rounded-full inline-flex items-center justify-center text-indigo-400 hover:bg-indigo-200 hover:text-indigo-500 focus:outline-none focus:bg-indigo-500 focus:text-white']//*[name()='svg']"))
)
Close1.click()
print("Close 1 done")
time.sleep(7)

# ----- Filter 2: Status -----
filter_bulk = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filters-menu']"))
)
filter_bulk.click()
print("Filter click done 2")
time.sleep(4)

status_m = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-status']"))
)
status_m.click()
time.sleep(3)

status_moption = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-status']/option[7]"))
)
status_moption.click()
print("Filter by Status Successful")
time.sleep(7)

# Close filter 2
Close2 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='flex-shrink-0 ml-0.5 h-4 w-4 rounded-full inline-flex items-center justify-center text-indigo-400 hover:bg-indigo-200 hover:text-indigo-500 focus:outline-none focus:bg-indigo-500 focus:text-white']//*[name()='svg']"))
)
Close2.click()
print("Close 2 done")
time.sleep(5)

# # ----- Filter 3: Payment Status -----
filter_bulk = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filters-menu']"))
)
filter_bulk.click()
print("Filter click done")
time.sleep(4)

Payment_status = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-payment_status']"))
)
Payment_status.click()
time.sleep(2)

Payment_status_option = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-payment_status']/option[4]"))
)
Payment_status_option.click()
print("Filter by Payment Status Successful")
time.sleep(7)

# Close filter 3
Close3 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='flex-shrink-0 ml-0.5 h-4 w-4 rounded-full inline-flex items-center justify-center text-indigo-400 hover:bg-indigo-200 hover:text-indigo-500 focus:outline-none focus:bg-indigo-500 focus:text-white']"))
)
Close3.click()
print("Close 3 done")
time.sleep(8)


browser.refresh()
print("Page refreshed successfully")
time.sleep(10)


# ============================
# Search Functionality Tests
# ============================



# 1st Search by Id
search_bar = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/div[1]/input"))
)
search_bar.click()
search_bar.send_keys(" 7409 ")
print("Search by ID successful")
time.sleep(6)



# 1st Close
close_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/div[1]/span"))
)
close_button.click()
print("Closed first search")
time.sleep(2)

search_bar.clear()
print("Search field 1 cleared")
time.sleep(5)

# 2nd Search
search_bar = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/div[1]/input"))
)
search_bar.click()
search_bar.send_keys(" D12959560 ")
print(" Search by way bill successful ")
time.sleep(6)

# 2nd Close
close_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/div[1]/span"))
)
close_button.click()
print("Closed second search")
time.sleep(3)

search_bar.clear()
print("Search field 2 cleared")
time.sleep(5)

# ============================
# Tracking Details 
# ============================

track_details=WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/button"))
)

track_details.click()
print("Open tracking detail")
time.sleep(8)

#close tracking details

close_td=WebDriverWait(browser,10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[4]/div/div/div[2]/form/div[2]/button"))
)

close_td.click()
print("Close Detail")
time.sleep(8)

# Refresh the page
browser.refresh()
print("Page refreshed")
time.sleep(8)



# ============================
# Select Entry and Export
# ============================

# Click entry checkbox 1
entry_checkbox1 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='7407']"))
)
entry_checkbox1.click()
print("Selected first entry checkbox")
time.sleep(6)

# Click entry checkbox 2
entry_checkbox2 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='7406']"))
)
entry_checkbox2.click()
print("Selected Second entry checkbox")
time.sleep(6)






# Click bulk action dropdown
bulk_action = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='options-menu']"))
)
bulk_action.click()
print("Clicked bulk action dropdown")
time.sleep(5)

# Click export button
export_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/button"))
)
export_button.click()
print("Clicked export button")
print("Exported Successfully")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(5)



# ============================
# Select entries per page 
# ============================




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

browser.refresh()
print("Page refreshed successfully")
time.sleep(5)



# ============================
# View the order details  
# ============================


order_details=WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[11]/div/button[1]"))
)
order_details.click()
print("Details window open successfully")
time.sleep(8)

close_details=WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[3]/div/div/div[2]/button"))
)
close_details.click()
print("Details window close successfully")
time.sleep(5)


browser.refresh()
print("Page refreshed successfully")
time.sleep(5)


# ============================
# Print the order details  
# ============================
print_details=WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[11]/div/button[2]"))
)
print_details.click()
print("Redirect to another page successfully")
time.sleep(8)

browser.refresh()
print("Page refreshed successfully")
time.sleep(5)






