import tkinter as tk
from tkinter import messagebox

class MyGui:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)

        self.root.mainloop()

def show_message(self):
    if self.check_state.get() == 0:
        print(self.textbox.get('1.0', tk.END))
    else:
        messagebox.showinfo(title="Message", message=self.textox.get('1.0', tk.END))

MyGui()