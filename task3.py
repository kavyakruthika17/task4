from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get('URL_OF_THE_WEBSITE')

# Perform actions to navigate through pages
while True:
    # Extract and process the page content
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # (extract and process data here)
    
    try:
        # Find and click the next page button
        next_button = driver.find_element(By.CLASS_NAME, 'next-button-class')
        next_button.click()
        time.sleep(2)  # wait for the page to load
    except:
        break

# Close the WebDriver
driver.quit()
