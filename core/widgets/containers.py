from kivy.uix.boxlayout import BoxLayout

class Row(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter('height'))  # height = sum of children

class Column(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', size_hint_x=None, **kwargs)
        self.bind(minimum_width=self.setter('width'))  # width = sum of children

class Box(BoxLayout):
    def __init__(self, width, height, **kwargs):
        super().__init__(size_hint=(None, None), width=width, height=height, **kwargs)