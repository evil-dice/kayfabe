from kivy.core.window import Window
from kivy.clock import Clock

def use_real_size(widget):
    """Convert widget.size_hint_x/y into fixed pixel sizes based on Window size."""

    # Grab the original hints
    w_hint = widget.size_hint_x
    h_hint = widget.size_hint_y

    def _update_size(win, size):
        if w_hint is not None:
            widget.width = size[0] * w_hint
        if h_hint is not None:
            widget.height = size[1] * h_hint

    # Disable normal size_hint so pixel sizes apply
    widget.size_hint_x = None
    widget.size_hint_y = None

    # Bind to window resize
    Window.bind(size=_update_size)

    # Schedule first update
    Clock.schedule_once(lambda dt: _update_size(Window, Window.size), 0)

    return widget