import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Title, Icon, Size
        self.title('Your Universe')
        self.iconbitmap('images/icon.ico')
        self.geometry('800x600')

        # Create status variable
        self.status = True

        # Create some widgets
        self.my_label = ctk.CTkLabel(self, text="Hello World!", font=("Roboto Condensed", 36))
        self.my_label.pack(pady=20)

        self.my_button = ctk.CTkButton(self, text="Change Text", command=self.change)
        self.my_button.pack(pady=20)
    
        # create a frame outside this function
        My_frame(self)

    def change(self):
        if self.status == True:
            self.my_label.configure(text="Goodbye World!")
            self.status = False
        else:
            self.my_label.configure(text="Hello World!")
            self.status = True

class My_frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Show frame on screen
        self.pack(pady=20)

        # Create buttons
        self.my_button1 = ctk.CTkButton(self, text="Change", command=parent.change)
        self.my_button2 = ctk.CTkButton(self, text="Change", command=parent.change)
        self.my_button3 = ctk.CTkButton(self, text="Change", command=parent.change)

        self.my_button1.grid(row=0, column=0, padx=10, pady=20)
        self.my_button2.grid(row=0, column=1, padx=10, pady=20)
        self.my_button3.grid(row=0, column=2, padx=10, pady=20)

# define and instantiate our app
app = App()
app.mainloop()