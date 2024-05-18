# Imports
from csv import DictReader
from tkinter import filedialog

Shows = list()
def load_shows():
    filename = "data\shows.csv"
    shows = open(filename, 'r')
    reader = DictReader(shows, delimiter=",")
    for show in reader:
        Shows.append(show)
    return Shows