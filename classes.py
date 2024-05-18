from customtkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap import constants#
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from styles import *
from roster import *
from shows import *
from events import *
from functions import EditableLabel

# class functions
def ShowEditorWindow(parent):
    ''' Allows launch of Show Editor window '''
    global edit_show
    edit_show = ShowEditor(parent)

# Startup Screens
class TitleScreen(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # widgets
        self.img = PhotoImage(file="images\Titlescreen.png")
        showimg = ttk.Label(self, text='', image=self.img)

        self.mainmenu = Frame(self)
        menu_options = {
            'NEW UNIVERSE': 'new_universe',
            'CONTINUE UNIVERSE': 'continue_universe',
            'LOAD UNIVERSE': 'load_universe',
            'SAVE UNIVERSE': 'save_universe',
            'RESET UNIVERSE': 'reset_universe'
        }

        for key, var in menu_options.items():
            Button(self.mainmenu, text=key, font=('Royal Rumble', 24)).pack(pady=5, expand=True, fill='x')

        # place widgets
        self.mainmenu.place(x=150, y=350, width=350)
        showimg.pack(side=RIGHT, anchor='se')


        # build and position frame
        self.configure(relief='solid', borderwidth=1, width=1280, height=720)
        self.pack(expand=False, fill='none', padx=50, pady=50)

class Company(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.rowconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.columnconfigure((0), weight=1)
        
        # create widgets
        companyNamelabel = Label(self, text='Company Name', font=('Conduit ITC',14))
        companyName = Entry(self, font=('Conduit ITC',14))

        companyName_Shortlabel = Label(self, text='Acronym / Short Name', font=('Conduit ITC',14))
        companyName_Short = Entry(self, font=('Conduit ITC',14))

        companyOwnerlabel = Label(self, text='Currently Owned by', font=('Conduit ITC',14))
        companyOwner = Entry(self, font=('Conduit ITC',14))

        companyLogolabel = Label(self, text='Company Logo (512x512)', font=('Conduit ITC',14))
        companyLogo = Button(self, font=('Conduit ITC',14), text='Browse')

        # place widgets
        companyNamelabel.grid(row=0,column=0,sticky='nsew', padx=20, pady=(20,0))
        companyName_Shortlabel.grid(row=2,column=0,sticky='nsew', padx=20, pady=(20,0))
        companyOwnerlabel.grid(row=4,column=0,sticky='nsew', padx=20, pady=(20,0))
        companyLogolabel.grid(row=6,column=0,sticky='nsew', padx=20, pady=(20,0))

        companyName.grid(row=1,column=0,sticky='ew', padx=20, pady=(0,20))
        companyName_Short.grid(row=3,column=0,sticky='ew', padx=20, pady=(0,20))
        companyOwner.grid(row=5,column=0,sticky='ew', padx=20, pady=(0,20))
        companyLogo.grid(row=7,column=0,sticky='ew', padx=20, pady=(0,20))

        # configure
        self.configure(padx=20, pady=20, relief='solid', borderwidth=1)
        
class Show(Frame):
    def __init__(self, parent, title='', logo='images\genericshow.png', timeslot='', runtime=120, GM='', matchtable='data/matchtables/basic.csv'):
        super().__init__(parent)

        # build widgets
        self.title

        self.logo

        self.timeslot

        self.runtime

        self.GM
        
        #self.matchtable




class ShowsSchedule(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # load data
        load_shows()

        # set up grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self.columnconfigure((0,1,2,3,4,5,6), uniform='y', weight=1)

        # set ttk styles
        showNames = ttk.Style()
        showNames.configure('showNames.TButton', font=('snes', 14))

        # add widgets
        count = 0
        DaysOfTheWeek = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
        ]

        for day in DaysOfTheWeek:
            ttk.Label(self, text=day, font=('Conduit ITC',12), anchor='center', style='inverse-secondary').grid(row=0, column=count, sticky='nsew', padx=5, pady=5)
            #ttk.Label(self, text='No shows booked', style='secondary').grid(row=1, column=count, sticky='nsew', padx=5, pady=0)
            showlogo = ttk.Button(self, text="Click to\nadd a\nshow", style='outline.Secondary.TButton', padding=5, command=lambda: ShowEditorWindow(self))
            showlogo.grid(row=1, column=count, sticky='nsew', padx=5, pady=0)
            
            for Show in Shows:
                if Show['timeslot'] == day:
                    showlogo.configure(text = Show['title'], style='showNames.TButton', command=lambda: ShowEditorWindow(self))

            #Button(self, text="Add\nShow", justi/=fy=CENTER, relief='raised', borderwidth=1, padx=5, pady=5).grid(row=1, column=count, sticky='nsew', padx=5, pady=0)
            count = count + 1        

        # configure
        self.configure(padx=20, pady=20, relief='solid', borderwidth=1)

class EventsSchedule(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # load Events
        load_events()

        # set up grid
        self.rowconfigure((0,2), weight=1)
        self.rowconfigure((1,3), weight=3)
        self.columnconfigure((0,1,2,3,4,5), uniform='y', weight=1)

        # set ttk styles
        eventNames = ttk.Style()
        eventNames.configure('eventNames.TButton', font=('snes', 14))
        # use wraplength=self.winfo_width() to fix above somehow

        # add widgets
        count = 0
        MonthsOfTheYear = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]

        for month in MonthsOfTheYear:
            if count < 6:
                ttk.Label(self, text=month, font=('Conduit ITC',12), anchor='center', style='inverse-secondary').grid(row=0, column=count, sticky='nsew', padx=5, pady=5)
                eventLogo = ttk.Button(self, text="Click to\nadd an\nevent", style='outline.Secondary.TButton', padding=5, command=lambda: Toplevel(EventEditor(timeslot=month)))
                eventLogo.grid(row=1, column=count, sticky='nsew', padx=5, pady=0)

                for Event in Events:
                    if Event['timeslot'] == month:
                        eventLogo.configure(text = Event['title'], style='eventNames.TButton', command=lambda: Toplevel(ShowEditor()))

                count = count + 1
            else:
                ttk.Label(self, text=month, font=('Conduit ITC',12), anchor='center', style='inverse-secondary').grid(row=2, column=(count-6), sticky='nsew', padx=5, pady=5)
                eventLogo = ttk.Button(self, text="Click to\nadd an\nevent", style='outline.Secondary.TButton', padding=5, command=lambda: Toplevel(EventEditor(timeslot=month)))
                eventLogo.grid(row=3, column=count-6, sticky='nsew', padx=5, pady=(5,0))

                for Event in Events:
                    if Event['timeslot'] == month:
                        eventLogo.configure(text = Event['title'], style='eventNames.TButton', command=lambda: Toplevel(ShowEditor(self)))

                count = count + 1

        # configure
        self.configure(padx=20, pady=20, relief='solid', borderwidth=1)

class NewUniverse(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Setup Frames
        NewCompany = Company(self)
        ShowSchedule = ShowsSchedule(self)
        EventSchedule = EventsSchedule(self)

        # setup grid
        self.rowconfigure((0,1,2), weight=1, uniform='x')
        self.columnconfigure((0,1,2), weight=1, uniform='y')

        NewCompany.grid(row=0,column=0,rowspan=3, padx=20, pady=20, sticky='nsew')
        ShowSchedule.grid(row=0,column=1,columnspan=2, padx=20, pady=20, sticky='nsew')
        EventSchedule.grid(row=1,column=1,columnspan=2,rowspan=2, padx=20, pady=20, sticky='nsew')

        # configure frame
        self.configure(relief='solid', borderwidth=0)
        self.pack(anchor='center', padx=0, pady=0, expand=True, fill='both')

class ShowEditor(Toplevel):
    def __init__(self, parent, title='', logo='images\genericshow.png', timeslot='', runtime=120, GM='', matchtable='data/matchtables/basic.csv'):
        super().__init__(parent)

        self.title('Show Editor')
        self.geometry('900x650')

        # set up grid 4x6
        self.rowconfigure((0,1,2,3), weight=1, uniform='x')
        self.columnconfigure((0,1,2,3,4,5), weight=1, uniform='x')

        # build + show logo frame
        ShowLogoFrame = Frame(self, relief='solid', borderwidth=0)
        ShowLogoFrame.grid(row=0, column=0, rowspan=2, columnspan=2)

        # add logo canvas
        img_canvas = Canvas(ShowLogoFrame, width=256, height=256)
        img_canvas.pack(expand=True, fill='both')
        img_canvas.img_file = ImageTk.PhotoImage(file=logo)
        img_canvas.create_image(0, 0, image=img_canvas.img_file, anchor=NW)

        # build + show details frame
        ShowDetailsFrame = Frame(self)
        ShowDetailsFrame.grid(row=0, column=2, rowspan=2, columnspan=2, sticky='nsew')

        # add widgets
        Label(ShowDetailsFrame, text='Show Title:', font=('Conduit ITC',14)).pack(side=LEFT)
        Entry(ShowDetailsFrame, font=('Conduit ITC',14)).pack(side=LEFT)

        Label(ShowDetailsFrame, text='Time Slot:', font=('Conduit ITC',14)).pack(side=LEFT)
        Entry(ShowDetailsFrame, font=('Conduit ITC',14)).pack(side=LEFT)

class ShowEditor_UNUSED(Frame):
    def __init__(self, parent, title='', logo='images\genericshow.png', timeslot='', runtime=120, GM='', matchtable='data/matchtables/basic.csv'):
        super().__init__(parent)

        # set up grid 4x6
        self.rowconfigure((0,1,2,3), weight=1, uniform='x')
        self.columnconfigure((0,1,2,3,4,5), weight=1, uniform='x')
        
        # build widgets


        # place widgets

# layout
class NavigationPanel(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #image
        img = CTkImage(dark_image=Image.open('images\KayfabeLogo.png'), size=(150,45))
        CTkLabel(self, text="", image=img).pack(pady=20)

        NavButtons(self)
        self.configure(relief='raised', borderwidth=0)
        self.pack(side=LEFT, expand=False, fill='y', padx=(20,0), pady=20)

class MainPanel(Frame):
    def __init__(self, parent, NavCurrent):
        super().__init__(parent)
        self.configure(relief='sunken', borderwidth=1, padx=20, pady=20)
        ttk.Label(self, text=NavCurrent, font=('SNES', 36)).pack(side=TOP, fill='x')
        self.pack(side=LEFT, padx=20, pady=20, expand=True, fill='both')


# widgets
class NavButtons(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # define grid
        self.rowconfigure((0,1,2,3,4,5), weight=1)
        self.columnconfigure(0, weight=1)

        # create widgets
        EditShow = ttkb.Button(self, text="Show Editor", command=lambda: ShowEditorWindow(self)).grid(row=0, column=0, padx=20, pady=5, sticky='nsew')
        #Roster = ttkb.Button(self, text="Talent Relations", command=lambda: print("hello")).grid(row=0, column=0, padx=20, pady=5, sticky='nsew')        
        Live = ttkb.Button(self, text="Live Tonight", command=lambda: print("hello")).grid(row=1, column=0, padx=20, pady=5, sticky='nsew')
        Events = ttkb.Button(self, text="Events", command=lambda: print("hello")).grid(row=2, column=0, padx=20, pady=5, sticky='nsew')
        Creative = ttkb.Button(self, text="Creative Dept", command=lambda: print("hello")).grid(row=3, padx=20, pady=5, column=0, sticky='nsew')
        Shows = ttkb.Button(self, text="Shows", command=lambda: print("hello")).grid(row=4, column=0, padx=20, pady=5, sticky='nsew')
        
        # place widget
        self.pack(side=TOP, expand=False, fill="x")

class RoadTo(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        H1("Road To")

        self.pack()
        
        # define grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Create some widgets
        H1(self, "Coming Up").grid(row=0, column=0, sticky='nw')
        img_filepath = 'images/Designer (9).jpeg'
        img = CTkImage(light_image=Image.open(img_filepath), 
                        dark_image=Image.open(img_filepath),
                        size=(600,300))
        img_label = CTkLabel(self, text="", image=img)
        img_label.grid(row=1, column=0)

class Attribute(Frame):
    def __init__(self, parent, Name):
        super().__init__(parent)

        #configure container
        self.configure()

        Label(self, text=Name, font=('Conduit ITC',14)).pack(side=LEFT)
        Entry(self, font=('Conduit ITC',14)).pack(side=LEFT)

## STYLE CLASSES

# Your class
class H1():
    '''This class sets the baseline characteristics 
    for the widgets, including font, font size, and colors
    '''

    # Attributes
    varFont = "Bebas Neue"
    fontSize = 36
    varFG = "#F2F2F2"
    varBG = "#3b3b3b"
    varPadx = 0
    varPady = 20

    
    # Constructor
    def __init__(self, parent, varText):
        self.parent = parent
        self.varText = varText

        self.label = Label(
            parent, 
            text = varText, 
            fg = self.varFG, 
            bg = self.varBG, 
            font = (self.varFont, self.fontSize),
            padx = self.varPadx,
            pady = self.varPady
            )

    # Allows you to grid as you would normally
    # Can subsitute pack() here or have both class methods
    def grid(self, **kwargs):
        self.label.grid(kwargs)

class H2():
    '''This class sets the baseline characteristics 
    for the widgets, including font, font size, and colors
    '''

    # Attributes
    varFont = "Bebas Neue"
    fontSize = 24
    varFG = "#F2F2F2"
    varBG = "#3b3b3b"
    varPadx = 0
    varPady = 20

    
    # Constructor
    def __init__(self, parent, name, varText):
        self.parent = parent
        self.name = name
        self.varText = varText

        self.label = Label(
            parent, 
            text = varText, 
            fg = self.varFG, 
            bg = self.varBG, 
            font = (self.varFont, self.fontSize),
            padx = self.varPadx,
            pady = self.varPady
            )

    # Allows you to grid as you would normally
    # Can subsitute pack() here or have both class methods
    def grid(self, **kwargs):
        self.label.grid(kwargs)



# Match display widgets
class Participant(Button):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="Wrestler", font=('Orator STD',14), background='#333333', padx=10, pady=5, command=lambda: Wrestler_Selector())
        self.pack(side=TOP, anchor='center', padx=5, pady=5)

class Side(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief='groove', borderwidth=0)
        self.pack(side=LEFT, anchor='center', expand=False)

class Vs(Label):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="  VS  ", font=('Chosence', 14))
        self.pack(side=LEFT, anchor='center', expand=False, fill='y')

class MatchType(Frame):
    def __init__(self, parent, ruleset, stipulation):
        super().__init__(parent)
        self.ruleset = ruleset
        self.stipulation = stipulation
        Label(self, text=ruleset, font=('Conduit ITC',14), justify=CENTER, width=8, wraplength=65).pack(side=TOP, anchor='s')
        Label(self, text=stipulation, font=('Conduit ITC',10), justify=CENTER, width=8, wraplength=65).pack(side=BOTTOM, anchor='n')
        #matchtype = ruleset + " - " + stipulation
        #Label(self, text=matchtype, font=('Roboto Condensed',10)).pack()
        self.configure(width=10)
        self.pack(side=LEFT, anchor='w', expand=False, fill='x')
        
class Match(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief='solid', borderwidth='1')
        self.pack(side=TOP, anchor='nw', fill='x', ipadx=10, ipady=10, padx=5, pady=5)
        #ttkb.Separator(self, orient=HORIZONTAL)

class Wrestler_Selector(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # set up grid
        self.columnconfigure(0, minsize=256)


        self.CurrentSelection = "Saraya"

        # border
        ttk.Separator(orient='vertical').pack(side=LEFT, expand=False, fill='y')

        # show portrait and name
        selection_portrait(self).grid(row=0,column=0,columnspan=3)

        #selection_searchoptions(self)

#REFACTOR BELOW WIP...
        # lookup and filters
        self.search = ttk.Labelframe(self, text='Search', padding=5)
        self.search.rowconfigure((0,1,2,3,4), weight=1)
        self.search.columnconfigure((0,1,2,3,4,5), weight=1, pad=0)
        
        # search bar
        Entry(self.search).grid(row=0, column=0, columnspan=6, sticky='nsew', padx=10, pady=5)
        Button(self.search, text="Random").grid(row=0, column=5, sticky='e', padx=(0,10))
 
        # set division
        Division = StringVar(self.search, "Divison")  # Create a variable for strings, and initialize the variable
        self.divisions = ttk.Notebook(self).grid(row=1,column=0,columnspan=6)

        #ttk.Radiobutton(self.search, variable=Division, value="Men", text="Mens Division", style='Outline.Toolbutton').grid(row=1, column=0, columnspan=3, sticky='e', padx=0, pady=5)
        #ttk.Radiobutton(self.search, variable=Division, value="Women",text="Womens Division", style='Outline.Toolbutton').grid(row=1, column=3, columnspan=3, sticky='w', padx=0, pady=5)

        # filters
        ttk.Checkbutton(self.search, text='Faces', style='RoundToggle.Toolbutton').grid(row=2, column=0, sticky='ew', columnspan=2, padx=10, pady=5)
        ttk.Checkbutton(self.search, text='Heels', style='RoundToggle.Toolbutton').grid(row=2, column=3, sticky='ew', columnspan=2, padx=10, pady=5)
        ttk.Checkbutton(self.search, text='Rivals', style='RoundToggle.Toolbutton').grid(row=2, column=5, sticky='ew', columnspan=2, padx=10, pady=5)
        ttk.Checkbutton(self.search, text='Upper Card', style='RoundToggle.Toolbutton').grid(row=3, column=0, sticky='ew', columnspan=2, padx=10, pady=5)
        ttk.Checkbutton(self.search, text='Mid Card', style='RoundToggle.Toolbutton').grid(row=3, column=3, sticky='ew', columnspan=2, padx=10, pady=5)
        ttk.Checkbutton(self.search, text='Lower Card', style='RoundToggle.Toolbutton').grid(row=3, column=5, sticky='ew', columnspan=2, padx=10, pady=5)
        self.search.grid(row=5,column=0, padx=20, pady=20, ipadx=20, ipady=10, sticky='nsew')


        # quick picks
        self.quickpicks = ttk.Labelframe(self, text='Quick Picks')
        self.quickpicks.rowconfigure(0, weight=1)
        self.quickpicks.columnconfigure((0,1,2), weight=1, pad=5)
        Button(self.quickpicks, text="Random Face", wraplength=50).grid(row=0,column=0, sticky='ew', padx=10, pady=5)
        Button(self.quickpicks, text="Random Heel", wraplength=50).grid(row=0,column=1, sticky='ew', padx=10, pady=5)
        Button(self.quickpicks, text="Random Rival", wraplength=50).grid(row=0,column=2, sticky='ew', padx=10, pady=5)
        #self.quickpicks.grid(row=6,column=0, padx=20, pady=0, ipadx=20, ipady=10, sticky='nsew')
        
        # Show list of wrestlers!
        wrestlerlist(self.search)

class wrestlerlist(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        load_roster()

        for Name in FullRoster:
            Button(self, text=Name['name'], font=('Orator STD', 12)).pack(expand=True, fill='x', pady=1)

        self.configure(relief='raised', borderwidth=0, padx=0, pady=20)
        
        #self.grid(row=4,column=0, columnspan=6, sticky='nsew', padx=20, pady=20)


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


# break out components of Selector
class selection_portrait(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief='solid', borderwidth=1, width=256, height=256, padx=20, pady=20)
        # load, crop and display image:
        # load image ... saving just in case
        # self.portrait = PhotoImage(file="images\Testportrait2.png")
        # showportrait = ttk.Label(self, text='', image=self.portrait)
        # showportrait.pack()
        name = Label(self, text=parent.CurrentSelection, font=('Boston Traffic', 24), justify='center', background='#111111')
        name.pack(anchor='center', expand=True, fill='both')
        
class selection_filters:
    def __init__(self, parent):
        super().__init__(parent)

class selection_searchbar:
    def __init__(self, parent):
        super().__init__(parent)

class selection_list:
    def __init__(self, parent):
        super().__init__(parent)

# For Popup menus... 
# Found at https://stackoverflow.com/questions/63725428/popup-menu-on-button-click-in-tkinter
# Actual technique used documented here: https://www.tcl.tk/man/tcl8.5/TkCmd/popup.htm