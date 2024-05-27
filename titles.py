# Imports
from csv import DictReader,DictWriter
from tkinter import filedialog


# Global Variables
AllTitles = list()
CurrentShowTitles = list()

# Classes
class Title():
    def __init__(self, titleName='', holderName='', currentChampion='', onShows=(), level='', division='', stipulation='', image='images\titles\generictitle.png'):
        super().__init__()
        self.titleName = titleName
        self.holderName = holderName
        self.currentChampion = currentChampion
        self.onShows = onShows
        self.level = level
        self.division = division
        self.stipulation = stipulation
        self.image = image



def load_titles():
    datafile = "data\Titles.csv"
    datafile_open = open(datafile, 'r')
    datafile_content = DictReader(datafile_open, delimiter=";")
    for title in datafile_content:
        AllTitles.append(title)
    return AllTitles

def view_titles():
    for title in AllTitles:
        print(title)

# [Add title] Add a title to all titles
def add_title(titleName='', holderName='', currentChampion='', onShows=(), level='', division='', stipulation='', image='images\titles\generictitle.png'):
    new_title = Title(titleName, holderName, currentChampion, onShows, level, division, stipulation, image)
    new_title = new_title.__dict__
    AllTitles.append(new_title)
    save_titles()


# [Select Show] Selects a show from all shows
def get_title(titleName):
    global CurrentShow
    global CurrentShowTitles
    CurrentShowTitles = AllTitles
    CurrentShowTitles = [x for x in AllTitles if CurrentShow['title'] in x['onShows']]
    return CurrentShowTitles

# [Delete Show] Removes show from all shows
def delete_title(title):
    for show in AllTitles:
        if show['title'] == title:
            AllTitles.remove(show)
    save_titles()

# [Save Shows] Saves current shows to shows.csv datafile
def save_titles():
    keys = AllTitles[0].keys()

    with open("data\titles.csv", 'w', newline='') as datafile:
        writer = DictWriter(datafile, fieldnames=keys, delimiter=';')
        writer.writeheader()
        writer.writerows(AllTitles)



# TESTING
'''
load_titles()
get_title('TBS Championship')
add_title(title='Rampage', timeslot='Friday', runtime='60')
delete_title
view_titles()
save_titles()

title;logo;timeslot;runtime;GM;matchtable
Dynamite,images\dynamite.png;Wednesday;120;Tony Khan;matchtables\basic.csv
Collision,images\collision.png;Saturday;120;Tony Khan;matchtables\basic.csv

'''


