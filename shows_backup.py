# Imports
from csv import DictReader, DictWriter
from pathlib import Path
import json
from tkinter import *
from tkinter import ttk
from functions import *


# Global Variables
Shows = {}
SelectedShow = {}

DaysOfTheWeek = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
        ]


# Classes
class Show():
    def __init__(self, title='New Show', logo='images/genericshow.png', timeslot='', runtime=120, GM='', matchtable='data/matchtables/basic.csv', championships='data/titles.csv'):
        self.title = title
        self.logo = logo
        self.timeslot = timeslot
        self.runtime = runtime
        self.GM = GM
        self.matchtable = matchtable
        self.championships = championships

    def edit(self):
        # set variable for show to pass to editor: 
        ShowToEdit = self.title

        # get dict of elements of the class...
        showVars = self.__dict__.items()
        print(showVars)

        # launch show editor with edited variable list
        ShowEditor(ShowToEdit, showVars)

    def VarsForEditor(self):
        EditorVars = {}
        return EditorVars

    def save(self, EditorVars):
        self.title = EditorVars['title'].get()
        self.logo = EditorVars['logo'].get()
        self.timeslot = EditorVars['timeslot'].get()
        self.runtime = EditorVars['runtime'].get()
        self.GM = EditorVars['GM'].get()
        self.matchtable = EditorVars['matchtable'].get()
        self.championships = EditorVars['championships'].get()

        save_shows()
        load_shows()

class ShowEditor(Toplevel):
    def __init__(self, target, showVars):
        super().__init__()

        self.title('Show Editor')
        #self.geometry('900x600')

        # build containers
        container = ttk.Frame(self, padding=10)
        container.pack(expand=False, fill='both')

        # section label
        # section_details(container, header='Edit Show', text='')

        # add logo canvas ... works, do not edit
        # img_canvas = Canvas(container, width=256, height=256)
        # img_canvas.pack(side=LEFT, padx=5, pady=5, fill='x', expand=False)
        # img_canvas.img_file = ImageTk.PhotoImage(file=Shows[target].logo)
        # img_canvas.create_image(0, 0, image=img_canvas.img_file, anchor=NW)

        # Alternative method with resizing...
        #canvas = Canvas(container, width=256, height=256)
        #canvas.pack(side=TOP, padx=(5,5), pady=20, expand=True, fill='x', anchor='center')
        #imgResize(256, Shows[target].logo)
        # img = Image.open(Shows[target].logo)
        # #img = img.resize((256,256))
        # img = ImageTk.PhotoImage(img)
        # ttk.Label(self, text='', image=img).pack()

        # simple img display
        
        imgframe = ttk.Frame(container)
        imgframe.pack(side=LEFT, expand=False, fill='x')
        self.img = PhotoImage(file=Shows[target].logo)
        showimg = ttk.Label(imgframe, text='', image=self.img)
        showimg.pack(side=LEFT)


        # create_image(128, 128, image=img, anchor='center')

        # img_canvas = Canvas(container, width=256, height=256)
        # img_canvas.pack(side=LEFT, padx=5, pady=5, fill='x', expand=False)

        # img1 = Image.open(Shows[target].logo)
        # resize_image1 = img1.resize((256, 256))
        # img = ImageTk.PhotoImage(resize_image1)
        # img_canvas.create_image(0, 0, image=img, anchor='nw')

        # generate data fields, store vars in list
        self.EditorVars = {}
        

        for key, value in showVars:
            # label = key
            # Specify exceptions that aren't simple data entry
            if key in ('title', 'GM', 'matchtable', 'championships'):
                self.EditorVars[key] = StringVar()
                self.EditorVars[key].set(value)
                datafield(container, key, self.EditorVars[key])
            elif key in ('timeslot'):
                self.EditorVars[key] = StringVar()
                self.EditorVars[key].set(value)
                datafield_dropdown(container, key, self.EditorVars[key], DaysOfTheWeek)
            elif key in ('runtime'):
                self.EditorVars[key] = IntVar()
                self.EditorVars[key].set(value)
                datafield_options(container, key, self.EditorVars[key], ['1 Hour', '2 Hours', '3 Hours'], [60, 120, 180])
            elif key in ('logo'):
                self.EditorVars[key] = StringVar()
                self.EditorVars[key].set(value)
                datafield_image(container, key, self.EditorVars[key])

        # Add / Save / Delete buttons
        FormButtons(container, Add='', Save=lambda: Shows[target].save(self.EditorVars), Delete='')
        # self.EditorVars.values().get()


