# core/universe_state.py

from kivy.event import EventDispatcher
from kivy.properties import StringProperty, ListProperty, ObjectProperty, BooleanProperty

from companies.model import Company

class Universe(EventDispatcher):
    active_screen = StringProperty("title")
    previous_screen = StringProperty(None, allownone=True)
    company = ObjectProperty(None, allownone=True)
    roster = ListProperty([])
    titles = ListProperty([])
    events = ListProperty([])
    shows = ListProperty([])
    active_gameplay_view = StringProperty("schedule")
    current_match = ObjectProperty(None)
    match_dirty = BooleanProperty(False)
    booking_errors = ListProperty([])

    # Universe Show Slots
    monday_show = ObjectProperty(None)
    tuesday_show = ObjectProperty(None)
    wednesday_show = ObjectProperty(None)
    thursday_show = ObjectProperty(None)
    friday_show = ObjectProperty(None)
    saturday_show = ObjectProperty(None)
    sunday_show = ObjectProperty(None)

    # Universe Event Slots
    january_event = ObjectProperty(None)
    february_event = ObjectProperty(None)
    march_event = ObjectProperty(None)
    april_event = ObjectProperty(None)
    may_event = ObjectProperty(None)
    june_event = ObjectProperty(None)
    july_event = ObjectProperty(None)
    august_event = ObjectProperty(None)
    september_event = ObjectProperty(None)
    october_event = ObjectProperty(None)
    november_event = ObjectProperty(None)
    december_event = ObjectProperty(None)

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Universe, cls).__new__(cls)
            cls._instance.company = Company()
            EventDispatcher.__init__(cls._instance)
        return cls._instance

    def reset(self):
        self.company = None
        self.roster = []
        self.titles = []
        self.events = []
        self.current_match = None
        self.match_dirty = False
        self.booking_errors = []
        self.active_screen = "title"

    def change_screen(self, screen):
        '''Stores current active_screen as previous_screen, and then changes active_screen.'''
        # copy the current value into previous_screen
        self.previous_screen = self.active_screen
        # now update active_screen
        self.active_screen = screen
        # Confirm
        print(f"Moving from {self.previous_screen} to {self.active_screen}")

    def change_gameplay_view(self, gameplay_view):
        '''Changes current view in the gameplay screen.'''
        # now update active_screen
        self.active_gameplay_view = gameplay_view
        # Confirm
        print(f"Current Gameplay View set to: {self.active_gameplay_view}")
    
    def all_shows(self):
        '''Returns all shows as a list.'''
        return [
            self.monday_show,
            self.tuesday_show,
            self.wednesday_show,
            self.thursday_show,
            self.friday_show,
            self.saturday_show,
            self.sunday_show
        ]

    def all_events(self):
        '''Returns all events as a list.'''
        return [
            self.january_event,
            self.february_event,
            self.march_event,
            self.april_event,
            self.may_event,
            self.june_event,
            self.july_event,
            self.august_event,
            self.september_event,
            self.october_event,
            self.november_event,
            self.december_event
        ]
