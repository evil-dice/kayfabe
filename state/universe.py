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
    active_gameplay_view = StringProperty("overview")
    current_match = ObjectProperty(None)
    match_dirty = BooleanProperty(False)
    booking_errors = ListProperty([])

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