# Imports
from csv import DictReader
from tkinter import filedialog

Events = list()
def load_events():
    filename = "data\events.csv"
    events = open(filename, 'r')
    reader = DictReader(events, delimiter=";")
    for event in reader:
        Events.append(event)
    return Events