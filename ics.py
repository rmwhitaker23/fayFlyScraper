import icalendar
from icalendar import Calendar, Event
import datetime
import dateutil.parser as parser
from bs4 import BeautifulSoup
import requests
import fetch
import lxml
import wget
import os

def fileCheck():
  # Delete .ics file if it already exists to prevent copies (export(1), export(2), etc.)
  if os.path.isfile("./export.ics"):
    os.remove("./export.ics")

def download(url):
  # Download .ics file from website
  # DTSpringdale: https://downtownspringdale.org/?post_type=tribe_events&ical=1
  wget.download(url, './export.ics')  

def printHeaders(output):
  # Write table headers to top of output file to be used when importing data
  output.write("Title; Time; Cost; Venue; Contact; Phone; Email; Description\n")

def num_there(s):
  # Check event cost for numbers
  return any(i.isdigit() for i in s)

def findAndSave(output):
  g = open('export.ics','rb')
  gcal = Calendar.from_ical(g.read())
  for component in gcal.walk():
    if component.name == "VEVENT":
        # Get title
        title = component.get('summary')
        output.write(title.encode("utf-8") + "; ")

        # Get event times from each event's individual page
        eventPage = component.get('url')
        eventPage = fetch.setPage(eventPage)
        soup = fetch.getPageContent(eventPage)
        time = soup.find(class_='timely-event-datetime')
        time = time.getText()
        time = str(time)
        time = time.strip()
        output.write(time)
        output.write("; ")

        

        # Only show event cost if contains number (aka exists)
        if num_there(str(component.get('x-cost'))) == True:
          output.write(component.get('x-cost'))
        else:
          output.write("na")
        output.write("; ")

        # Get venue and strip away address if it exists
        sep = '@'
        text = str(component.get('location'))
        rest = text.split(sep, 1)[0]
        #rest = rest[:rest.find("Contact:")]
        output.write(rest)
        output.write("; ")

        # show contact information if isn't empty and isn't the default spam email
        if component.get('contact') != "MAILTO:noreply@facebookmail.com" and component.get('contact') != "":
          contact = component.get('contact')
          output.write(contact.encode("utf-8"))
        output.write("; ")

        # Only show event description if it exists
        ''' if str(component.get('description').encode("utf-8")) != "":
          description = component.get('description')
          soup = BeautifulSoup(description, 'lxml')
          for a in soup.find_all('p'):
            desc = a.string
            output.write(desc.encode("utf-8"))
          else:
            output.write("na") '''
        output.write("\n")
  g.close()