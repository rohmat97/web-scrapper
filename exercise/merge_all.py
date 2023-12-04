import pandas as pd
import os

# Set the directory containing your CSV files
csv_directory = './'

# File paths of the CSV files you want to merge
csv_files = ['file_csv/AIT69_table_data.csv', 'file_csv/AFT69_table_data.csv', 'file_csv/CIT69_table_data.csv', 'file_csv/PP069_table_data.csv']

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through each CSV file and concatenate its data to the merged_data DataFrame
for file in csv_files:
    file_path = os.path.join(csv_directory, file)
    current_data = pd.read_csv(file_path)
    merged_data = pd.concat([merged_data, current_data], axis=0, ignore_index=True)

# Save the vertically merged data to a new CSV file
merged_data.to_csv('./vertically_merged_data.csv', index=False)

print("Merging complete. Merged data saved to merged_data.csv.")
