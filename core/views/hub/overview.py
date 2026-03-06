from kivy.uix.screenmanager         import Screen
from kivy.graphics                  import Rectangle, Color
from kivy.uix.button                import Button
from kivy.core.window               import Window
from kivy.uix.boxlayout             import BoxLayout
from kivy.uix.floatlayout           import FloatLayout
from kivy.uix.stacklayout           import StackLayout
from kivy.uix.relativelayout        import RelativeLayout
from kivy.uix.gridlayout            import GridLayout
from core.views.hub.placeholder     import Placeholder

from core.widgets.containers import Column, Row

class Overview(BoxLayout):
    def __init__(self, orientation='horizontal', spacing=20, padding=20, **kwargs):
        super().__init__(**kwargs)

        self.orientation = orientation
        self.spacing = spacing
        self.padding = padding

        # Background Layer
        with self.canvas.before:
            self.bg_color = Color(0, 0, 0, 0.8)
            self.bg_rect = Rectangle(source="assets\images\gameplay_bg.png", pos=self.pos, size=Window.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # Layout
        column_1 = Column(size_hint_x=0.65)
        self.add_widget(column_1)
        
        column_2 = Column(size_hint_x=0.35)
        self.add_widget(column_2)

        # Content
        column_1.add_widget(Placeholder())

        list = [0, 1]
        for x in list:
            column_2.add_widget(Placeholder())

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size