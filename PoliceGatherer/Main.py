from PoliceGatherer import Gatherer
import requests
import json

TOKEN = ''

# pushbullet function
def pushbullet_message(title, body):
    msg = {"type": "note", "title": title, "body": body}
    resp = requests.post('https://api.pushbullet.com/v2/pushes', 
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Error',resp.status_code)
    else:
        print ('Message sent') 
        
# formats message to later be used in pushbullet call
def push_Message(index):
    gatherer.updateEvents()
    title = gatherer.getEvents()[index].title + ", " + gatherer.getEvents()[index].location
    body = str(gatherer.getEvents()[index].date) + "\n" + gatherer.getEvents()[index].text
    pushbullet_message(title, body)

# function to check if latest event is at different time than stored latest
def pushIfNew():
    gatherer.updateEvents()
    latest = open("latest.txt", "r+")
    txtLatest = latest.readline()
    gathLatest = str(gatherer.getEvents()[0].date)
    
    if txtLatest != gathLatest:
        print("True")
        latest.seek(0)
        latest.write(gathLatest)
        push_Message(0)
    latest.close()