# Imports
from csv import DictReader,DictWriter
from tkinter import *
from tkinter import ttk


# Global Variables
AllShows = list()
CurrentShow = ''

# Classes
class Show():
    def __init__(self, showtitle='', logo='images/genericshow.png', timeslot='', runtime=120, GM='', matchtable='data/matchtables/basic.csv'):
        self.showtitle = showtitle
        self.logo = logo
        self.timeslot = timeslot
        self.runtime = runtime
        self.GM = GM
        self.matchtable = matchtable



def load_shows():
    datafile = "data\shows.csv"
    datafile_open = open(datafile, 'r')
    datafile_content = DictReader(datafile_open, delimiter=";")
    for show in datafile_content:
        AllShows.append(show)
    return AllShows

def view_shows():
    for show in AllShows:
        print(show)

# [Add Show] Add a show to all shows
def add_show(showtitle='', logo='images/genericshow.png', timeslot='', runtime=120, GM='', matchtable='data/matchtables/basic.csv'):
    new_show = Show(showtitle, logo, timeslot, runtime, GM, matchtable)
    new_show = new_show.__dict__
    AllShows.append(new_show)
    # save_shows()
    # load_shows()
    print(AllShows)


# [Select Show] Selects a show from all shows
# def select_show(showtitle):
#     # pull show based on selection
#     global SelectedShow
#     SelectedShow = next(show for show in AllShows if show["showtitle"] == showtitle)
#     return SelectedShow

# [Delete Show] Removes show from all shows
def delete_show(showtitle):
    for show in AllShows:
        if show['showtitle'] == showtitle:
            AllShows.remove(show)
    save_shows()

# [Save Shows] Saves current shows to shows.csv datafile
def save_shows():
    keys = AllShows[0].keys()

    with open("data\shows.csv", 'w', newline='') as datafile:
        writer = DictWriter(datafile, fieldnames=keys, delimiter=';')
        writer.writeheader()
        writer.writerows(AllShows)




# TESTING
'''
load_shows()
get_show('Dynamite')
add_show(title='RAW', timeslot='Monday', runtime='180')
delete_show
view_shows()
save_shows()

title;logo;timeslot;runtime;GM;matchtable
Dynamite,images\dynamite.png;Wednesday;120;Tony Khan;matchtables\basic.csv
Collision,images\collision.png;Saturday;120;Tony Khan;matchtables\basic.csv

'''


