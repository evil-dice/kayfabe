# Imports
from csv import DictReader, DictWriter
from pathlib import Path
import json
from tkinter import *
from tkinter import ttk
from functions import *
from glob import glob


# Global Variables
Shows = []
SelectedShow = None

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
        super().__init__()
        
        # define object attributes
        self.title = title
        self.logo = logo
        self.timeslot = timeslot
        self.runtime = runtime
        self.GM = GM
        self.matchtable = matchtable
        self.championships = championships

        # add instance to object master list
        global Shows
        Shows.append(self)


    # def edit(self):
    #     # set variable for show to pass to editor: 
    #     ShowToEdit = self.title

    #     # get dict of elements of the class...
    #     showVars = self.__dict__.items()
    #     print(showVars)

    #     # launch show editor with edited variable list
    #     ShowEditor(ShowToEdit, showVars)

    # def VarsForEditor(self):
    #     EditorVars = {}
    #     return EditorVars

    # def save(self, EditorVars):
    #     self.title = EditorVars['title'].get()
    #     self.logo = EditorVars['logo'].get()
    #     self.timeslot = EditorVars['timeslot'].get()
    #     self.runtime = EditorVars['runtime'].get()
    #     self.GM = EditorVars['GM'].get()
    #     self.matchtable = EditorVars['matchtable'].get()
    #     self.championships = EditorVars['championships'].get()

    #     save_shows()
    #     load_shows()

