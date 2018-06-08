import fetch

# import convert

############################################################
####          Fetch data and save in .txt file          ####
############################################################

# Open file for output
output = fetch.openOutput()

# Set the page to be searched and do page status check
page = fetch.setPage()

# Fetch page content
soup = fetch.getPageContent(page)

# Print headers in output file
fetch.printHeaders(output)

# Fetch number of events on calendar
numTables = fetch.getNumTables(soup)

# Bulk of the process - find, save, and output data
fetch.findAndSave(numTables, soup, output)

# Close output file
fetch.closeOutput(output)

############################################################
####                     Conversion                     ####
############################################################
# does not work on Python 2.7.10/Debian 8.6

''' # Create a Pandas dataframe from the data.
convert.mkTable()

# Create a Pandas Excel writer using xlsxwriter as the engine.
writer = convert.mkWriter()

# Convert dataframe to an Excel object and save
convert.convertAndSave(writer)

# Convert .xlsx to a .html webpage with the table
convert.mkHTML() '''
