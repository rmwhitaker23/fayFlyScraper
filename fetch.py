from bs4 import BeautifulSoup
import requests
import sys
import tldextract

# Extracts the domain name from the url... ex: www.google.com -> google
def getDomain(url):
  extracted = tldextract.extract(url)
  domain = extracted.domain
  return domain

def openOutput(domain):
  output = open(str(domain) + '.txt', 'w')
  return output

def setPage(url):
  page = requests.get(url)
  # save status code as a string for availability checking below
  stat = str(page.status_code)
  # Terminate program and return error on screen and in output if page is unavailable
  if stat.startswith('4' or '5'):
	  #print("Error: " + stat)
	  output.write("Error " + stat)
	  sys.exit("Error " + stat)
  return page

def getPageContent(page):
  soup = BeautifulSoup(page.content, 'html.parser')
  #print(soup.prettify())
  return soup

def printHeaders(output):
  # Write table headers to top of output file to be used when importing data
  # Use system check to prevent enable compatibility w/ Windows and Linux
  if sys.platform.startswith('linux'):
    output.write("Title; Day of Week; Time; Venue; Category; Link; Description\n")
  else:
    output.write("Title-_- Day -_- Time-_- Venue-_- Category; Link; Description\n")

def getNumTables(soup):
  # Find the number of tables on the page (for looping)
  numTables = len(soup.find_all('table'))
  return numTables

def findAndSave(domain, numTables, soup, output):
  if domain == "fayettevilleflyer":
    fayFly(numTables, soup, output)
  else:
    DTBville(numTables, soup, output)

def fayFly(numTables, soup, output):
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
      # Save the link for each event
      link = dayTable.find_all('a', href=True)[y]
      eventPage = requests.get(link['href'])
      # Fetch and save description of each event, found in blockquotes on the event's own site
      eventSoup = BeautifulSoup(eventPage.content, 'html.parser')
      numBlockquotes = len(eventSoup.find_all('blockquote'))
      if numBlockquotes > 0:
        # numBlockquotes-1 because the first blockquote on the page is blockquote 0, not 1
        description = eventSoup.find_all('blockquote')[numBlockquotes-1].get_text()
      ''' print(title)
      print(dayOfWeek)
      print(time)
      print(venue)
      print(category)
      # Print link for each event
      print(link['href'])
      # Print blockquote if it exists
      if numBlockquotes > 0:
        print(description)
      print("\n") '''
      # Use platform check to prevent enable compatibility w/ Windows and Linux
      if sys.platform.startswith('linux'):
        # Output to text file using .encode('utf-8') on Linux (repl.it)
        output.write(title.encode('utf-8') + "; ")
        output.write(dayOfWeek.encode('utf-8') + "; ")
        output.write(time.encode('utf-8') + "; ")
        output.write(venue.encode('utf-8') + "; ")
        output.write(category.encode('utf-8') + "; ")
        output.write(link['href'].encode('utf-8') + "; ")
        # Output description if it exists, otherwise just output newline character
        if numBlockquotes > 0:
          output.write(description.encode('utf-8') + "\n")
        else:
          output.write("\n")
      else:
        # Output without .encode, and change | to -_- or similar on Windows
        # see if ; works on Windows... could get rid of platform check in that case
        output.write(title + "-_- ")
        output.write(dayOfWeek + "-_- ")
        output.write(time + "-_- ")
        output.write(venue + "-_- ")
        output.write(category + "-_- ")
        output.write(link['href'] + "-_- ")
        # Output description if it exists, otherwise just output newline character
        if numBlockquotes > 0:
          output.write(description + "\n")
        else:
          output.write("\n")

''' def DTBville(numTables, soup, output):
  numTimes = len(soup.find_all(class_="timely-title-text"))
  for y in range(numTimes-4):
    print(y+1)
    #Get title, time, venue, and category of event y
    title = soup.find_all(class_="timely-title-text")[y].get_text()
    time = soup.find_all(class_="timely-start-time")[y].get_text()
    venue = soup.find_all(class_="timely-venue")[y].get_text()
    # remove tabs, new lines, and a dash from time
    time = time.replace('\t', '')
    time = time.replace('\n', '')
    time = time.replace('-', '')
    venue = venue.replace('\t', '')
    venue = venue.replace('\n', '')
    venue = venue.replace('-', '')  
    # Print event info with new line to separate them
    # Don't need this, but nice to see when developing
    print(title.strip())
    print(time.strip())
    print(venue.strip())
    print("\n")
    # Output to text file using .encode('utf-8') because otherwise ascii error will occur
    output.write(title.encode('utf-8') + "; ")
    output.write("")
    output.write(time.encode('utf-8') + "; ")
    output.write(venue.encode('utf-8') + "; ")
    output.write("" + "\n") '''

def closeOutput(output):
  # Close the output file
  output.close()