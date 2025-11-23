from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.metrics import dp

COLORS={
    'primary': (1, 1, 1, 0.9),
    'secondary': (0.9, 0.2, 0.2, 0.9),
    'inactive': (0, 0, 0, 0),
    'highlight': (0, 0, 0, 0)
}

FONTS={
    'headers': "assets/fonts/BEBASNEUE BOLD.OTF",
    'bodytext': "assets/fonts/RUBIK-REGULAR_0.TTF",
    'fields': "assets/fonts/BARLOWCONDENSED-REGULAR.TTF"
}

STYLES = {
    "default": {"font_size": "16dp", "font_name": FONTS['bodytext'], "color": COLORS['primary']},
    "header": {"font_size": "48dp", "font_name": FONTS['headers'], "color": COLORS['secondary']},
    "field": {"font_size": "16dp", "font_name": FONTS['fields'], "color": COLORS['primary']}
}

class CustomLabel(Label):
    def __init__(self, text, padding_top=0, padding_bottom=0, variant="default", **kwargs):
        style = STYLES.get(variant, {})
        super().__init__(text=text, **{**style, **kwargs})

        # # Fill width, fixed height
        # self.size_hint_x = None   # Disable horizontal scaling
        # self.size_hint_y = None   # Disable vertical scaling
        
        # self.halign = "left"
        # self.valign = "middle"

        # Set text wrapping to match width
        self.bind(width=self._update_text_size)
        self.text_size = (self.width, None)

        # Update height based on text + padding
        self.bind(texture_size=self._update_height)

        # Store padding
        self.padding_top = dp(padding_top)
        self.padding_bottom = dp(padding_bottom)

    def _update_text_size(self, *args):
        self.text_size = (self.width, None)

    def _update_height(self, *args):
        self.height = self.texture_size[1] + self.padding_top + self.padding_bottom

class HeaderLabel(CustomLabel):
    def __init__(self, text, **kwargs):
        super().__init__(text, variant="header", **kwargs)

        # Customizations
        self.size_hint_x = 1   # Fill width of parent
        self.halign='center'
        self.valign='top'
        self.padding = (0, 10) # Padding after
        
class BodyLabel(CustomLabel):
    def __init__(self, text, **kwargs):
        super().__init__(text, variant="default", **kwargs)

        # Customizations
        self.size_hint_x = 1   # Fill width of parent
        self.valign='top'
        self.padding = (dp(10), dp(10)) # Padding before and after

class FieldLabel(CustomLabel):
    def __init__(self, text, **kwargs):
        super().__init__(text, variant="field", **kwargs)

        # Customizations
        self.size_hint_y = 1  # match height of field

















# class CustomLabel(Label):
#     def __init__(self, text, padding_top=0, padding_bottom=0, **kwargs):
#         super().__init__(text=text, **kwargs)

#         # Fill width, fixed height
#         self.size_hint_x = None   # Disable horizontal scaling
#         self.size_hint_y = None   # Disable vertical scaling
        
#         self.halign = "left"
#         self.valign = "middle"

#         # Set text wrapping to match width
#         self.bind(width=self._update_text_size)
#         self.text_size = (self.width, None)

#         # Update height based on text + padding
#         self.bind(texture_size=self._update_height)

#         # Store padding
#         self.padding_top = dp(padding_top)
#         self.padding_bottom = dp(padding_bottom)

#     def _update_text_size(self, *args):
#         self.text_size = (self.width, None)

#     def _update_height(self, *args):
#         self.height = self.texture_size[1] + self.padding_top + self.padding_bottom




# class FieldLabel(CustomLabel):
#     def __init__(self, **kwargs):
#         super().__init__(
#             font_name=r"assets/fonts/LATO-REGULAR.TTF", 
#             font_size=16, 
#             color=COLORS['primary'], 
#             **kwargs
#         )
#         self.size_hint_y = 1

# class Header(CustomLabel):
#     def __init__(self, **kwargs):
#         super().__init__(
#             font_name=r"assets/fonts/BEBASNEUE BOLD.OTF", 
#             font_size=48, 
#             color=COLORS['secondary'], 
#             **kwargs
#         )

#         self.size_hint_x = 1 # Fill width of parent
#         self.padding = (0, 10)

class BodyText(Label):
    def __init__(self, **kwargs):
        super().__init__(
            font_family="Lato",
            font_size=12,
            halign="left",
            valign="top",
            **kwargs)

class FormField(TextInput):
    def __init__(self, **kwargs):
        super().__init__()

        # Fill width, fixed height
        self.size_hint_x = 1      # Fill width of parent
        self.size_hint_y = None   # Disable vertical scaling
        self.height = 30          # Explicit height
        self.multiline = False