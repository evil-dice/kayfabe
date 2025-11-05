import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Title, Icon, Size
        self.title('Your Universe')
        self.iconbitmap('images/icon.ico')
        self.geometry('800x600')

        # create widgets

    
    # create popup function


# define and instantiate our app
app = App()
app.mainloop()