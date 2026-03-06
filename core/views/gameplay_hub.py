from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

from core.widgets.navbar import NavBar
from core.views.hub.overview import Overview
from core.views.hub.schedule import Schedule
from state.universe import Universe

class GameplayHub(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background image
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(source="assets/images/overview_bg.png",
                                     pos=self.pos, size=self.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # Root layout: vertical split
        root = BoxLayout(orientation="vertical")
        self.add_widget(root)

        # NavBar at the top
        self.navbar = NavBar(size_hint_y=None, height=60)
        root.add_widget(self.navbar)

        # Content area below, centered
        self.content_area = AnchorLayout()
        root.add_widget(self.content_area)

        # Bind Universe → swap views
        Universe().bind(active_gameplay_view=self._switch_view)

        # Start with overview
        Universe().active_gameplay_view = "overview"

    def _switch_view(self, inst, val):
        """Swap the content area to show the requested view."""
        print("GameplayHub received:", val)
        self.content_area.clear_widgets()

        # Create a fresh instance each time so it redraws
        if val == "overview":
            self.bg_rect.source = "assets/images/overview_bg.png"
            view = Overview()
        elif val == "schedule":
            self.bg_rect.source = "assets/images/schedule_bg.png"
            from core.views.hub.schedule import Schedule
            view = Schedule()
        elif val == "roster":
            self.bg_rect.source = "assets/images/roster_bg.png"
            from core.views.hub.roster import Roster
            view = Roster()
        elif val == "rankings":
            self.bg_rect.source = "assets/images/rankings2_bg.png"
            from core.views.hub.rankings import Rankings
            view = Rankings()
        elif val == "creative":
            self.bg_rect.source = "assets/images/creative2_bg.png"
            from core.views.hub.creative import Creative
            view = Creative()
        else:
            # fallback
            from kivy.uix.label import Label
            print(f"{val}")
            view = Label(text=f"Unknown view: {val}")

        # Shrink view so background margins show
        view.size_hint = (0.9, 0.9)
        view.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.content_area.add_widget(view)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size