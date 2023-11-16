import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'C:\Projects\Python\matPlotLib\Etoro Data Analysis\etoro-account-statement-1-1-2023-11-14-2023.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Display the DataFrame
print(df)