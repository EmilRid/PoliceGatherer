import bs4
import requests
from datetime import datetime

# list of all the months in a year for later indexing
months = ["januari", "februari", "mars", "april", "maj", "juni",
          "juli", "augusti", "september", "oktober", "november", "december"]  


class Event:  # Event class used by Gatherer class

    def __init__(self, date, location, title, content, text):
        self.date = date
        self.location = location
        self.title = title
        self.content = content
        self.text = text

    def __repr__(self):
        return self.title

    def print(self):  # used to print out a formatted version of event information
        print(f"DATE: {self.date}\nTITLE: {self.title}\nCONTENT: {self.content}\nTEXT: {self.text}\n","-"*50, "\n")


class Gatherer:  # class that creates objects which can request new event information
    def __init__(self, source):

        self.page = requests.get(source)  # the raw page from request
        self.soup = bs4.BeautifulSoup(self.page.content, "html.parser") # processed page
        self.events = []  # list containing the events gathered from the internet

    def updateEvents(self):  # used to update tthe list of events

        self.raw_list = [event for event in list(self.soup.find(
            "ul", {"class": "listing-control-items js-item-list"})) if isinstance(event, bs4.element.Tag)]  # list comprehension that gathers the raw list of events
        for i, event in enumerate(self.raw_list):
            if len(event.find("strong", {"class": "list-item-heading"}).get_text().split(", ")[0].split(" ")) == 3:
                split_output = event.find("strong", {"class": "list-item-heading"}).get_text().split(", ")
                split_date = event.find("div", {"class": "published-container"}).get_text().split("\n")[2].split(" ")
                
                # DATETIME VARIABLES
                year = datetime.now().year  # year variable
                month = months.index(split_date[1])+1  # month variable
                day = int(split_date[0])  # day variable
                hour = int(split_date[2][0:2])  # hour variable
                minute = int(split_date[2][3:5])  # minute variable

                # EVENT VARIABLES (including the datetime)
                location = split_output[-1]
                date = datetime(year, month, day, hour, minute)
                title = ", ".join(split_output[1:len(split_output)-1])
                content = event.find("span", {"class": "content"}).get_text()
                text = " ".join([paragraph.get_text() for paragraph in event.find("div", {"class": "text-body"}) if paragraph != "\n"])
                
                # APPENDS NEW EVENT CREATED
                self.events.append(Event(date, location, title, content, text))
                

    def getEvents(self):
        return self.events  # returns self.events list
