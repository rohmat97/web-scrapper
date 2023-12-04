  
  
  
import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'path/to/geckodriver' with the actual path to your GeckoDriver executable
gecko_path = './geckodriver'

# Set GeckoDriver executable path using executable_path argument in options
options = webdriver.FirefoxOptions()
options.binary_location = '/Applications/Firefox.app/Contents/MacOS/firefox-bin'  # Update with your Firefox binary location
options.add_argument(f"marionette;executable_path={gecko_path}")

# Open Firefox WebDriver with specified options
driver = webdriver.Firefox(options=options)

# Open the webpage
driver.get('https://reksadana.ojk.go.id/Public/APERDPublic.aspx?id=AIT69')

try:
    # Wait for the button to be clickable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,"cpContent_cboAPERD_I"))
    )
    # Click the button
    button.click()
    
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cpContent_cboAPERD_DDD_L_LBI1T0"))
    )
    # Click the button
    button.click()
    
    # Get page source
    page_source = driver.page_source

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the table element by its ID (or any other selector)
    table = soup.find('table', {'id': 'cpContent_cboAPERD_DDD_L_LBT'})
    if table:  # Check if the table exists
        rows = table.find_all('tr')
        for item in rows:
            td_element = item.find('td', class_='dxeListBoxItem_DevEx')
            value = td_element.text.replace(" ", "")
            print(value)
                
    else:
        print("Table not found on the webpage.")

finally:
    # Close the browser window
    driver.quit()
