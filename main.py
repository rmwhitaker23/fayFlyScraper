# coding=<utf-8>
import control
import fetch
import convert
import ics
import datetime

############################################################
####          Fetch data and save in .txt file          ####
############################################################

partNum = 0

partNum += 1
start = control.partBegin(partNum)

# FayFly section
url = "https://www.fayettevilleflyer.com/calendar/"
# Get domain from url
domain = fetch.getDomain(url)
# Open file for output
output = fetch.openOutput(domain)
# Set the page to be searched and do page status check
page = fetch.setPage(url)
# Fetch page content
soup = fetch.getPageContent(page)
# Print headers in output file
fetch.printHeaders(output)
# Fetch number of events on calendar
numTables = fetch.getNumTables(soup)
# Bulk of the process - find, save, and output data
fetch.findAndSave(domain, numTables, soup, output)
# Close output file
fetch.closeOutput(output)

control.partEnd(partNum, start)

############################################################
####                  DTBville Section                  ####
############################################################

partNum += 1
start = control.partBegin(partNum)

ics.fileCheck()

url = 'https://events.downtownbentonville.org/export?format=ics'

domain = fetch.getDomain(url)

output = fetch.openOutput(domain)

ics.download(url)

ics.printHeaders(output)

ics.findAndSave(output)

control.partEnd(partNum, start)

############################################################
####                     Conversion                     ####
############################################################
# does not work on Python 2.7.10/Debian 8.6
# Needs updating for DTBville integration

''' # Create a Pandas dataframe from the data.
convert.mkTable()

# Create a Pandas Excel writer using xlsxwriter as the engine.
writer = convert.mkWriter()

# Convert dataframe to an Excel object and save
convert.convertAndSave(writer)

# Convert .xlsx to a .html webpage with the table
convert.mkHTML() '''