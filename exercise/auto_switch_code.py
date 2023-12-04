  
  
  
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
list_code = ['cpContent_cboAPERD_DDD_L_LBI0T0', 'cpContent_cboAPERD_DDD_L_LBI1T0', 'cpContent_cboAPERD_DDD_L_LBI2T0', 'cpContent_cboAPERD_DDD_L_LBI3T0', 'cpContent_cboAPERD_DDD_L_LBI4T0', 'cpContent_cboAPERD_DDD_L_LBI5T0', 'cpContent_cboAPERD_DDD_L_LBI6T0', 'cpContent_cboAPERD_DDD_L_LBI7T0', 'cpContent_cboAPERD_DDD_L_LBI8T0', 'cpContent_cboAPERD_DDD_L_LBI9T0', 'cpContent_cboAPERD_DDD_L_LBI10T0', 'cpContent_cboAPERD_DDD_L_LBI11T0', 'cpContent_cboAPERD_DDD_L_LBI12T0', 'cpContent_cboAPERD_DDD_L_LBI13T0', 'cpContent_cboAPERD_DDD_L_LBI14T0', 'cpContent_cboAPERD_DDD_L_LBI15T0', 'cpContent_cboAPERD_DDD_L_LBI16T0', 'cpContent_cboAPERD_DDD_L_LBI17T0', 'cpContent_cboAPERD_DDD_L_LBI18T0', 'cpContent_cboAPERD_DDD_L_LBI19T0', 'cpContent_cboAPERD_DDD_L_LBI20T0', 'cpContent_cboAPERD_DDD_L_LBI21T0', 'cpContent_cboAPERD_DDD_L_LBI22T0', 'cpContent_cboAPERD_DDD_L_LBI23T0', 'cpContent_cboAPERD_DDD_L_LBI24T0', 'cpContent_cboAPERD_DDD_L_LBI25T0', 'cpContent_cboAPERD_DDD_L_LBI26T0', 'cpContent_cboAPERD_DDD_L_LBI27T0', 'cpContent_cboAPERD_DDD_L_LBI28T0', 'cpContent_cboAPERD_DDD_L_LBI29T0', 'cpContent_cboAPERD_DDD_L_LBI30T0', 'cpContent_cboAPERD_DDD_L_LBI31T0', 'cpContent_cboAPERD_DDD_L_LBI32T0', 'cpContent_cboAPERD_DDD_L_LBI33T0', 'cpContent_cboAPERD_DDD_L_LBI34T0', 'cpContent_cboAPERD_DDD_L_LBI35T0', 'cpContent_cboAPERD_DDD_L_LBI36T0', 'cpContent_cboAPERD_DDD_L_LBI37T0', 'cpContent_cboAPERD_DDD_L_LBI38T0', 'cpContent_cboAPERD_DDD_L_LBI39T0', 'cpContent_cboAPERD_DDD_L_LBI40T0', 'cpContent_cboAPERD_DDD_L_LBI41T0', 'cpContent_cboAPERD_DDD_L_LBI42T0', 'cpContent_cboAPERD_DDD_L_LBI43T0', 'cpContent_cboAPERD_DDD_L_LBI44T0', 'cpContent_cboAPERD_DDD_L_LBI45T0', 'cpContent_cboAPERD_DDD_L_LBI46T0', 'cpContent_cboAPERD_DDD_L_LBI47T0', 'cpContent_cboAPERD_DDD_L_LBI48T0', 'cpContent_cboAPERD_DDD_L_LBI49T0', 'cpContent_cboAPERD_DDD_L_LBI50T0', 'cpContent_cboAPERD_DDD_L_LBI51T0', 'cpContent_cboAPERD_DDD_L_LBI52T0', 'cpContent_cboAPERD_DDD_L_LBI53T0', 'cpContent_cboAPERD_DDD_L_LBI54T0', 'cpContent_cboAPERD_DDD_L_LBI55T0', 'cpContent_cboAPERD_DDD_L_LBI56T0', 'cpContent_cboAPERD_DDD_L_LBI57T0', 'cpContent_cboAPERD_DDD_L_LBI58T0', 'cpContent_cboAPERD_DDD_L_LBI59T0', 'cpContent_cboAPERD_DDD_L_LBI60T0', 'cpContent_cboAPERD_DDD_L_LBI61T0', 'cpContent_cboAPERD_DDD_L_LBI62T0', 'cpContent_cboAPERD_DDD_L_LBI63T0', 'cpContent_cboAPERD_DDD_L_LBI64T0', 'cpContent_cboAPERD_DDD_L_LBI65T0', 'cpContent_cboAPERD_DDD_L_LBI66T0', 'cpContent_cboAPERD_DDD_L_LBI67T0', 'cpContent_cboAPERD_DDD_L_LBI68T0', 'cpContent_cboAPERD_DDD_L_LBI69T0', 'cpContent_cboAPERD_DDD_L_LBI70T0', 'cpContent_cboAPERD_DDD_L_LBI71T0', 'cpContent_cboAPERD_DDD_L_LBI72T0', 'cpContent_cboAPERD_DDD_L_LBI73T0', 'cpContent_cboAPERD_DDD_L_LBI74T0', 'cpContent_cboAPERD_DDD_L_LBI75T0', 'cpContent_cboAPERD_DDD_L_LBI76T0', 'cpContent_cboAPERD_DDD_L_LBI77T0', 'cpContent_cboAPERD_DDD_L_LBI78T0', 'cpContent_cboAPERD_DDD_L_LBI79T0', 'cpContent_cboAPERD_DDD_L_LBI80T0']
try:
    for item in list_code:
        # Wait for the button to be clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID,"cpContent_cboAPERD_I"))
        )
        # Click the button
        button.click()
        
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, item))
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
            print(rows)

                
        else:
            print("Table not found on the webpage.")

finally:
    # Close the browser window
    driver.quit()
