from bs4 import BeautifulSoup
import requests
import sys

# Open text file for raw data output
output = open('fayettevilleEvents.txt', 'w')

page = requests.get("https://www.fayettevilleflyer.com/calendar/")
# save status code as a string for availability checking below
stat = str(page.status_code)

# Terminate program and return error on screen and in output if page is unavailable
if stat.startswith('4' or '5'):
	#print("Error: " + stat)
	output.write("Error " + stat)
	sys.exit("Error " + stat)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

# Write table headers to top of output file to be used when importing data
# Use system check to prevent enable compatibility w/ Windows and Linux
if sys.platform.startswith('linux'):
  output.write("Title; Day of Week; Time; Venue; Category\n")
else:
  output.write("Title-_- Day -_- Time-_- Venue-_- Category\n")

# Find the number of tables on the page (for looping)
numTables = len(soup.find_all('table'))

for z in range(numTables):
  # Store day of week for table z
  dayOfWeek = soup.find_all(class_="event_day")[z].get_text()
  # Store table of events for table z
  dayTable = soup.find_all('table')[z]
  #Get title, time, venue, and category of event y
  numTimes = len(dayTable.find_all(class_="event_time"))
  for y in range(numTimes):
    title = dayTable.find_all('h4')[y].get_text()
    time = dayTable.find_all(class_="event_time")[y].get_text()
    venue = dayTable.find_all(class_="event_venue")[y].get_text()
    category = dayTable.find_all(class_="event_category")[y].get_text()
    print(title)
    print(dayOfWeek)
    print(time)
    print(venue)
    print(category)
    print("\n")
  	# Use platform check to prevent enable compatibility w/ Windows and Linux
    if sys.platform.startswith('linux'):
      # Output to text file using .encode('utf-8') on Linux (repl.it)
      output.write(title.encode('utf-8') + "; ")
      output.write(dayOfWeek.encode('utf-8') + "; ")
      output.write(time.encode('utf-8') + "; ")
      output.write(venue.encode('utf-8') + "; ")
      output.write(category.encode('utf-8') + "\n")
    else:
      # Output without .encode, and change | to -_- or similar on Windows
      # see if ; works on Windows... could get rid of platform check in that case
      output.write(title + "-_- ")
      output.write(dayOfWeek + "-_- ")
      output.write(time + "-_- ")
      output.write(venue + "-_- ")
      output.write(category + "\n")

# Close the output file
output.close()