# functions
def import_shows(filename, delimiter=';'): # Complete
    ''' Imports a CSV file of Shows and creates instances for each in the Shows dictionary'''
    if filename == None:
        filetypes = (
            ('CSV files', '*.csv'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(initialdir="/", title="Select Shows file to import", filetypes=filetypes)
    data = open(filename, 'r')
    input = DictReader(data, delimiter=delimiter)
    global Shows
    for show in input:
        new_show(show['title'], **show)
    return Shows

def new_show(refVar, **showAttributes):# Complete, but not saving reference name variable
    '''Creates a new show.'''
    VarName = refVar
    vars()[VarName] = Show(**showAttributes)
    # select_show(title)
    # edit_show(SelectedShow)

# def select_show_old(showObject):# Works
#     global SelectedShow
#     SelectedShow = showObject
#     return SelectedShow

def select_show(title):# WIP
    global SelectedShow
    for show in Shows:
        if show.title == title:
            SelectedShow = show
    return SelectedShow

def edit_show(title):# WIP
    # select the show
    select_show(title)
    print(SelectedShow)

    # launch Show Editor
    ShowEditor(SelectedShow)

def save_show(showObject):# Complete
    '''Saves the Show to the current save's shows.json file.'''
    ShowToSave = {}
    JSONfile = 'data\\Shows' + showObject.title + '.json'
    for key, value in showObject.__dict__.items():
        ShowToSave[key] = value
        output = json.dumps(ShowToSave, indent=4)
        
        with open(JSONfile, 'w') as datafile:
            datafile.write(output)

def load_show(JSONfile): # works but doesn't save the variables right. 
    '''Creates Show object from a JSON file in the current save slot's Shows folder.'''
    input = open(JSONfile)
    global Shows
    ShowToLoad = json.load(input)
    showObject = Show(**ShowToLoad)
    return showObject

def delete_show(showObject): # works
    select_show(showObject)
    global SelectedShow
    del SelectedShow
    global Shows
    Shows.remove(showObject)

def load_all_shows(savepath):
    '''Creates Show objects from each available JSON file in the current save's Shows directory.'''
    global Shows
    for JSONfile in glob(savepath + '\Shows\*.json'):
        load_show(JSONfile)
    return Shows

class ScheduleSlot(ttk.Frame):
    def __init__(self, parent, label, img, btntext, width):
        super().__init__(parent)
        '''Create a Slot object that can be used to access Shows or Events to edit.'''
        # Set attributes
        self.parent = parent
        self.label = label
        self.img = img
        self.btntext = btntext
        # self.btnaction = btnaction
        self.width = width

        # configure slot frame
        self.configure(relief='sunken', borderwidth=1)

        # Slot Label
        slotlabel = ttk.Label(self, text=label, anchor='center', style='schedule.TLabel')
        slotlabel.pack(expand=True, fill='x', padx=5, pady=5)

        # Slot Button
        slotButton = StaticImageBtn(self, btntext, img, lambda: edit_show(btntext), width)
        slotButton.pack(expand=False, fill='x', padx=10, pady=10)
    
    def edit_show(self, showObject):# WIP
        # # select the show
        # SelectedShow = select_show(showObject)

        # launch Show Editor
        ShowEditor(showObject)

class ViewShows(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(padding=40)

        # load data
        load_all_shows()

        # set up grid
        # self.rowconfigure((0,1))
        self.rowconfigure(2, weight=1)
        self.columnconfigure((0,1,2,3,4,5,6), uniform='y', weight=1)

        # section intro + details
        intro = section_details(self, 'Show Schedule', 'Below, you can see all weekly shows. You must have at least one show defined, and can only have one show per day of the week.')
        intro.grid(row=0, column=0, columnspan=7, sticky='nsew')

        # show schedule
        global ShowSchedule
        ShowSchedule = {
            'Monday': None,
            'Tuesday': None,
            'Wednesday': None,
            'Thursday': None,
            'Friday': None,
            'Saturday': None,
            'Sunday': None
        }

        # populate with generic slots
        count = 0
        for slot in ShowSchedule:
            ShowSchedule[slot] = ScheduleSlot(self, slot, 'images\genericshow.png', 'Add New Show', 130)

            # check if show is in slot and overwrite if so
            for show in Shows:
                if show.timeslot == slot:
                    ShowSchedule[slot] = ScheduleSlot(self, slot, show.logo, show.title, 130)

            # place final resulting slot on grid and increment count
            ShowSchedule[slot].grid(row=1, column=count, sticky='nsew')
            count += 1

        # configure
        self.configure(relief='solid', borderwidth=0)

class ShowEditor(Toplevel):
    def __init__(self, ShowToEdit):
        super().__init__()

        self.title('Show Editor')
        #self.geometry('900x600')
        print(ShowToEdit)
        self.populate_fields(ShowToEdit)
        

        # build containers
        container = ttk.Frame(self, padding=10)
        container.pack(expand=False, fill='both')

        # build fields
        for key in self.Editor.keys():
            if key in ('logo'):
                imgframe = ttk.LabelFrame(container, text = 'Logo')
                imgframe.pack(side=LEFT, fill='x', expand=False, padx=(0, 20))
                UploadableImage(imgframe, self.Editor[key].get(), self.winfo_reqwidth()).pack(side=LEFT, fill='x', expand=False)
            elif key in ('title', 'GM', 'matchtable', 'championships'):
                datafield(container, key, self.Editor[key])
            elif key in ('timeslot'):
                datafield_dropdown(container, key, self.Editor[key], ShowSchedule.keys())
            elif key in ('runtime'):
                datafield_options(container, key, self.Editor[key], self.Editor[key], ['1 Hour', '2 Hours', '3 Hours'], [60, 120, 180])


    def populate_fields(self, ShowToEdit):

        # create dict to hold fields
        self.Editor = {}

        # initialize StringVars
        self.Editor['logo'] = StringVar()
        self.Editor['title'] = StringVar()
        self.Editor['timeslot'] = StringVar()
        self.Editor['runtime'] = IntVar()
        self.Editor['GM'] = StringVar()
        self.Editor['matchtable'] = StringVar()
        self.Editor['championships'] = StringVar()

        # set values of self.Editor attributes
        self.Editor['title'].set(ShowToEdit.title)
        self.Editor['logo'].set(ShowToEdit.logo)
        self.Editor['timeslot'].set(ShowToEdit.timeslot)
        self.Editor['runtime'].set(ShowToEdit.runtime)
        self.Editor['GM'].set(ShowToEdit.GM)
        self.Editor['matchtable'].set(ShowToEdit.matchtable)
        self.Editor['championships'].set(ShowToEdit.championships)

        print(ShowToEdit.__dict__)
        return self.Editor

    def apply_changes(self):
        global SelectedShow

        SelectedShow.title = self.Editor['title'].get()
        SelectedShow.logo = self.Editor['logo'].get()
        SelectedShow.timeslot = self.Editor['timeslot'].get()
        SelectedShow.runtime = self.Editor['runtime'].get()
        SelectedShow.GM = self.Editor['GM'].get()
        SelectedShow.matchtable = self.Editor['matchtable'].get()
        SelectedShow.championships = self.Editor['championships'].get()

        print(SelectedShow.__dict__)
        # print(Shows.index(SelectedShow.timeslot))