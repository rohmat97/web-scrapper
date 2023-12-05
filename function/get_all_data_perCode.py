  
  
  
import csv
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getListAllData(list_code, driver):
    print(list_code[0]["flag"])
    driver.get('https://reksadana.ojk.go.id/Public/APERDPublic.aspx?id=AIT69')
    try:
        for item in list_code:
            # Wait for the button to be clickable
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID,"cpContent_cboAPERD_I"))
            )
            # Click the button
            button.click()
            
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, item["id"]))
            )
            # Click the button
            button.click()
            
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

            # Wait for the data to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'cpContent_grdProdReksadana_DXMainTable'))
            )

            
            # Get page source
            page_source = driver.page_source
            # Get page code
            code = re.search(r'id=(\w+)', driver.current_url).group(1)

            # Use BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(page_source, 'html.parser')

            # Now you can extract data using BeautifulSoup
            # Example: Find and print the title of the page
            table = soup.find('table', {'id': 'cpContent_grdProdReksadana_DXMainTable'})
            if table:  # Check if the table exists
                rows = table.find_all('tr')
                # Extract headers
                headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]

                # Add a new header for the new column as the first column
                headers.insert(0, 'New Column')
                rows.pop(1)
                rows.pop(1)
                # Extract and write existing table data with the new column as the first column to CSV
                with open('file_csv/'+code+'_table_data.csv', mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    # writer.writerow(headers)
                    for row in rows[1:]:
                        cols = row.find_all(['td', 'th'])
                        row_data = [col.get_text(strip=True) for col in cols]

                        # Add dummy data for the new column (you can modify this logic)
                        new_column_data = code
                        row_data.insert(0, new_column_data)

                        writer.writerow(row_data)

                print("New column added as the first column in 'table_data.csv'")
            else:
                print("Table not found on the webpage.")

    finally:
        # Close the browser window
        driver.quit()
