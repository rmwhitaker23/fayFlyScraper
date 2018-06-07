import pandas as pd

# Create a Pandas dataframe from the data.
data = pd.read_csv('fayettevilleEvents.txt', sep='-_- ')

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('fayettevilleEvents.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
data.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()