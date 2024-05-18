from customtkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap import constants
from tkinter import *
from PIL import Image,ImageTk

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
