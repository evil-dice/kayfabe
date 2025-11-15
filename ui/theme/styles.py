# ui/theme/style.py

FONT_FAMILY = "assets/fonts/legacy.ttf"

COLORS = {
    "basictext": (1, 1, 1, 1),
    "text_secondary": (0.8, 0.8, 0.8, 1),
    "accent": (1, 0.8, 0.2, 1),
    "panel_bg": (0, 0, 0, 0.6),
}

SIZES = {
    "header": 24,
    "field": 16,
    "tile": 18,
}


fonts = {
    'headers': 'Bebas Neue',
    'body': 'Lato',
    'stylized': 'Royal Rumble'
}

stylesheet = {
    'h1': {'style': 'h1.TLabel', 'font': (fonts['headers'], 36), 'anchor': 'w', 'justify': 'left'},
    'h2': {'style': 'h2.TLabel', 'font': (fonts['headers'], 24), 'anchor': 'w', 'justify': 'left'},
    'body': {'style': 'body.TLabel', 'font': (fonts['body'], 12), 'anchor': 'w', 'justify': 'left'},
    'field': {'style': 'field.TLabel', 'font': (fonts['body'], 12), 'anchor': 'w', 'justify': 'left', 'width': 15},
    'schedule': {'style': 'schedule.TLabel', 'font': (fonts['stylized'], 26), 'anchor': 'center', 'justify': 'center'},
    'companyselect': {'style': 'companyselect.TCombobox', 'font': (fonts['body'], 20), 'anchor': 'center'}
}

buttons = {
    'slot': {'style': 'slot.TButton', 'font': (fonts['headers'], 20), 'anchor': 's', 'justify': 'center'}
}

space = {
    'h1': {'padx': 0, 'pady': (0,10), 'expand': 'False', 'fill': 'x'},
    'h2': {'padx': 0, 'pady': (0,10), 'expand': 'False', 'fill': 'x'},
    'body': {'padx': 0, 'pady': (0,20), 'expand': 'False', 'fill': 'x'},
    'entry': {'padx': 20, 'pady': (0,20), 'expand': 'False', 'fill': 'x'}
}

frames = {
    'blackBG': {'background': '000000'}
}