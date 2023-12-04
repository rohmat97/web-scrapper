import requests
from bs4 import BeautifulSoup
import csv


my_array = ['CIT69','AFT69','AIT69','PP069']

# Data for the new row header
new_row_header = ['Label', 'Manager Investasi', 'Reksa Dana']
# Loop through the array using range and index
for i in range(len(my_array)):
    # print(my_array[i])
    url = 'https://reksadana.ojk.go.id/Public/APERDPublic.aspx?id='+my_array[i]

    # Fetch the HTML content from the URL
    response = requests.get(url)

    if response.status_code == 200:  # Check if the request was successful (status code 200)
        html_content = response.text

        # Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table element by its ID (or any other selector)
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
            with open('file_csv/'+ my_array[i]+'_table_data.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                writer.writerow(new_row_header)
                for row in rows[1:]:
                    cols = row.find_all(['td', 'th'])
                    row_data = [col.get_text(strip=True) for col in cols]

                    # Add dummy data for the new column (you can modify this logic)
                    new_column_data = my_array[i]
                    row_data.insert(0, new_column_data)
                    
                    writer.writerow(row_data)

            print("New column added as the first column in 'table_data.csv'")
        else:
            print("Table not found on the webpage.")
    else:
        print("Failed to fetch the webpage.")
