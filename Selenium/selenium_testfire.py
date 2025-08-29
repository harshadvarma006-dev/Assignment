from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Save screenshots folder
os.makedirs("screenshots", exist_ok=True)

# Launch browser (make sure you installed ChromeDriver or GeckoDriver)
driver = webdriver.Chrome()  # or webdriver.Firefox()

driver.get("https://demo.testfire.net/")
time.sleep(2)
driver.save_screenshot("screenshots/home.png")

# 1. Click Sign In
driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(2)
driver.save_screenshot("screenshots/signin.png")

# 2. Fill login form (test credentials)
driver.find_element(By.ID, "uid").send_keys("admin")
driver.find_element(By.ID, "passw").send_keys("admin")
driver.find_element(By.NAME, "btnSubmit").click()
time.sleep(2)
driver.save_screenshot("screenshots/dashboard.png")

# 3. Navigate to Account Summary
driver.find_element(By.LINK_TEXT, "View Account Summary").click()
time.sleep(2)
driver.save_screenshot("screenshots/account_summary.png")

# 4. Navigate to Transfer Funds
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
time.sleep(2)
driver.save_screenshot("screenshots/transfer_funds.png")

# 5. Navigate to View Recent Transactions
driver.find_element(By.LINK_TEXT, "View Recent Transactions").click()
time.sleep(2)
driver.save_screenshot("screenshots/recent_txns.png")

# 6. Navigate to Online Statements
driver.find_element(By.LINK_TEXT, "Online Statements").click()
time.sleep(2)
driver.save_screenshot("screenshots/statements.png")

# Done
driver.quit()
print("Crawling complete. Screenshots saved in 'screenshots/' folder.")
