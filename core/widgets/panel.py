from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from config.styles import COLORS
from utils.realsizehint import RealSizeHint

# class Panel(BoxLayout, RealSizeHint):
#     def __init__(self, orientation = 'vertical', radius=[8], spacing=10, padding=10, real_size_hint=(1, 1), **kwargs):
#         super().__init__(**kwargs)

#         # Force size hint
#         RealSizeHint.__init__(self, width_percent=real_size_hint[0], height_percent=real_size_hint[1])

#         self.orientation = orientation
#         self.spacing = spacing
#         self.padding = padding

#         # # Let width be controlled by parent, but height = sum of children
#         self.size_hint_y = None
#         self.bind(minimum_height=self.setter('height'))

#         with self.canvas.before:
#             # Border layer
#             Color(0.9, 0.9, 0.9, 0.5)  # Red border (RGBA)
#             self.border = RoundedRectangle(radius=radius)

#             # Background layer
#             Color(0, 0, 0, 0.75)  # Dark translucent background
#             self.bg = RoundedRectangle(radius=radius)  # Slightly smaller radius
        
#         self.bind(pos=self._update_bg, size=self._update_bg)

#     def _update_bg(self, *args):
#         self.border.pos = self.pos
#         self.border.size = self.size
#         self.bg.pos = (self.x + 2, self.y + 2)
#         self.bg.size = (self.width - 4, self.height - 4)

class Panel(BoxLayout):
    def __init__(self,
                 orientation='vertical',
                 radius=[8],
                 spacing=10,
                 padding=10,
                 real_size_hint=None,   # (width%, height%) or None
                 shrink_to_fit=False,   # toggle shrink mode
                 **kwargs):
        super().__init__(**kwargs)

        self.orientation = orientation
        self.spacing = spacing
        self.padding = padding

        # --- Mode selection ---
        if shrink_to_fit:
            # Hug children vertically
            self.size_hint_y = None
            self.bind(minimum_height=self.setter('height'))
        elif real_size_hint:
            # Fixed size relative to window
            self.size_hint = (None, None)
            self._width_percent, self._height_percent = real_size_hint
            self._apply_real_size(Window.size)
            Window.bind(size=lambda inst, size: self._apply_real_size(size))
        else:
            # Default: fill parent
            self.size_hint = (1, 1)

        # --- Background drawing ---
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 0.5)  # Border
            self.border = RoundedRectangle(radius=radius)
            Color(0, 0, 0, 0.75)        # Background
            self.bg = RoundedRectangle(radius=radius)

        self.bind(pos=self._update_bg, size=self._update_bg)

    def _apply_real_size(self, size):
        w, h = size
        if self._width_percent:
            self.width = w * self._width_percent
        if self._height_percent:
            self.height = h * self._height_percent

    def _update_bg(self, *args):
        self.border.pos = self.pos
        self.border.size = self.size
        self.bg.pos = (self.x + 2, self.y + 2)
        self.bg.size = (self.width - 4, self.height - 4)
