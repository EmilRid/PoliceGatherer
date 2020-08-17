from Gatherer import Gatherer

def get_contacts(filename):
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split()[1])
    return emails

gatherer = Gatherer("https://polisen.se/aktuellt/polisens-nyheter?requestId=1597518822273&lpfm.loc=Stockholm")

gatherer.updateEvents()
for event in gatherer.getEvents():
    event.print()