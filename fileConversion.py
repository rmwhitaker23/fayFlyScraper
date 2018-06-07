# install pandas for spreadsheet operations
import pandas
# install pyexcel and pyexcel-xlsx (for .xlsx files)
import pyexcel
# install xlsxwriter for writing to xlsxwriter
import xlsxwriter
# install sys for platform check
import sys

# Create a Pandas dataframe from the data.
if sys.platform.startswith('linux'):
  data = pandas.read_csv('fayettevilleEvents.txt', sep='; ')
else:
  data = pandas.read_csv('fayettevilleEvents.txt', sep='-_- ')

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pandas.ExcelWriter('fayettevilleEvents.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
data.to_excel(writer, sheet_name='Sheet1', encoding='utf-8')

print("I made it!")

# Close the Pandas Excel writer and output the Excel file.
writer.save()

# Convert .xlsx to a .html webpage with the table
# must include ".handsontable" in dest_file_name
pyexcel.save_as(file_name='fayettevilleEvents.xlsx', dest_file_name='fayettevilleEvents.handsontable.html')
