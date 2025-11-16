from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from config.styles import COLORS
from kivy.uix.widget import Widget


from kivy.uix.gridlayout import GridLayout

# class Panel(GridLayout):
#     def __init__(self, **kwargs):
#         super().__init__(cols=1, spacing=10, padding=20, **kwargs)

#         # Let the panel grow vertically based on its children
#         self.size_hint_y = None
#         self.bind(minimum_height=self.setter('height'))

#         # Anchor to top of parent
#         self.pos_hint = {'top': 1}

#         with self.canvas.before:
#             Color(0, 0, 0, 0.6)  # Semi-transparent black
#             self.rect = Rectangle(size=self.size, pos=self.pos)


# class Panel(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         self.size_hint_y = None  # Control box height 
#         self.bind(minimum_height=self.setter('height'))  # Grow to fit children



#         with self.canvas.before:
#             Color(0, 0, 0, 0.6)  # Semi-transparent black
#             self.rect = Rectangle(size=self.size, pos=self.pos)
        
#         self.orientation='vertical'
#         self.size_hint_x = 1      # Fill width of parent
#         self.size_hint_y = None   # Disable vertical scaling
#         self.padding = 20

#         self.bind(size=self._update_rect, pos=self._update_rect)

#     def _update_rect(self, *args):
#         self.rect.size = self.size
#         self.rect.pos = self.pos

# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.graphics import Color, RoundedRectangle

# class Panel(RelativeLayout):
#     def __init__(self, width=400, padding=20, spacing=10, **kwargs):
#         super().__init__(**kwargs)

#         self.size_hint = (None, None)
#         self.width = width
#         self.height = 0  # will be updated dynamically
#         self.pos_hint = {'top': 1}

#         # Background
#         with self.canvas.before:
#             Color(0.1, 0.1, 0.1, 0.6)
#             self.bg = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)

#         self.bind(pos=self._update_bg, size=self._update_bg)

#         # Inner layout that stacks widgets
#         self.content = GridLayout(
#             cols=1,
#             spacing=spacing,
#             padding=padding,
#             size_hint=(1, None)
#         )
#         self.content.bind(minimum_height=self._sync_height)
#         self.add_widget(self.content)

#     def _update_bg(self, *args):
#         self.bg.pos = self.pos
#         self.bg.size = self.size

#     def _sync_height(self, *args):
#         self.content.height = self.content.minimum_height
#         self.height = self.content.height

#     def new_widget(self, widget, *args, **kwargs):
#         if hasattr(self, 'content'):
#             self.content.add_widget(widget, *args, **kwargs)
#         else:
#             super().add_widget(widget, *args, **kwargs)


# from kivy.uix.widget import Widget
# from kivy.uix.gridlayout import GridLayout
# from kivy.graphics import Color, RoundedRectangle

# class Panel(Widget):
#     def __init__(self, width=400, padding=20, spacing=10, **kwargs):
#         super().__init__(**kwargs)

#         self.size_hint = (None, None)
#         self.width = width
#         self.height = 0
#         self.pos_hint = {'top': 1}

#         # Inner layout
#         self.content = GridLayout(
#             cols=1,
#             spacing=spacing,
#             padding=padding,
#             size_hint=(None, None),
#             width=width
#         )
#         self.content.bind(minimum_height=self._sync_height)
#         self.add_widget(self.content)

#         # Background
#         with self.canvas.before:
#             Color(0.1, 0.1, 0.1, 0.6)
#             self.bg = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)

#         self.bind(pos=self._update_bg, size=self._update_bg)

#     def _sync_height(self, *args):
#         self.content.height = self.content.minimum_height
#         self.height = self.content.height
#         self.size = (self.width, self.height)
#         self.content.pos = self.pos  # lock content to panel's position

#     def _update_bg(self, *args):
#         self.bg.pos = self.pos
#         self.bg.size = self.size

#     def new_widget(self, widget, *args, **kwargs):
#         self.content.add_widget(widget, *args, **kwargs)


from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle

class Panel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)
        self.size_hint = (None, None)
        self.bind(minimum_height=self.setter('height'))

        with self.canvas.before:
            # Border layer
            Color(0.5, 0.5, 0.5, 0.5)  # Red border (RGBA)
            self.border = RoundedRectangle(radius=[10])

            # Background layer
            Color(0.1, 0.1, 0.1, 0.8)  # Dark translucent background
            self.bg = RoundedRectangle(radius=[8])  # Slightly smaller radius

        # with self.canvas.before:
        #     Color(0.1, 0.1, 0.1, 0.6)
        #     self.bg = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)

        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *args):
        # Border slightly larger than background
        self.border.pos = (self.x - 2, self.y - 2)
        self.border.size = (self.width + 4, self.height + 4)

        self.bg.pos = self.pos
        self.bg.size = self.size


    # def _update_bg(self, *args):
    #     self.bg.pos = self.pos
    #     self.bg.size = self.size
