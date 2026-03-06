# theme.py
from kivy.metrics import sp, dp
from kivy.properties import ColorProperty, NumericProperty, StringProperty
from kivy.event import EventDispatcher


# -----------------------------
# COLOR NAMESPACE
# -----------------------------
class ColorNamespace(EventDispatcher):
    # Core text colors
    text_primary = ColorProperty((1, 1, 1, 1))          # basictext
    text_secondary = ColorProperty((0.8, 0.8, 0.8, 1))  # text_secondary

    # Accent + UI colors
    primary = ColorProperty((1, 0.8, 0.2, 1))
    accent = ColorProperty((1, 0.8, 0.2, 1))            # accent
    panel_bg = ColorProperty((0, 0, 0, 0.6))            # panel_bg

    # Utility colors
    white = ColorProperty((1, 1, 1, 1))
    black = ColorProperty((0, 0, 0, 1))
    grey = ColorProperty((0.5, 0.5, 0.5, 1))
    darkgrey = ColorProperty((0.25, 0.25, 0.25, 1))
    lightgrey = ColorProperty((0.75, 0.75, 0.75, 1))
    transparent = ColorProperty((0, 0, 0, 0))

    # Special colors from your old theme
    new_item = ColorProperty((0.2, 1, 0.2, 1))
    highlighted_item = ColorProperty((1, 0.8, 0, 1))

    def alpha(self, rgba, alpha):
        return (rgba[0], rgba[1], rgba[2], alpha)


# -----------------------------
# FONT NAMESPACE
# -----------------------------
class FontNamespace(EventDispatcher):
    # These map directly to your old "fonts" dict
    headers = StringProperty("assets/fonts/Bebas Neue.ttf")
    body = StringProperty("assets/fonts/Lato.ttf")
    stylized = StringProperty("assets/fonts/Royal Rumble.ttf")

    # Semantic roles
    h1 = headers
    h2 = headers
    body_text = body
    field = body
    schedule = stylized
    companyselect = body

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# -----------------------------
# SIZE NAMESPACE
# -----------------------------
class SizeNamespace(EventDispatcher):
    # These map directly to your old SIZES + stylesheet font sizes
    h1 = NumericProperty(sp(36))   # stylesheet['h1']['font']
    h2 = NumericProperty(sp(24))   # stylesheet['h2']['font']
    body = NumericProperty(sp(12)) # stylesheet['body']['font']
    field = NumericProperty(sp(12))
    schedule = NumericProperty(sp(26))
    companyselect = NumericProperty(sp(20))
    tile = NumericProperty(sp(18))

    # Layout spacing
    padding = NumericProperty(dp(20))
    spacing = NumericProperty(dp(10))
    radius = NumericProperty(dp(12))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# -----------------------------
# THEME ROOT
# -----------------------------
class Theme(EventDispatcher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = ColorNamespace()
        self.font = FontNamespace()
        self.size = SizeNamespace()


theme = Theme()

# Convenience aliases
color = theme.color
font = theme.font
size = theme.size