def import_shows(filename = "data\shows.csv"):
    ''' Imports a CSV file of Shows and creates instances for each in the Shows dictionary'''
    data = open(filename, 'r')
    input = DictReader(data, delimiter=";")
    global Shows
    for show in input:
        add_show(show['title'], **show)
    save_shows()
    load_shows()

def new_show(**details):
    '''Creates a new show and launches an editor window for it.'''
    add_show('New Show', **details)
    Shows['New Show'].edit()

def get_show(target):
    '''Returns SelectedShow if target matches any attribute from a Show object in the Shows list.'''
    global Shows
    global SelectedShow
    for show, object in Shows.items():
        # print(object)
        if target in object.__dict__.values():
            SelectedShow = show
            return SelectedShow
            break

def delete_show(name):
    '''Creates a Show instance and adds it to the Shows dictionary.'''
    global Shows
    # Remove show from memory and Shows dictionary.
    Shows.pop(name)
    save_shows()

def add_show(name, **details):
    '''Creates a Show instance and adds it to the Shows dictionary.'''
    global Shows
    # instantiate class and add to dict
    Shows[name] = Show(**details)

def save_shows():
    '''Saves the Shows list to the current save's shows.json file.'''
    ShowsToSave = {}
    for key, value in Shows.items():
        ShowsToSave[key] = value.__dict__
        output = json.dumps(ShowsToSave, indent=4)
        
        with open('data\shows.json', 'w') as datafile:
            datafile.write(output)
        
    ShowsSchedule.update_shows()

    



def load_shows():
    '''Creates Show objects from shows.json contents and adds them into the Shows dictionary'''
    input = open('data\shows.json')
    global Shows
    ShowsToLoad = json.load(input)
    for key, value in ShowsToLoad.items():
        add_show(key, **value)
    return Shows

# def new_show():
#     add_show('New Show')
#     global SelectedShow
#     SelectedShow = Shows['New Show']
#     LaunchShowEditor()

# def select_show(target):
#     '''Creates a reference to a targeted Show object to edit'''
#     # global SelectedShow
#     SelectedShow = Shows[target]
#     return SelectedShow

# def edit_show(parent, target):
#     ''' Launch the Show Editor window'''
#     select_show(target)
#     ShowEditor(parent)

class ShowsSchedule(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(padding=20)

        # load data
        load_shows()

        # set up grid
        # self.rowconfigure((0,1))
        self.rowconfigure(2, weight=1)
        self.columnconfigure((0,1,2,3,4,5,6), uniform='y', weight=1)

        # create reference list
        global ShowSlots
        ShowSlots = {
            'Monday': None,
            'Tuesday': None, 
            'Wednesday': None,
            'Thursday': None,
            'Friday': None,
            'Saturday': None,
            'Sunday': None
        }

        intro = section_details(self, 'Show Schedule', 'Below, you can see all weekly shows. You must have at least one show defined, and can only have one show per day of the week.')
        intro.grid(row=0, column=0, columnspan=7, sticky='nsew')

        self.update_shows()

    def update_shows(self):

        # destroy previous
        global ShowSlots
        for timeslot in ShowSlots:
            # get a show schduled for a corresponding day
            get_show(timeslot)

            # Add slot for that show
            print(SelectedShow)
            # ShowSlots[timeslot] = ScheduleSlot(self, timeslot, getattr(SelectedShow, 'logo'), getattr(SelectedShow, 'title'), '', 130 )

            # # check for and overwrite add show button if there is a real show
            # for show in Shows:
            #     if Shows[show].timeslot == day:
            #         showButton = StaticImageBtn(ShowSlots[day], Shows[show].title, Shows[show].logo, Shows[show].edit, 130)

            # display the button



            


        
        # configure
        self.configure(relief='solid', borderwidth=1)