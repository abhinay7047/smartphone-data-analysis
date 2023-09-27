import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
s = Service("C:/Users/Lenovo/Downloads/chromedriver.exe")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=s)

# Navigate to the Smartprix website's mobiles section
driver.get("https://www.smartprix.com/mobiles")

# Click on the checkboxes
# These are the XPaths for the checkboxes, which apply the desired filters
driver.find_element(by=By.XPATH, value="//*[@id='app']/main/aside/div/div[5]/div[2]/label[1]/span").click()
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span').click()

# Use explicit wait for the "Load More" button to become clickable
wait = WebDriverWait(driver, 10)
load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/div[1]/div[2]/div[3]')))

# Get the initial height of the webpage to determine the total scrollable height
old_height = driver.execute_script("return document.body.scrollHeight")

# Scroll down repeatedly until the page height remains constant
while True:
    # Click on the "Load More" button to load more products dynamically
    load_more_button.click()

    # Get the new height of the webpage after loading more products
    new_height = driver.execute_script("return document.body.scrollHeight")

    # If the new height is the same as the old height, it means there are no more products to load
    # Exit the loop
    if new_height == old_height:
        break

    # Update the old height with the new height for the next iteration
    old_height = new_height

# Get the entire HTML source of the webpage
html = driver.page_source

# Save the HTML source to a file named "smartprix.html"
with open("smartprix.html", "w", encoding="utf-8") as f:
    f.write(html)
time.sleep(500)
# Close the browser
driver.quit()
