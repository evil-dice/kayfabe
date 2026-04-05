from kivy.uix.boxlayout import BoxLayout

class Row(BoxLayout):
    def __init__(self, size_hint_y=None, height=None, orientation="vertical", **kwargs):
        super().__init__(orientation='horizontal', **kwargs)
        self.size_hint_x = 1
        self.size_hint_y = size_hint_y
        self.spacing = 20
        self.orientation = orientation
        if height:
            self.height = height
        else:
            self.bind(minimum_height=self.setter('height'))  # height = sum of children

class Column(BoxLayout):
    def __init__(self, size_hint_x=None, width=None, orientation='vertical', **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = size_hint_x
        self.size_hint_y = 1
        self.spacing = 20
        self.orientation = orientation
        if width:
            self.width = width
        else:
            self.bind(minimum_width=self.setter('width'))  # width = sum of children

class Box(BoxLayout):
    def __init__(self, width, height, **kwargs):
        super().__init__(size_hint=(None, None), width=width, height=height, **kwargs)