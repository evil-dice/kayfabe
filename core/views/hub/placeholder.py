from kivy.uix.button import Button
from utils.userealsize import use_real_size

class Placeholder(Button):
    def __init__(self, text="Placeholder", square_x=False, square_y=False, **kwargs):
        super().__init__(**kwargs)
    
        self.text=text
        self.background_normal=""   # remove default background image
        self.background_down=""     # remove pressed background image
        self.background_color=(1, 0, 0, 0.2)  # RGBA: fully transparent

        if square_x == True:
            self.size_hint=(1, None)   # stretch horizontally, fixed vertically
            # use_real_size(self)
            self.bind(width=self._sync_height)

        if square_y == True:
            self.size_hint=(None, 1)   # fixed horizontally, stretch vertically
            # use_real_size(self)
            self.bind(width=self._sync_width)

    def _sync_height(self, *args):
        self.height = self.width  # keep square
    
    def _sync_width(self, *args):
        self.width = self.height  # keep square

