from kivy.core.window import Window

class HoverBehavior(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self._on_mouse_pos)
        self._hovered = False

    def _on_mouse_pos(self, window, pos):
        if not self.get_root_window():
            return
        inside = self.collide_point(*self.to_widget(*pos))
        if inside and not self._hovered:
            self._hovered = True
            self.on_hover(True)
        elif not inside and self._hovered:
            self._hovered = False
            self.on_hover(False)

    def on_hover(self, value):
        pass  # override in subclass