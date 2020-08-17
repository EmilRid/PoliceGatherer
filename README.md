# PoliceGatherer
Gathers news and events from the swedish police website from specified location.
Later as desired you can use the ```push_Message(index)``` to push latest event from specified
location in Sweden to your phone as a notification by the PushBullet app.

## Setup
### Beginning 
1. Go onto the https://polisen.se/aktuellt/polisens-nyheter/ website and insert your county name into the "Ange kommun eller län" field.
2. Take the newly generated URL and insert it into the constructor of new Gatherer object. Ex. ```gath = Gatherer(URL)```.
3. Using the ```gath.updateEvents()``` you update the Event object list containing the newest events in that county which is stored in ```gath.events```.
4. Now in Main.py using the ```gath.getEvents()``` function you get a return of the 25 element list of Event objects.
5. For example you can now try out ```print(gath.getEvents()[0].title)``` and it'll print the title of the zeroeth index event in ```gath.events```.
6. Another example is that you can use ```gath.getEvents()[0].print()``` and it'll print the indexed event and its information in formatted fashion.

### Notifications
1. Download the PushBullet app to your phone and sign in using either your Google or Facebook account. (https://www.pushbullet.com/)
2. Get your token at https://www.pushbullet.com/#settings and insert it in the pushbullet_message function "TOKEN" variable in Main.py.
3. If you now want to get a notification on your phone of an event at specific index you need to call ```push_Message(index)```.
4. Hopefully the event at the specified index will now be sent to your phone as a notification by the pushBullet app. 

![Example Code Image](https://github.com/EmilRid/PoliceGatherer/blob/master/ReadMeSrc/ExampleCode.PNG?raw=true)
