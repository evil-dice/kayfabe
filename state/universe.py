# core/universe_state.py

from kivy.event import EventDispatcher
from kivy.properties import StringProperty, ListProperty, ObjectProperty, BooleanProperty

class Universe(EventDispatcher):
    active_screen = StringProperty("title")
    company = ObjectProperty(None)
    roster = ListProperty([])
    titles = ListProperty([])
    events = ListProperty([])
    current_match = ObjectProperty(None)
    match_dirty = BooleanProperty(False)
    booking_errors = ListProperty([])

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Universe, cls).__new__(cls)
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
