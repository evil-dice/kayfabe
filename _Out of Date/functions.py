from customtkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap import constants
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from pathlib import Path
import os


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

PATH = Path(__file__).parent / 'assets'

# widgets

class StaticImageBtn(Frame):
    def __init__(self, parent, text, filepath, commandtorun, maxsize):
        super().__init__(parent)
        # build container

        # open image
        file = Image.open(filepath)
        file.thumbnail((maxsize, maxsize))
        self.img = ImageTk.PhotoImage(file)

        render = ttk.Button(self, text=text, image=self.img, compound=TOP, command=commandtorun, style='dark.TButton')
        render.pack(expand=True, fill='both')

class UploadableImage(Frame):
    def __init__(self, parent, filepath, maxsize):
        super().__init__(parent)
        # build container

        # open image
        file = Image.open(filepath)
        file.thumbnail((maxsize, maxsize))
        self.img = ImageTk.PhotoImage(file)
        self.render = Label(self, text='', image=self.img)
        self.render.pack(expand=True, fill='both')

        # browse button
        browse = ttk.Button(self, text='Browse', command=lambda: self.browse(maxsize))
        browse.pack(padx=5, fill='x', expand=True)

    def browse(self, maxsize):
        fileTypes = [("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.tif")]
        filepath = filedialog.askopenfilename(filetypes=fileTypes)

        # if file is selected
        if len(filepath):
            file = Image.open(filepath)
            file.thumbnail((maxsize, maxsize))
            self.updatedimg = ImageTk.PhotoImage(file)
            self.render.configure(image=self.updatedimg)

class StaticImage(Frame):
    def __init__(self, parent, filepath, maxsize):
        super().__init__(parent)
        # build container

        # open image
        file = Image.open(filepath)
        file.thumbnail((maxsize, maxsize))
        # elif self.file.size[0] < parent.winfo_width:

        self.img = ImageTk.PhotoImage(file)
        render = Label(self, text='', image=self.img)
        render.pack(expand=True, fill='both')

