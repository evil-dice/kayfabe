from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

class UILayer(FloatLayout):
    '''
    Creates a layer over 
    '''
    def __init__(self, anchor='bottom_left', size_hint=(1, 1), debug_frame=False, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = size_hint
        self.pos_hint = self._anchor_to_pos(anchor, size_hint)

        # Internal layout fills the UILayer
        self.layout = BoxLayout(orientation='vertical',
                                spacing=20,
                                padding=20,
                                size_hint=(1, 1))
        self.add_widget(self.layout)

        # Optional debug frame
        if debug_frame:
            with self.canvas.after:
                Color(1, 0, 0, 1)  # Red border
                self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=2)
            self.bind(pos=self._update_border, size=self._update_border)

    def _anchor_to_pos(self, anchor, size_hint):
        return {
            'bottom_left': {'x': 0, 'y': 0},
            'bottom_right': {'x': 1 - size_hint[0], 'y': 0},
            'top_left': {'x': 0, 'y': 1 - size_hint[1]},
            'top_right': {'x': 1 - size_hint[0], 'y': 1 - size_hint[1]},
            'center': {'x': 0.5 - size_hint[0] / 2, 'y': 0.5 - size_hint[1] / 2}
        }.get(anchor, {'x': 0, 'y': 0})

    def _update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)
