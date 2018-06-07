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
	output.write("Title; Time; Venue; Category\n")
else:
	output.write("Title-_- Time-_- Venue-_- Category\n")

# Find number of instances of times on list
numTimes = len(soup.find_all(class_="event_time"))

# Fetch data for the amount of times "event_time" appears on page (used as number of events)
for y in range(numTimes):
	#Get title, time, venue, and category of event y
	title = soup.find_all('h4')[y].get_text()
	time = soup.find_all(class_="event_time")[y].get_text()
	venue = soup.find_all(class_="event_venue")[y].get_text()
	category = soup.find_all(class_="event_category")[y].get_text()
	# Print event info with new line to separate them
	# Don't need this, but nice to see when developing
	print(title)
	print(time)
	print(venue)
	print(category)
	print("\n")
	# Use platform check to prevent enable compatibility w/ Windows and Linux
	if sys.platform.startswith('linux'):
		# Output to text file using .encode('utf-8') on Linux (repl.it)
		output.write(title.encode('utf-8') + "; ")
		output.write(time.encode('utf-8') + "; ")
		output.write(venue.encode('utf-8') + "; ")
		output.write(category.encode('utf-8') + "\n")
	else:
		# Output without .encode, and change | to -_- or similar on Windows
    # see if ; works on Windows... could get rid of platform check in that case
		output.write(title + "-_- ")
		output.write(time + "-_- ")
		output.write(venue + "-_- ")
		output.write(category + "\n")
''' #For testing on first event in calendar
x=1
title = soup.find_all('h4')[x].get_text()
time = soup.find_all(class_="event_time")[x].get_text()
day = soup.find_all(class_="event_day")[x].get_text()
venue = soup.find_all(class_="event_venue")[x].get_text()
category = soup.find_all(class_="event_category")[x].get_text()
print(title)
print(day)
print(time)
print(venue)
print(category)
print("\n") '''
''' # find number of days
numChildren = len(soup.find_all('h2'))
print numChildren '''

# could do count of h2 children (events) and do separate loop to loop for that many times, then update the day

# Close the output file
output.close()
