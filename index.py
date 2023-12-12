
import json
import shutil
from selenium import webdriver

from function.get_list_menu import getListMenu
from function.get_all_data_perCode import getListAllData

# Replace 'path/to/geckodriver' with the actual path to your GeckoDriver executable
# gecko_path = './geckodriver'

# # Set GeckoDriver executable path using executable_path argument in options
# options = webdriver.FirefoxOptions()
# options.binary_location = '/Applications/Firefox.app/Contents/MacOS/firefox-bin'  # Update with your Firefox binary location
# options.add_argument(f"marionette;executable_path={gecko_path}")

# Open Firefox WebDriver with specified options
driver = webdriver.Firefox()

driver.get("https://www.example.com")
print(driver.title)

# Your Selenium code here

driver.quit()

# getListMenu(driver)

# # Specify the file path
# file_path = './outputListMenu.json'
# # Read data from the file
# with open(file_path, 'r') as json_file:
#     loaded_data = json.load(json_file)

# if loaded_data: 
#     getListAllData(loaded_data, driver)
    
    
# # Specify the path of the folder you want to zip
# folder_path = './file_csv'

# # Specify the path for the zip file
# zip_file_path = './file_csv/archive.zip'

# # Create a zip file from the folder
# shutil.make_archive(zip_file_path, 'zip', folder_path)

# print(f'Folder "{folder_path}" has been successfully zipped to "{zip_file_path}"')

