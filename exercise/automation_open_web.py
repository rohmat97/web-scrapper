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
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Produk Reksa Dana')]"))
    )
    
    # Click the button
    button.click()
    
    # Wait for the button to be clickable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'cpContent_grdProdReksadana_DXPagerBottom_PSB'))
    )
    
    # Click the button
    button.click()
    
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'cpContent_grdProdReksadana_DXPagerBottom_PSP_DXI3_T'))
    )
    
    # Click the button
    button.click()

    # Perform other actions if needed after clicking the button

finally:
    # Close the browser window
    driver.quit()
