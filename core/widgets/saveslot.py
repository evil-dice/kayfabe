from core.widgets.panel   import Panel
from core.widgets.labels  import HeaderLabel, FieldLabel, BodyLabel, CaptionLabel
from core.widgets.tile    import Tile
from kivy.uix.button      import ButtonBehavior
from kivy.uix.gridlayout  import GridLayout
from kivy.metrics         import dp
from kivy.core.window     import Window

from companies.manager import CompanyManager
from state.universe import Universe

class SaveSlot(ButtonBehavior, Panel):
    def __init__(self, target, name, slot, **kwargs):
        super().__init__(orientation='vertical', radius=[30], size_hint=(None, None), **kwargs)  # width=170, height=240,

        # Set size by fraction of screen space, and update if resized
        self.size=(Window.width * 0.135, Window.height * 0.40)
        Window.bind(size=self._update_size)

        # Expose company object
        self.target = target

        # Register event to close modal
        self.register_event_type('on_saveslot_selected')  # declare custom event

        # Layout
        # self.grid = GridLayout(cols=1)
        # self.add_widget(self.grid)

        # Build Tile
        self.tile = Tile(self.target, if_none="assets/images/genericcompany.png", size_hint_x=0.9, pos_hint={'center_x': 0.5}) # Using if_none to add dict reference
        self.add_widget(self.tile)

        # Build Labels
        self.label = HeaderLabel(text=f"{name}", font_size=dp(24), size_hint=(None, 1), halign='center')
        # self.label.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        self.add_widget(self.label)
        # self.label = HeaderLabel(text=f"{name}", font_size=32, size_hint=(None, 1), height=70, valign='top')
        # # self.label.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        # self.add_widget(self.label)
        
        self.slot = CaptionLabel(text=f"Slot {slot}")
        self.add_widget(self.slot)
    
    def _update_size(self, window, size):
        self.size = (window.size[0] * 0.135, window.size[1] * 0.40)
    
    def on_release(self):
        # Set the active company in the Universe singleton
        CompanyManager().load(self.target['slot'])

        # fire the event
        self.dispatch('on_saveslot_selected', self.target)

    def on_saveslot_selected(self, company):
        """Default handler (does nothing)."""
        pass






