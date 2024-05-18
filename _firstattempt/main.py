# Tutorial stuff from https://www.youtube.com/watch?v=ibf5cx221hk
# Doing Custom TKinter based off this: https://www.youtube.com/watch?v=30L3pJ73TSY&t
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from csv import DictReader
from PIL import Image, ImageTk

from roster import FullRoster, load_roster, view_roster
#from testcases import testmatch

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self, title, size):

        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])

        # widgets
        self.top = TopPanel(self, fg_color='transparent')
        self.left = LeftPanel(self, border_width=1)
        self.main = MainFrame(self, fg_color='transparent', border_width=1)
        self.right = RightPanel(self)
        self.bottom = BottomPanel(self)

        # set up grid
        self.columnconfigure((0), weight = 1)
        self.columnconfigure((1), weight = 5)
        self.columnconfigure((2), weight = 2)
        self.rowconfigure((1), weight = 1, pad=20)

        # run
        self.mainloop()

class TopPanel (ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.grid(row = 0, column = 0, columnspan = 3, padx = (0,10), pady = (0,0), sticky = 'ew')
        self.create_widgets()
    
    def create_widgets(self):

        # create the widgets
        img_logo = ctk.CTkImage(Image.open('images\KayfabeLogo.png'), size=(300,75))


        # create the grid
        #self.columnconfigure((0), weight = 1, uniform = 'a')
        #self.rowconfigure((0,1,2), weight = 1, uniform = 'a')

        # place the widgets
        logo = ctk.CTkLabel(self, text="", image=img_logo, width=320, height=85)
        logo.grid(row = 0, column = 0, padx = 0, pady = (0,10), sticky = 'w')

class LeftPanel (ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.grid(row = 1, column = 0, padx = (0,10), pady = (0,0), sticky = 'nsew')
        self.create_widgets()
    
    def create_widgets(self):

        # create the widgets
        menu_label = ctk.CTkLabel(self, text="OPTIONS", font=('Conduit ITC', 24), fg_color='black')
        button1 = ctk.CTkButton(self, text = "Load Roster", command = load_roster)
        button2 = ctk.CTkButton(self, text = "Show Roster", command = view_roster)

        # create the grid
        self.columnconfigure((0), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2), weight = 0, uniform = 'a')

        # place the widgets
        menu_label.grid(row = 0, column = 0, padx = 0, pady = (0,10), sticky = 'new')
        button1.grid(row = 1, column = 0, padx = 5, pady = 10, sticky = 'n')
        button2.grid(row = 2, column = 0, padx = 5, pady = 10, sticky = 'n')

class RightPanel (ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row = 1, column = 2, padx = (0,10), pady = (0,0), sticky = 'nsew')
        self.create_widgets()
    
    def create_widgets(self):

        # create the widgets
        for character in FullRoster:
            user_button = ctk.CTkButton(self, text=character, command=lambda name=character: self.a(name))

        # create the grid
        #self.columnconfigure((0), weight = 1)
        #self.rowconfigure((0,1,2), weight = 1)

        # place the widgets


class MainFrame (ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.grid(row = 1, column = 1, padx = 0, pady = (0,0), sticky = 'nsew')
        self.create_widgets()
        matchside = element_side(self,'Wrestler1')

    def create_widgets(self):

        # create the widgets
        main_label = ctk.CTkLabel(self, text="OPTIONS", font=('Conduit ITC', 24))
        button_test = ctk.CTkButton(self, text = "Test Side Builder")

        # create the grid
        #self.columnconfigure((0), weight = 1, pad=20)
        #self.rowconfigure((0,1,2), weight = 1, pad=20)

        # place the widgets
        main_label.pack()
        button_test.pack()
        matchside.pack()

class BottomPanel (ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row = 3, column = 0, columnspan = 3, padx = (0,10), pady = (0,0), sticky = 'nsew')
        self.create_widgets()
    
    def create_widgets(self):

        # create the widgets
        menu_label = ctk.CTkLabel(self, text="Kayfabe.io by Rob Walker", font=('Calibri', 18))

        # create the grid
        #self.columnconfigure((0), weight = 1, uniform = 'a')
        #self.rowconfigure((0,1,2), weight = 1, uniform = 'a')

        # place the widgets
        menu_label.grid(row = 0, column = 0, padx = 0, pady = (0,10), sticky = 'ew')

# Classes for Match elements
class element_participant(ctk.CTkButton):
    def __init__(self, parent, participant):
        super().__init__(parent)
        self.pack()

    def create_widgets(self):
        participant = ctk.CTkButton(self, text = participant, font=('Conduit ITC', 18))
        participant.pack()

class element_side(ctk.CTkFrame):
    def __init__(self, parent, participants):
        super().__init__(parent, participants)
        self.participants = []
        self.pack(side = TOP, expand = False, fill = NONE, ipadx = 10, ipady = 10, padx = 20, pady = 20)

    def create_widgets(self):
        for participant in participants:
            wrestler = element_participant(self, participant)
            wrestler.pack(side = 'TOP', expand = False, padx = 10, pady = 5)

class match_1v1(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the widgets

        # matchtype info
        self.description = ""
        self.matchrules = ctk.CTkLabel(self, text=self.description)
        self.matchrules.pack(side = LEFT, expand = FALSE, padx = 20, pady = 20)

App('Kayfabe.io', (800,600))x