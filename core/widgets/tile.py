from kivy.uix.button  import ButtonBehavior
from kivy.uix.image   import Image
from kivy.graphics    import Color, Line
from core.widgets.labels import COLORS

class Tile(ButtonBehavior, Image):
    '''Minimalist tile, re-usable. Border Property is size of the border + preferred color.'''
    def __init__(self, target, on_select=None, if_none="assets/images/generic.png", border=False, border_weight=2, border_color=COLORS['secondary'], size_hint_x=1, **kwargs):
        super().__init__(**kwargs)

        # Use update() to resolve dict vs. object
        self.source = if_none
        self.slot = None
        if target is not None:
            self.update(target)

        # Force square aspect ratio
        self.size_hint_x = size_hint_x
        self.size_hint_y = None  # To disable automatic vertical sizing
        # Keep height equal to width
        self.bind(width=self._update_height)

        # Callback when clicked
        if on_select:
            self.bind(on_release=lambda _: on_select(target))
    
        # Manage borders
        with self.canvas.after:
            self.border_color_instr = Color(border_color)
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=border_weight)

        self.bind(pos=self._update_border, size=self._update_border)

        if not border:
            self.border_color_instr.a = 0  # alpha = 0 hides it

        # Keep border updated when widget resizes/moves
        self.bind(pos=self._update_border, size=self._update_border)

    def _update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)

    def _update_width(self, *args):
        self.width = self.height

    def _update_height(self, *args):
        self.height = self.width
    
    def update(self, object_or_meta):
        """Accept either metadata dict or full Company object."""
        if object_or_meta is None:
            self.source = ""
            self.slot = None
            return

        if isinstance(object_or_meta, dict):
            self.source = object_or_meta.get("logo", "")
            self.slot = object_or_meta.get("slot")
        else:
            self.source = getattr(object_or_meta, "logo", "")
            self.slot = getattr(object_or_meta, "saveslot", None)
