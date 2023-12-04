  
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getListMenu(driver):
    
    # Open the webpage
    driver.get('https://reksadana.ojk.go.id/Public/APERDPublic.aspx?id=AIT69')
    list_id = []
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
                id_value = td_element.get('id')
                flag = td_element.text.replace(" ", "")
                list_id.append({"id":id_value , "flag": flag})
                
        else:
            print("Table not found on the webpage.")
           
        file_path = './outputListMenu.json'
        with open(file_path, 'w') as json_file:
            json.dump(list_id, json_file)
    
    finally:
        print('success')
        # driver.quit()
