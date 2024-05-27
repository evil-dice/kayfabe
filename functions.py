from customtkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap import constants
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from pathlib import Path


PATH = Path(__file__).parent / 'assets'

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

class img(Canvas):
    def __init__(self, parent, file, width, height):
        super().__init__(parent, file, width, height)
        img_canvas = Canvas(self, width=width, height=height)
        img_canvas.pack(expand=True, fill='both')
        img_canvas.img_file = ImageTk.PhotoImage(file=file)
        img_canvas.create_image(0, 0, image=img_canvas.img_file, anchor='center')
    def stretch_image(event):
        # size
        width = event.width
        height = event.height
        #create an image
        resized_img = img_original.resize((width, height))
        resized_tk = ImageTk.PhotoImage(resized_img)

        # place on the canvas
        canvas.create_image(0,0,image=resized_tk, anchor='nw')

class graphic(Frame):
    def __init__(self, parent, file, width, height):
        super().__init__(parent, file, width, height)

        self.file = file
        self.width = width
        self.height = height

        # build + show logo frame
        ShowGraphicFrame = Frame(self, relief='solid', borderwidth=1)
        ShowGraphicFrame.pack()

        # add graphic canvas
        img_canvas = Canvas(ShowGraphicFrame, width=width, height=height)
        img_canvas.pack(expand=True, fill='both')
        img_canvas.img_file = ImageTk.PhotoImage(file=graphic)
        img_canvas.create_image(0, 0, image=img_canvas.img_file, anchor=NW)


def detailsbox(parent, header, text):
    '''Create a single form entry'''
    container = Frame(parent)
    container.pack(fill='x', expand=False, pady=5)

    # entrytext=ttk.Style()
    # entrytext.configure('TLabel', font=('Convection',12))

    lbl = ttk.Label(container, text=header.title(), style='TLabel')
    lbl.pack(side=TOP, padx=5)

    body = ttk.Label(container, text=text.title())
    body.pack(side=TOP, padx=5)

def datafield(parent, label, variable):
    '''Create a single form entry'''
    container = Frame(parent)
    container.pack(fill='x', expand=False, pady=5)

    entrytext=ttk.Style()
    entrytext.configure('TLabel', font=('Convection',12))

    lbl = ttk.Label(container, text=label.title()+": ", width=15, style='TLabel')
    lbl.pack(side=LEFT, padx=5)

    ent = ttk.Entry(container, textvariable=variable)
    ent.pack(side=LEFT, padx=5, fill='x', expand=True)

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





# For Reference below here, not used
class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter your contact information" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("name", self.name)
        self.create_form_entry("address", self.address)
        self.create_form_entry("phone", self.phone)
        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            #bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            #bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        """Print the contents to console and return the values."""
        print("Name:", self.name.get())
        print("Address:", self.address.get())
        print("Phone:", self.phone.get())
        return self.name.get(), self.address.get(), self.phone.get()

    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()


# class ImageHandler(Frame):
#     def __init__(self, parent):
#         super().__init__()
#         image_files = {
#             'appLogo': 'KayfabeLogo.png',
#             'genericShow': 'genericshow.png',
#             'genericCompany': 'genericcompany.png',
#             'genericWrestler': 'genericwrestler.png',
#             'genericEvent': 'genericevent.png'
#         }

#         self.photoimages = []
#         imgpath = Path(__file__).parent / 'images'
#         for key, val in image_files.items():
#             _path = imgpath / val
#             self.photoimages.append(PhotoImage(name=key, file=_path))