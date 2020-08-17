from Gatherer import Gatherer
import requests
import json

# pushbullet function
def pushbullet_message(title, body):
    msg = {"type": "note", "title": title, "body": body}
    TOKEN = ''
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
    
#Gatherer object with Stockholm specified 
gatherer = Gatherer("https://polisen.se/aktuellt/polisens-nyheter?requestId=0&lpfm.loc=Stockholm")

push_Message(0)