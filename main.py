# Tutorial stuff from https://www.youtube.com/watch?v=ibf5cx221hk
import tkinter as tk

app = tk.Tk()

# TODO ... Convert to Custom TKinter later
# import customtkinter as ctk
# app = ctk.CTk()



app.title("Kayfabe")
app.geometry("800x500")

label = tk.Label(app, text="Hello World", font=('Calibri', 18) )
label.pack(padx=10, pady=10)

# Multiline Text Box
textbox = tk.Text(app, height=1, padx = 20, font=('Arial', 14))
textbox.pack(padx=10, pady=10)

# Entry
myentry = tk.Entry(app)
myentry.pack(padx=10, pady=10)

# Set of buttons on grid
# Grid layout within button frame
buttonframe = tk.Frame(app)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text = "1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text = "1", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text = "1", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text = "1", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text = "1", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text = "1", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')


# Widget placement exact positioning
anotherbtn = tk.Button(app, text="TEST")
anotherbtn.place(x=200, y=200, height=100, width=100)


# Button
# button = tk.Button(app, text="Click me!", font=('Arial', 18))
# button.pack(padx=10, pady=10)

app.mainloop()