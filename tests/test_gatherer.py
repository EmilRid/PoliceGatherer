from PoliceGatherer import * 
import pytest
import requests

gatherer = Gatherer("https://polisen.se/aktuellt/polisens-nyheter?requestId=1597518822273&lpfm.loc=Stockholm")

def test_noToken():
    assert TOKEN == ""

def test_noLatest():
    with open("PoliceGatherer/latest.txt", "r") as latest:
        assert latest.read() == ""

def test_url():
    assert requests.get(gatherer.source).status_code == 200

def test_eventList():
    gatherer.updateEvents()
    assert isinstance(gatherer.getEvents(), list)

def test_containsEvents():
    gatherer.updateEvents()
    assert len(gatherer.getEvents()) != 0
