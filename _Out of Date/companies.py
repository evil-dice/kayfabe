# Library Imports
from csv import DictReader, DictWriter
from pathlib import Path
import json
from tkinter import *
from tkinter import ttk
import os
from ttkbootstrap.scrolled import ScrolledFrame
from glob import glob

# Local Imports
from functions import *
from classes import *
from shows import Shows, load_all_shows

# Global Variables
Companies = []



# Classes
class Company():
    def __init__(self, name='New Company', alias='', logo='images/genericcompany.png', owner='', saveslot='', savepath=''):
        self.name = name
        self.alias = alias
        self.logo = logo
        self.owner = owner

        # if no alias selected, duplicate name
        if not self.alias:
            self.alias = self.name
        
        # add to global Company list
        global Companies
        Companies.append(self)

        # create new save folder if needed
        self.saveslot = Companies.index(self)
        self.savepath = 'savedata\\' + str(self.saveslot)
        
        # if savepath doesn't exist, create it
        if not os.path.isdir(self.savepath):
            os.makedirs(self.savepath)

class CompanySelectorBasic(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # build Company Selector
        global Companies
        global CurrentCompany
        CurrentCompany = ''

        # create a list to use for drop down
        # AvailableCompanies = []
        # for company in Companies:
        #     AvailableCompanies.append(company.name)

        SelectCompany = ttk.Combobox(self, state='readonly', values=[company.name for company in Companies], style='companyselect.TCombobox')
        SelectCompany.pack(pady=5, expand=True, fill='x')

        def selection_changed(event):
            selection = SelectCompany.get()
            global CurrentCompany
            CurrentCompany = [company.name for company in Companies].index(selection)
            print(CurrentCompany)
            return CurrentCompany
        
        SelectCompany.bind("<<ComboboxSelected>>", selection_changed)

class CompanySelector(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # self configure
        self.configure(relief='groove', borderwidth=0)

        # build containers
        buttons = ttk.Frame(self, padding=10)
        buttons.pack(expand=False, fill='both')

        global Companies

        # buttons for each company
        self.CompanyButtons = []
        self.CompanyNames = []

        # get images for all companies
        for company in Companies:
            self.CompanyButtons.append(ImageTk.PhotoImage(Image.open(company.logo).resize((200, 200))))
            self.CompanyNames.append(company.name)

        # generic image for add new company
        self.CompanyButtons.append(ImageTk.PhotoImage(Image.open('images\genericcompany.png').resize((200, 200))))
        self.CompanyNames.append('New Company...')

        # for company in Companies:
        #     self.CompanyButtons.append(StaticImageBtn(self, company.name, company.logo, lambda: CompanyEditor(company), 250))
        
        # set current selection
        self.currentslot = 0
        self.maxslots = len(self.CompanyButtons) - 1

        # Dynamic label
        self.CompanyToOpen = ttk.Label(self, text=self.CompanyNames[self.currentslot], style='schedule.TLabel', justify='center', anchor='center')
        self.CompanyToOpen.pack(side=TOP, anchor='nw', expand=True, fill='x')
        self.CompanyToOpen.bind('<Configure>', lambda e: self.CompanyToOpen.config(wraplength=self.CompanyToOpen.winfo_width()))

        # Launch menu 
        self.EditUniverse = ttk.Button(buttons, text='Manage', command='', style='nav.TButton')
        self.PlayUniverse = ttk.Button(buttons, text='Play', command='', style='nav.TButton')
        self.DeleteUniverse = ttk.Button(buttons, text='Delete', command='', style='nav.TButton')

        # back button
        Previous = ttk.Button(self, text='<', command=self.Previous, style='secondary.TButton')

        # next button
        Next = ttk.Button(self, text='>', command=self.Next, style='secondary.TButton')

        # render carousel
        Previous.pack(side=LEFT, expand=False, fill='none')
        self.ImageLabel = Label(self, text='', image=self.CompanyButtons[self.currentslot], compound=BOTTOM)
        self.ImageLabel.pack(side=LEFT, expand=True, fill='x')
        Next.pack(side=LEFT, expand=False, fill='none')

        # render buttons
        self.EditUniverse.pack(side=LEFT, expand=True, fill='x', pady=5, padx=(0,10))
        self.PlayUniverse.pack(side=LEFT, expand=True, fill='x', pady=5, padx=(10,10))
        self.DeleteUniverse.pack(side=LEFT, expand=True, fill='x', pady=5, padx=(10,0))

        # set button function if New or existing
        self.New_or_Existing()

    def New_or_Existing(self):
        if self.CompanyNames[self.currentslot] == 'New Company...':
            self.EditUniverse.configure(text='New', command=lambda: load_universe(self.currentslot))
            self.PlayUniverse.configure(state='disabled')
            self.DeleteUniverse.configure(state='disabled')
        else:
            self.EditUniverse.configure(text='Manage', command=lambda: load_universe(self.currentslot))
            self.PlayUniverse.configure(state='normal')
            self.DeleteUniverse.configure(state='normal')

    def Previous(self):
        self.currentslot = self.currentslot - 1
        if self.currentslot < 0:
            self.currentslot = self.maxslots
        self.ImageLabel.configure(image=self.CompanyButtons[self.currentslot])
        self.CompanyToOpen.configure(text=self.CompanyNames[self.currentslot])
        self.New_or_Existing()


    def Next(self):
        self.currentslot = self.currentslot + 1
        if self.currentslot > self.maxslots:
            self.currentslot = 0
        self.ImageLabel.configure(text='', image=self.CompanyButtons[self.currentslot])
        self.CompanyToOpen.configure(text=self.CompanyNames[self.currentslot])
        self.New_or_Existing()
        
    # def load_universe(self):
    #     CurrentCompany = Companies[self.currentslot]
    #     # load shows
    #     load_all_shows(CurrentCompany.savepath)
    #     global Shows
    #     print(Shows)
    #     # load events
    #     # load roster
    #     # etc...

class CompanySelectorSlot(ttk.Frame):
    def __init__(self, parent, companyObject):
        super().__init__(parent)
        '''Create a Slot object that can be used to select a Company to edit or run.'''
        # Set attributes
        self.parent = parent
        self.img = companyObject.logo
        self.text = companyObject.name
        self.width = 250

        # configure slot frame
        self.configure(relief='sunken', borderwidth=0)

        # Slot Label
        slotlabel = ttk.Label(self, text=self.text, anchor='center', style='info.TLabel')
        
        # Slot Image
        CompanyImg = ImageTk.PhotoImage(Image.open(self.img).resize((self.width, self.width)))
        ImageLabel = Label(self, text='', image=CompanyImg)
        ImageLabel.pack()

        
        # render elements
        slotButton.pack(expand=False, fill='x', padx=10, pady=10)
        slotlabel.pack(expand=True, fill='x', padx=5, pady=5)

    def edit_company(self, companyObject):# WIP
        # # select the company
        # Selectedcompany = select_company(companyObject)

        # launch Show Editor
        CompanyEditor(self, companyObject)



class ViewCompanies(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # set background
        background = ResizableImage(self, "images\company.png").pack(expand=True, fill='both')

        # build container
        container = ttk.Frame(self, padding=40)
        container.place(relx=0.5, rely=0.5, anchor='center')

        # load data
        load_all_companies()

        # Section intro
        CompanyDetails = section_details(container, 'Choose a Company','Each Wrestling Universe starts with a Company. Select or create a new Company below to continue.')

        # place elements
        CompanyDetails.grid(row=0, column=0, columnspan=6, sticky='nsew')



class CompanySlot(ttk.Frame):
    def __init__(self, parent, img, btntext, width):
        super().__init__(parent)
        '''Create a Slot object that can be used to select a Company to edit or run.'''
        # Set attributes
        self.parent = parent
        self.img = img
        self.btntext = btntext
        # self.btnaction = btnaction
        self.width = width


        # configure slot frame
        self.configure(relief='sunken', borderwidth=1)

        # Slot Label
        # slotlabel = ttk.Label(self, text='', anchor='center', style='schedule.TLabel')
        # slotlabel.pack(expand=True, fill='x', padx=5, pady=5)

        # Slot Button
        slotButton = StaticImageBtn(self, btntext, img, lambda: edit_company(btntext), width)
        slotButton.pack(expand=False, fill='x', padx=10, pady=10)
    
    def edit_company(self, companyObject):# WIP
        # # select the company
        # Selectedcompany = select_company(companyObject)

        # launch Show Editor
        CompanyEditor(self, companyObject)


# Views
class CompanyEditor(Frame):
    def __init__(self, parent, CompanyToEdit):
        super().__init__(parent)

        self.title('Company Editor')
        #self.geometry('900x600')
        print(CompanyToEdit)
        self.populate_fields(CompanyToEdit)


        

        # build containers
        container = ttk.Frame(self, padding=10)
        container.pack(expand=False, fill='both')

        # build fields
        for key in self.Editor.keys():
            if key in ('logo'):
                imgframe = ttk.LabelFrame(container, text = 'Logo')
                imgframe.pack(side=LEFT, fill='x', expand=False, padx=(0, 20))
                UploadableImage(imgframe, self.Editor[key].get(), self.winfo_reqwidth()).pack(side=LEFT, fill='x', expand=False)
            elif key in ('name', 'alias', 'owner'):
                datafield(container, key, self.Editor[key])

    def populate_fields(self, CompanyToEdit):

        # create dict to hold fields
        self.Editor = {}

        # initialize StringVars
        self.Editor['name'] = StringVar()
        self.Editor['alias'] = StringVar()
        self.Editor['logo'] = StringVar()
        self.Editor['owner'] = StringVar()
        self.Editor['saveslot'] = StringVar()
        self.Editor['savepath'] = StringVar()

        # set values of self.Editor attributes
        self.Editor['name'].set(CompanyToEdit.name)
        self.Editor['alias'].set(CompanyToEdit.alias)
        self.Editor['logo'].set(CompanyToEdit.logo)
        self.Editor['owner'].set(CompanyToEdit.owner)
        self.Editor['saveslot'].set(CompanyToEdit.saveslot)
        self.Editor['savepath'].set(CompanyToEdit.savepath)

        print(CompanyToEdit.__dict__)
        return self.Editor

# functions
# functions
def add_company(**details):
    '''Creates a new Company instance and adds it to the Companies list'''
    global Companies
    # instantiate class and add to list
    Company(**details)

def save_company(companyObject):# Copied from Shows... needs some edits
    '''Saves the Show to the current save's Shows folder in JSON format.'''
    CompanyToSave = {}
    JSONfile = companyObject.savepath + '\company.json'
    for key, value in companyObject.__dict__.items():
        CompanyToSave[key] = value
        output = json.dumps(CompanyToSave, indent=4)
        
        with open(JSONfile, 'w') as datafile:
            datafile.write(output)

def load_company(JSONfile): # works but doesn't save the variables right. 
    '''Creates company object from the company's JSON file in a given save slot.'''
    input = open(JSONfile)
    global Companies
    companyToLoad = json.load(input)
    companyObject = Company(**companyToLoad)
    return companyObject

def load_all_companies():
    '''Creates Show objects from each available JSON file in the current save's Companies directory.'''
    global Companies
    for JSONfile in glob('savedata\*\company.json'):
        load_company(JSONfile)
    return Companies

def load_universe(SaveSlot):
    global Companies
    CurrentCompany = Companies[SaveSlot]
    # load shows
    load_all_shows(CurrentCompany.savepath)
    global Shows
    for show in Shows:
        print(show.title)
    # load events
    # load roster
    # etc...
    from main import app
    app.switch(EditUniverse)

# UI elements
class SaveSlot(Frame):
    def __init__(self, parent, companyName, companyLogo):
        super().__init__(parent)

        # build container
        self.file = Image.open(companyLogo)
        self.file_copy = self.file.copy()
        self.file = self.file_copy.resize((200, 200), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.file)

        button = Button(self, text=companyName, image=self.img, compound=TOP).pack()




