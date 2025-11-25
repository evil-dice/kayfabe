from kivy.core.window import Window
from kivy.clock import Clock

class RealSizeHint:
    '''Disable size hints and use window size to calculate a real size in pixels.'''
    def __init__(self, width_percent=None, height_percent=None, **kwargs):
        super().__init__(**kwargs)
        self._width_percent = width_percent
        self._height_percent = height_percent

        # Disable normal size_hint
        self.size_hint = (None, None)

        # Bind to window resize
        Window.bind(size=self._update_size)

        # Schedule a recalculation after the first frame
        Clock.schedule_once(lambda dt: self._update_size(Window, Window.size), 0)
    
    def _update_size(self, instance, size):
        if self._width_percent is not None:
            self.width = size[0] * self._width_percent
        if self._height_percent is not None:
            self.height = size[1] * self._height_percent
