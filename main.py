from customtkinter import *
import sv_ttk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as ttkb
from ttkbootstrap import constants, Style
from classes import *
from functions import *
from styles import *


class AppWindow(Tk):
    def __init__(self, title, size):
        super().__init__()

        # Title, Icon, Size
        self.title(title)
        self.iconbitmap('images/icon.ico')
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        
        # Set TTKBootstrap style
        style = Style(theme='newtheme')

        # Image Handler
        #ImageHandler(AppWindow)
        
        
        # Screens
        self.views = {}
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        for frame in (TitleScreen, ManageUniverse): # list all the frames in the stack here
            f = frame(self)
            f.grid(row=0, column=0, sticky='nsew')
            self.views[frame] = f
        self.switch(TitleScreen) # set the starting frame

    def switch(self, frame):
        self.views[frame].tkraise()




        #TitleScreen(self)
        
        #self.TitleScreen = TitleScreen(self).lift()


        
        #self.ManageUniverse = ManageUniverse(self.MainPanel)
        

        # Main Content Area

        # Run App
        self.mainloop()

# define and instantiate our app
AppWindow('Squared Circle Universe', (1280,720))