class ResizableImage(Frame):
    def __init__(self, parent, filepath):
        super().__init__(parent)
        # build container
        # self.pack(expand=True, fill='both')

        # display image
        self.file = Image.open(filepath)
        self.file_copy = self.file.copy()
        self.img = ImageTk.PhotoImage(self.file)
        self.render = Label(self, text='', image=self.img)
        self.render.pack(side=RIGHT, anchor='nw', expand=True, fill='both')

        self.render.bind('<Configure>', self.resize_image)

    def resize_image(self, event):
        # get original size and aspect ratio
        OrigSize = (self.winfo_width(), self.winfo_height())
        AspectRatio = (OrigSize[0] / OrigSize[1])

        # resize image with aspect ratio
        # Calculate new size keeping the aspect ratio
        if (self.winfo_width() / self.winfo_height()) > AspectRatio:
            new_width = int(self.winfo_height() * AspectRatio)
            new_height = self.winfo_height()
        else:
            new_width = self.winfo_width()
            new_height = int(self.winfo_width() / AspectRatio)

        # Resize the image...FIX THIS AND WERE GOOD TO GO
        self.file = self.file_copy.resize((new_width, new_height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.file)
        self.render.configure(image=self.img)

class ResizableImageBtn(Frame):
    def __init__(self, parent, text, filepath, commandtorun):
        super().__init__(parent)
        # build container
        # self.pack(expand=True, fill='both')

        # display image
        self.file = Image.open(filepath)
        self.file_copy = self.file.copy()
        self.img = ImageTk.PhotoImage(self.file)
        self.render = Button(self, text=text, image=self.img, compound='top', command=commandtorun)
        

        self.render.bind('<Configure>', self.resize_image)

    def resize_image(self, event):
        # get original size and aspect ratio
        OrigSize = (self.winfo_width(), self.winfo_height())
        AspectRatio = (OrigSize[0] / OrigSize[1])

        # resize image with aspect ratio
        # Calculate new size keeping the aspect ratio
        if (self.winfo_width() / self.winfo_height()) > AspectRatio:
            new_width = int(self.winfo_height() * AspectRatio)
            new_height = self.winfo_height()
        else:
            new_width = self.winfo_width()
            new_height = int(self.winfo_width() / AspectRatio)

        # Resize the image...FIX THIS AND WERE GOOD TO GO
        self.file = self.file_copy.resize((new_width, new_height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.file)
        self.render.configure(image=self.img)

class EditableLabel(Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.entry = Entry(self)
        self.bind("<Double-1>", self.edit_start)
        self.entry.bind("<Return>", self.edit_stop)
        self.entry.bind("<FocusOut>", self.edit_stop)
        self.entry.bind("<Escape>", self.edit_cancel)

    def edit_start(self, event=None):
        self.entry.place(relx=.5, rely=.5, relwidth=1.0, relheight=1.0, anchor="center")
        self.entry.focus_set()

    def edit_stop(self, event=None):
        self.configure(text=self.entry.get())
        self.entry.place_forget()

    def edit_cancel(self, event=None):
        self.entry.delete(0, "end")
        self.entry.place_forget()


# styles
def set_styles(style):
    global fonts, stylesheet, space, frames, buttons

    fonts = {
        'headers': 'Freedom45',
        'body': 'Lato',
        'stylized': 'Royal Rumble'
    }

    stylesheet = {
        'h1': {'style': 'h1.TLabel', 'font': (fonts['headers'], 36), 'anchor': 'w', 'justify': 'left'},
        'h2': {'style': 'h2.TLabel', 'font': (fonts['headers'], 24), 'anchor': 'w', 'justify': 'left'},
        'body': {'style': 'body.TLabel', 'font': (fonts['body'], 12), 'anchor': 'w', 'justify': 'left'},
        'field': {'style': 'field.TLabel', 'font': (fonts['body'], 12), 'anchor': 'w', 'justify': 'left', 'width': 15},
        'schedule': {'style': 'schedule.TLabel', 'font': (fonts['stylized'], 26), 'anchor': 'center', 'justify': 'center'},
        'companyselect': {'style': 'companyselect.TCombobox', 'font': (fonts['body'], 20), 'anchor': 'center', 'arrowsize': 25},
        'nav': {'style': 'nav.TButton', 'font': (fonts['stylized'], 20), 'anchor': 'center', 'justify': 'center'}
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


class section_details(Frame):
    def __init__(self, parent, header, text):
        super().__init__(parent)
        '''Create a header and brief description'''
        # container = Frame(parent)
        # container.pack(fill='x', expand=False, pady=5)

        header = ttk.Label(self, text=header, style='h1.TLabel')
        header.pack(side=TOP)
        header.bind('<Configure>', lambda e: header.config(wraplength=header.winfo_width()))

        if text:
            header.pack(side=TOP, **space['h1'])
            bodytext = ttk.Label(self, text=text, style='body.TLabel')
            bodytext.pack(side=TOP, **space['body'])
            bodytext.bind('<Configure>', lambda e: bodytext.config(wraplength=bodytext.winfo_width()))

# ??? Should I redefine datafields as classes to try and directly address data content? 

def datafield(parent, label, variable):
    '''Create a single form entry with either Stringvar or IntVar.'''
    # build container
    container = Frame(parent)
    container.pack(fill='x', expand=False, pady=5)

    # create label
    entrylbl = ttk.Label(container, text=label.title()+": ", style='field.TLabel', width=15)
    entrylbl.pack(side=LEFT, padx=5, fill='both', expand=True)

    # # create TK special variable
    # if Int == False:
    #     EditorVars[label] = StringVar()
    #     EditorVars[label].set(variable)
    # elif Int == True:
    #     EditorVars[label] = IntVar()
    #     EditorVars[label].set(variable)

    # create entry field
    ent = ttk.Entry(container, textvariable=variable)
    # ent.delete(0, END)
    # ent.insert(0, value)
    ent.pack(side=LEFT, padx=5, fill='x', expand=True)


def datafield_image(parent, label, variable, imagefile, maxsize):
    '''Create an image with an update button to edit it.'''
    # build container
    container = Frame(parent)
    container.pack(fill='x', expand=False, pady=5)

    # create label
    labelframe = ttk.LabelFrame(container, text=label.title())
    labelframe.pack(side=LEFT, padx=5, pady=5, fill='x', expand=False)

    # create image from original value
    img = StaticImage(labelframe, imagefile, maxsize)
    img.pack()

    # browse button
    browse = ttk.Button(labelframe, text='Browse', command=lambda: browsebtn())
    browse.pack(padx=5, fill='x', expand=True)

    def browsebtn():
        fileTypes = [("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.tif")]
        filepath = filedialog.askopenfilename(filetypes=fileTypes)

        # if file is selected
        if len(filepath):
            img = StaticImage(labelframe, filepath, maxsize)
            img.pack()
    



def datafield_file(parent, label, variable):
    '''Create a single form entry'''
    # build container
    container = Frame(parent)
    container.pack(fill='x', expand=False, pady=5)

    # create label
    entrylbl = ttk.Label(container, text=label.title()+": ", style='field.TLabel', width=15)
    entrylbl.pack(side=LEFT, padx=5, fill='x', expand=False)

    # create TK special variable
    # EditorVars[label] = StringVar()
    # EditorVars[label].set(variable)

    # create entry field
    ent = ttk.Entry(container, textvariable=variable)
    # ent.delete(0, END)
    # ent.insert(0, value)
    ent.pack(side=LEFT, padx=5, fill='x', expand=True)

    # browse button
    browse = ttk.Button(container, text='Browse', command=lambda: browsebtn())
    browse.pack(side=LEFT, padx=5, fill='x', expand=True)

    def browsebtn():
        fileTypes = [("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.tif")]
        filepath = filedialog.askopenfilename(filetypes=fileTypes)
        ent.delete(0, END)
        ent.insert(END, filepath) # add this

        # get new image name to update image
        # ent.get()

    # def imageUploader():
    #     fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    #     path = filedialog.askopenfilename(filetypes=fileTypes)
    
    #     # if file is selected
    #     if len(path):
    #         img = Image.open(path)
    #         img = img.resize((200, 200))
    #         pic = ImageTk.PhotoImage(img)
    
    #         # re-sizing the app window in order to fit picture
    #         # and buttom
    #         app.geometry("560x300")
    #         label.config(image=pic)
    #         label.image = pic
 
    # # if no file is selected, then we are displaying below message
    # else:
    #     print("No file is Choosen !! Please choose a file.")
    


def datafield_dropdown(parent, label, variable, valuelist, Int=False):
    '''Create a single form entry with a combo box'''
    container = Frame(parent)
    container.pack(fill='x', expand=False, pady=5)

    entrylbl = ttk.Label(container, text=label.title()+": ", style='field.TLabel', width=15)
    entrylbl.pack(side=LEFT, padx=5, fill='x', expand=False)

    # if Int == False:
    #     EditorVars[label] = StringVar()
    #     EditorVars[label].set(variable)
    # elif Int == True:
    #     EditorVars[label] = IntVar()
    #     EditorVars[label].set(variable)

    ent = ttk.Combobox(container, textvariable=variable, values=valuelist, style='CompanySelect.TCombobox')
    # ent.set(value)
    ent.pack(side=LEFT, padx=5, fill='x', expand=True)


def datafield_options(parent, label, variable, btnvariable, btnText, btnValues):
    '''Create a single form entry with radio buttons for options'''
    container = Frame(parent)
    container.pack(fill='x', expand=False, pady=5)

    entrylbl = ttk.Label(container, text=label.title()+": ", style='field.TLabel', width=15)
    entrylbl.pack(side=LEFT, padx=(5,10), fill='x', expand=False)

    # if Int == False:
    #     EditorVars[label] = StringVar()
    #     EditorVars[label].set(variable)
    # elif Int == True:
    #     EditorVars[label] = IntVar()
    #     EditorVars[label].set(variable)

    for button, value in zip(btnText, btnValues):
        rbtn = ttk.Radiobutton(container, text=button, textvariable=variable, variable=btnvariable, value=value, style='light.Outline.Toolbutton')
        rbtn.pack(side=LEFT, fill='x', expand=True)


def FormButtons(parent, **kwargs):
    '''Generic buttons to Add, Save, or Delete the relevant item in saved datafiles'''
    container = Frame(parent)
    container.pack(fill='x', expand=True, padx=20, pady=20, anchor='center')

    for key, value in kwargs.items():
        btn = ttk.Button(container, text=key, command=value)
        btn.pack(side=LEFT, anchor='center', padx=5, expand=True, fill='x')
        
    cancel = ttk.Button(container, text="Cancel", command=parent.destroy)
    cancel.pack(side=LEFT, anchor='center', padx=5, expand=True, fill='x')

def datafield_alt(parent, label, variable):
    '''Create a single form entry'''
    container = Frame(parent)
    container.pack(fill='x', expand=True, pady=5)

    entrytext=ttk.Style(container)
    entrytext.configure('my.TLabel', font=('Convection',12))

    lbl = ttk.Label(container, text=label.title(), style='my.TLabel')
    lbl.pack(side=TOP, padx=5)

    ent = ttk.Entry(container, textvariable=variable)
    ent.pack(side=TOP, padx=5, fill='x', expand=True)

# lifted from online, modify to fit our use case for uploading show logos
def imageUploader(imageObj):
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.tif")]
    path = filedialog.askopenfilename(filetypes=fileTypes)
 
    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((256, 256))
        pic = ImageTk.PhotoImage(img)
        imageObj.config(image=pic)
        imageObj.image = pic
 
    # # if no file is selected, then we are displaying below message
    # else:
    #     print("No file is Choosen !! Please choose a file.")