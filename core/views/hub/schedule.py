from kivy.uix.screenmanager         import Screen
from kivy.graphics                  import Rectangle, Color
from kivy.uix.button                import Button
from kivy.core.window               import Window
from kivy.uix.boxlayout             import BoxLayout
from kivy.uix.floatlayout           import FloatLayout
from kivy.uix.stacklayout           import StackLayout
from kivy.uix.relativelayout        import RelativeLayout
from kivy.uix.gridlayout            import GridLayout
from kivy.metrics import dp


from core.views.hub.placeholder     import Placeholder
from core.widgets.containers import Column, Row
from core.widgets.labels import HeaderLabel, BodyLabel, CaptionLabel, SideLabel
from utils.userealsize  import use_real_size
from state.universe import Universe
from core.widgets.slottile import SlotTile

class Schedule(BoxLayout):
    def __init__(self, orientation='vertical', spacing=40, padding=20, **kwargs):
        super().__init__(**kwargs)

        self.orientation = orientation
        self.spacing = spacing
        self.padding = padding

        # Background Layer
        with self.canvas.before:
            self.bg_color = Color(0, 0, 0, 0.8)
            self.bg_rect = Rectangle(source="assets\images\schedule_bg.png", pos=self.pos, size=Window.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # Layout
        # Row 1 - Days of the week
        row_1 = Row(orientation='vertical', size_hint_y=1)
        self.add_widget(row_1)
        
        # Months of the Year
        row_2 = Row(orientation='vertical', size_hint_y=1)
        self.add_widget(row_2)

        # Content
        # Row 1
        header_shows = HeaderLabel("Weekly Shows")
        row_1.add_widget(header_shows)

        daysoftheweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekly_schedule = GridLayout(cols=7, spacing=10)
        row_1.add_widget(weekly_schedule)
        
        # Create widgets for each show slot
        show_slots = Universe().all_shows
        
        for slot in show_slots:
            # Make a box
            week_tile=BoxLayout(orientation='vertical', size_hint_y=0.2)
            
            # Add a label to box
            week_tile.add_widget(CaptionLabel(text=slot, halign="center"))

            # Add show tile to the box
            week_tile.add_widget(SlotButton(slot))

            # Add to grid
            weekly_schedule.add_widget(week_tile)

        # Row 2
        header_events = HeaderLabel("Events")
        row_2.add_widget(header_events)

        monthsoftheyear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        monthly_schedule = GridLayout(cols=6, spacing=10)
        row_2.add_widget(monthly_schedule)

        # create widgets for each
        for month in monthsoftheyear:
            # Make a box
            month_tile=BoxLayout(orientation='horizontal')
            
            # Add a label to box
            month_tile.add_widget(SideLabel(text=month, halign="center", valign="middle"))
            month_tile.add_widget(Placeholder(text=" + ", square_x=True, pos_hint={'center_y': 0.5}))

            # Add to grid
            monthly_schedule.add_widget(month_tile)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size