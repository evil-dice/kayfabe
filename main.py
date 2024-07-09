from customtkinter import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as ttkb
from ttkbootstrap import constants, Style

# Local Imports
from functions import *
from classes import *
from companies import *
from shows import *
from roster import *

load_all_companies()
#load_all_shows()
#load_roster()

class AppWindow(Tk):
    def __init__(self, title, size):
        super().__init__()

        # Title, Icon, Sizez
        self.title(title)
        self.iconbitmap('images/icon.ico')
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        
        # Set TTKBootstrap style
        global style
        style = Style(theme='newtheme')
        set_styles(style)
        
        
        # Screens
        # Some alternative methods...
        # https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
        self.views = {}
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        for frame in (TitleScreen, EditUniverse, PlayUniverse): # list all the frames in the stack here
            f = frame(self)
            f.grid(row=0, column=0, sticky='nsew')
            self.views[frame] = f
        self.switch(TitleScreen) # set the starting frame

    def switch(self, frame):
        self.views[frame].tkraise()

        # Run App
        self.mainloop()

# define and instantiate our app
app = AppWindow('Squared Circle Universe', (1280,720))