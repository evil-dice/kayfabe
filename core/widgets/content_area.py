from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line

class ContentArea(Widget):
    '''
    Creates a borderd box layout that can be placed absolutely.  
    '''
    def __init__(self, size=(600, 600), position=(0, 0), padding=20, **kwargs):
        super().__init__(**kwargs)
        self.size = size
        self.pos = position

        self.layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=padding,
            size=self.size,
            pos=(0, 0)
        )
        self.add_widget(self.layout)

        with self.canvas.after:
            Color(0, 0, 1, 1)  # Red border
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=1)

        self.bind(pos=self._update_border, size=self._update_border)

    def _update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)

