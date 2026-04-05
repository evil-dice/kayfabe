from kivy.event import EventDispatcher
from kivy.properties import ListProperty, StringProperty

from kivy.uix.label import Label
from kivy.metrics import dp

from kivy.event import EventDispatcher
from kivy.properties import ListProperty, StringProperty

class ColorTheme(EventDispatcher):
    black      = ListProperty([0, 0, 0, 1])
    white      = ListProperty([1, 1, 1, 1])
    neutral    = ListProperty([0.3, 0.3, 0.3, 0.9])
    primary    = ListProperty([1, 1, 1, 0.9])
    secondary  = ListProperty([0.9, 0.2, 0.2, 0.9])
    inactive   = ListProperty([0, 0, 0, 0])
    background = ListProperty([0, 0, 0, 0.75])
    border     = ListProperty([0.9, 0.9, 0.9, 0.5])
    text       = ListProperty([1, 1, 1, 0.9])

class FontTheme:
    headers   = "assets/fonts/BEBASNEUE BOLD.OTF"
    bodytext  = "assets/fonts/RUBIK-REGULAR_0.TTF"
    fields    = "assets/fonts/BARLOWCONDENSED-REGULAR.TTF"
    captions  = "assets/fonts/BARLOWCONDENSED-REGULAR.TTF"

class StyleTheme:
    def __init__(self, theme):
        self.default = {
            "font_size": "16dp",
            "font_name": theme.font.bodytext,
            "color": theme.color.primary
        }
        self.header = {
            "font_size": "48dp",
            "font_name": theme.font.headers,
            "color": theme.color.secondary
        }
        self.field = {
            "font_size": "16dp",
            "font_name": theme.font.fields,
            "color": theme.color.primary
        }
        self.caption = {
            "font_size": "17dp",
            "font_name": theme.font.fields,
            "color": theme.color.primary
        }

class Theme(EventDispatcher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = ColorTheme()
        self.font  = FontTheme()
        self.style = StyleTheme(self)

_theme_instance = Theme()
def ThemeManager():
    return _theme_instance