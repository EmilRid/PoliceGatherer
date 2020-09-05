from PoliceGatherer import *


def test_noToken():
    assert TOKEN == ""


def test_noLatest():
    with open("PoliceGatherer/latest.txt", "r") as latest:
        assert latest.read() == ""