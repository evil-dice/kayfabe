from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from config.styles import COLORS
from kivy.uix.widget import Widget


from kivy.uix.gridlayout import GridLayout

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle

class Panel(BoxLayout):
    def __init__(self, orientation = 'vertical', size_hint=(None, None), radius=[8], spacing=10, **kwargs):
        super().__init__(padding=10, **kwargs)
        self.size_hint = size_hint
        self.orientation = orientation
        self.spacing = spacing
        # self.bind(minimum_height=self.setter('height'))

        with self.canvas.before:
            # Border layer
            Color(0.9, 0.9, 0.9, 0.5)  # Red border (RGBA)
            self.border = RoundedRectangle(radius=radius)

            # Background layer
            Color(0, 0, 0, 0.75)  # Dark translucent background
            self.bg = RoundedRectangle(radius=radius)  # Slightly smaller radius

        # with self.canvas.before:
        #     Color(0.1, 0.1, 0.1, 0.6)
        #     self.bg = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)

        self.bind(pos=self._update_bg, size=self._update_bg)

    # def _update_bg(self, *args):
    #     # Border slightly larger than background
    #     self.border.pos = (self.x - 2, self.y - 2)
    #     self.border.size = (self.width + 4, self.height + 4)

    #     self.bg.pos = self.pos
    #     self.bg.size = self.size

    def _update_bg(self, *args):
        self.border.pos = self.pos
        self.border.size = self.size
        self.bg.pos = (self.x + 2, self.y + 2)
        self.bg.size = (self.width - 4, self.height - 4)
