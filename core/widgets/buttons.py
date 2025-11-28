# core.widgets.buttons.py

from kivy.uix.image import Image
from kivy.uix.button import Button, ButtonBehavior
from kivy.metrics import dp


from utils.hoverbehavior import HoverBehavior
from utils.realsizehint import RealSizeHint

from core.widgets.labels import COLORS

class ImageButton(ButtonBehavior, Image):
    def __init__(self, source, **kwargs):
        super().__init__(source=source, **kwargs)
        # You can set size hints or fixed size here if needed
        self.size_hint = (None, None)
        self.width = 100
        self.height = 100

        # self.bind(on_click)

# Example usage:
# img_btn = ImageButton(source="assets/images/logo.png")
# img_btn.bind(on_release=lambda instance: print("Image button clicked!"))

class MainMenuButton(Button, HoverBehavior):
    def __init__(self, label_to_update=None, size_hint=(0.85, None), height=dp(45), hover_text="", **kwargs):
        super().__init__(pos_hint={'center_x': 0.5}, **kwargs)

        self.size_hint = size_hint
        self.height=height

        # Text styling
        self.font_name = "assets/fonts/OLD PRESS ITALIC_0.TTF"   # path to your font file
        self.font_size = 32                          # larger text
        # self.color = (1, 0, 0, 1)                    # RGBA (yellow text)

        # Background styling
        # self.background_normal = ""                  # remove default image
        self.background_color = (0.25,0.25,0.25,1) # dark gray background
        self.background_color_hover = (0.4, 0.4, 0.4, 1)   # dark gray background

        # link to updatable text if profided
        self.hover_text = hover_text
        self.label_to_update = label_to_update

        # Remember the label's original text
        if self.label_to_update:
            self._default_text = self.label_to_update.text

    def on_hover(self, value):
        if self.label_to_update:
            if value:
                self.label_to_update.text = self.hover_text
            else:
                self.label_to_update.text = self._default_text
