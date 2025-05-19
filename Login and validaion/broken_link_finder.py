from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Setup browser (ChromeDriver must be in your PATH or set the correct location)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# URL to test
url = "https://dev-api.tgo.lk/login?lan=en"
driver.get(url)

wait = WebDriverWait(driver, 10)
time.sleep(3)  # Allow page to load

# Collect all links and clickable buttons
elements = driver.find_elements(By.XPATH, "//a[@href] | //button | //*[@role='button']")

print(f"Found {len(elements)} clickable elements.\n")

# Check each link/button for valid redirection
for index, elem in enumerate(elements, start=1):
    try:
        tag_name = elem.tag_name
        text = elem.text.strip()
        href = elem.get_attribute("href")
        
        if href and href.startswith("http"):
            try:
                response = requests.head(href, allow_redirects=True, timeout=5)
                status = response.status_code
                if status >= 400:
                    print(f"[BROKEN] ({status}) {text or '[No text]'} --> {href}")
                else:
                    print(f"[OK] ({status}) {text or '[No text]'} --> {href}")
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] {text or '[No text]'} --> {href} : {e}")
        else:
            print(f"[SKIPPED] No valid href for: {text or '[No text]'} (tag: {tag_name})")

    except Exception as e:
        print(f"[ERROR] While processing element #{index}: {e}")

# Close browser
driver.quit()
