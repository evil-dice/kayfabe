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

# Set TTKbootstrap theme


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
        
        
        # Screens
        #TitleScreen(self)
        
        
        self.NavigationPanel = NavigationPanel(self)
        self.MainPanel = MainPanel(self, "Start a New Universe")
        NewUniverse(self.MainPanel)
        
        # Main Content Area

        # Run App
        self.mainloop()

# define and instantiate our app
AppWindow('Squared Circle Universe', (1280,720))