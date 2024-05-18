import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

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
        self.my_label = ctk.CTkLabel(self, text="Enter your name:", font=("Roboto Condensed", 24))
        self.my_label.pack(pady=20)

        self.my_entry = ctk.CTkEntry(self, width=130, font=("Roboto Condensed", 24))
        self.my_entry.pack(pady=20)

        self.my_button = ctk.CTkButton(self, text="Popup", command=self.popup)
        self.my_button.pack(pady=20)
    
    # create popup function
    def popup(self):
        if self.my_entry.get():
            messagebox.showinfo("Hello", f"Hello {self.my_entry.get()}")
        else:
            messagebox.showerror("Error", "You didn't type anything dude.")

# define and instantiate our app
app = App()
app.mainloop()