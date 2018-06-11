# coding=<utf-8>
import fetch
import convert

############################################################
####          Fetch data and save in .txt file          ####
############################################################

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



############################################################
#### DTBville Section - needs to be put into functions  ####
############################################################

import icalendar
from icalendar import Calendar, Event
from bs4 import BeautifulSoup
import lxml
import wget
import os

# Delete .ics file if it already exists to prevent copies (export(1), export(2), etc.)
if os.path.isfile("./export.ics"):
  os.remove("./export.ics")

# Download .ics file from website
# DTSpringdale: https://downtownspringdale.org/?post_type=tribe_events&ical=1
url = 'https://events.downtownbentonville.org/export?format=ics' 
domain = fetch.getDomain(url) 
wget.download(url, './export.ics')  

output = open(domain + '.txt', 'w')
# Write table headers to top of output file to be used when importing data
output.write("Title; Cost; Venue; Description\n")

# Check event cost for numbers
def num_there(s):
    return any(i.isdigit() for i in s)

g = open('export.ics','rb')
gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
  if component.name == "VEVENT":
      summary = component.get('summary')
      output.write(summary.encode("utf-8") + "; ")
      # Only show event cost if contains number (aka exists)
      if num_there(str(component.get('x-cost'))) == True:
        output.write(component.get('x-cost'))
      else:
        output.write("na")
      output.write("; ")
      output.write(str(component.get('location')))
      # Only show event description if it exists
      ''' if str(component.get('description').encode("utf-8")) != "":
      description = component.get('description')
      soup = BeautifulSoup(description, 'lxml') '''
      ''' for a in soup.find_all('p'):
          desc = a.string
          output.write(desc.encode("utf-8"))
        else:
          output.write("na")
        output.write("; ") '''
      # show contact information if isn't empty and isn't the default spam email
      if component.get('contact') != "MAILTO:noreply@facebookmail.com" and component.get('contact') != "":
        contact = component.get('contact')
        output.write("Contact: " + contact.encode("utf-8"))
      output.write("; \n")
g.close()



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