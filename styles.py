from customtkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap import constants
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from pathlib import Path
import os

# styles
def set_styles(style):
    global fonts, stylesheet, space, frames, buttons

    fonts = {
        'headers': 'Bebas Neue',
        'body': 'Lato',
        'stylized': 'Royal Rumble'
    }

    stylesheet = {
        'h1': {'style': 'h1.TLabel', 'font': (fonts['headers'], 36), 'anchor': 'w', 'justify': 'left'},
        'h2': {'style': 'h2.TLabel', 'font': (fonts['headers'], 24), 'anchor': 'w', 'justify': 'left'},
        'body': {'style': 'body.TLabel', 'font': (fonts['body'], 12), 'anchor': 'w', 'justify': 'left'},
        'field': {'style': 'field.TLabel', 'font': (fonts['body'], 12), 'anchor': 'w', 'justify': 'left', 'width': 15},
        'schedule': {'style': 'schedule.TLabel', 'font': (fonts['stylized'], 26), 'anchor': 'center', 'justify': 'center'},
        'companyselect': {'style': 'companyselect.TCombobox', 'font': (fonts['body'], 20), 'anchor': 'center'}
    }

    buttons = {
        'slot': {'style': 'slot.TButton', 'font': (fonts['headers'], 20), 'anchor': 's', 'justify': 'center'}
    }

    space = {
        'h1': {'padx': 0, 'pady': (0,10), 'expand': 'False', 'fill': 'x'},
        'h2': {'padx': 0, 'pady': (0,10), 'expand': 'False', 'fill': 'x'},
        'body': {'padx': 0, 'pady': (0,20), 'expand': 'False', 'fill': 'x'},
        'entry': {'padx': 20, 'pady': (0,20), 'expand': 'False', 'fill': 'x'}
    }

    frames = {
        'blackBG': {'background': '000000'}
    }
    
    for element in stylesheet.values():
        style.configure(**element)