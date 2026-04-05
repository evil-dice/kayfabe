from kivy.uix.boxlayout import BoxLayout
from state.universe import Universe
from kivy.uix.button import Button
from kivy.graphics                  import Rectangle, Color
from kivy.uix.button                import Button
from kivy.uix.togglebutton                import ToggleButton, ToggleButtonBehavior
from kivy.uix.image                 import Image

from core.widgets.labels import COLORS

class NavBar(BoxLayout):
    def __init__(self, orientation='horizontal', size_hint_x=1, size_hint_y=None, height=50, **kwargs):
        super().__init__(**kwargs)
        self.orientation = orientation
        self.size_hint_x = size_hint_x
        self.size_hint_y = size_hint_y
        self.height = height
        # self.pos_hint={'top': 1}

        # Draw one background for the whole bar
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # dark bluish background
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

        # Keep background synced with layout size/pos
        self.bind(pos=self._update_bg, size=self._update_bg)

        # Add buttons with transparent backgrounds
        self.overview = NavButton(text="Overview", group="nav")
        self.schedule = NavButton(text="Schedule", group="nav")
        self.roster = NavButton(text="Roster", group="nav")
        self.rankings = NavButton(text="Rankings", group="nav")
        self.creative = NavButton(text="Creative", group="nav")

        # self.add_widget(self.overview)
        self.add_widget(self.rankings)
        self.add_widget(self.schedule)
        self.add_widget(self.overview)
        self.add_widget(self.roster)
        self.add_widget(self.creative)

        # Bind each button to change the screen
        self.overview.bind(state=lambda btn, state: self._switch_view("overview", state))
        self.overview.bind(state=lambda btn, state: self._switch_view("overview", state))
        self.schedule.bind(state=lambda btn, state: self._switch_view("schedule", state))
        self.roster.bind(state=lambda btn, state: self._switch_view("roster", state))
        self.rankings.bind(state=lambda btn, state: self._switch_view("rankings", state))
        self.creative.bind(state=lambda btn, state: self._switch_view("creative", state))

        # Bind Universe property to update button states
        Universe().bind(active_gameplay_view=self._update_buttons)

    def _update_buttons(self, inst, val):
        # Normalize string
        key = val.strip().lower()

        # Reset all buttons
        for btn in (self.overview, self.schedule, self.roster, self.rankings, self.creative):
            btn.state = "normal"

        # Set the active one
        if key == "overview":
            self.overview.state = "down"
        elif key == "schedule":
            self.schedule.state = "down"
        elif key == "roster":
            self.roster.state = "down"
        elif key == "rankings":
            self.rankings.state = "down"
        elif key == "creative":
            self.creative.state = "down"

    def _switch_view(self, screen_name, state):
        if state == "down":
            print("NavBar switching to:", screen_name)
            Universe().active_gameplay_view = screen_name

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

class NavButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "assets/fonts/BEBASNEUE BOLD.OTF"
        self.font_size = 20
        self.background_normal = ""
        self.background_color = (0,0,0,0)
        self.bind(pos=self._update_canvas, size=self._update_canvas, state=self._update_canvas)

    def _update_canvas(self, *args):
        # Background
        self.canvas.before.clear()
        with self.canvas.before:
            if self.state == "down":
                Color(*COLORS['secondary'])  # highlight color
            else:
                Color(0, 0, 0, 0)  # transparent
            Rectangle(pos=self.pos, size=self.size)

        # Bottom underline
        self.canvas.after.clear()
        if self.state == "down":
            with self.canvas.after:
                Color(*COLORS['primary'])  # white underline
                Rectangle(pos=(self.x, self.y), size=(self.width, 4))  # 4px thick

class NavImage(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_no_selection = False
    
    def on_state(self, widget, value):
        if value == "down":
            self.color = COLORS['secondary']   # active (full color)
        else:
            self.color = (0,0,0,0)  # inactive (dimmed)