from core.widgets.panel   import Panel
from core.widgets.labels  import HeaderLabel, FieldLabel, BodyLabel
from core.widgets.tile    import Tile
from kivy.uix.button      import ButtonBehavior
from kivy.uix.gridlayout  import GridLayout

class SaveSlot(Panel, ButtonBehavior):
    def __init__(self, target, name, slot, **kwargs):
        super().__init__(orientation='vertical', radius=[30], size_hint=(1, None), height=240, **kwargs)  # width=170, height=240,

        # Layout
        # self.grid = GridLayout(cols=1)
        # self.add_widget(self.grid)

        # Build Tile
        self.tile = Tile(target, if_none="assets/images/genericcompany.png", size_hint_x=0.9, pos_hint={'center_x': 0.5}) # Using if_none to add dict reference
        self.add_widget(self.tile)

        # Build Labels
        self.label = BodyLabel(text=f"{name}", font_size=22, size_hint=(None, 1), halign='center')
        # self.label.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        self.add_widget(self.label)
        # self.label = HeaderLabel(text=f"{name}", font_size=32, size_hint=(None, 1), height=70, valign='top')
        # # self.label.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        # self.add_widget(self.label)
        
        # self.slot = FieldLabel(text=f"Slot {slot}")
        # # self.slot.bind(size=lambda inst, val: setattr(inst, "text_size", (inst.width, None)))
        # self.add_widget(self.slot)

class NewSaveSlot(SaveSlot):
    def __init__(self, on_add, **kwargs):
        super().__init__(target=None, name="Add New Company", slot="New", **kwargs)
        self.tile.if_none = "assets/images/genericcompany.png"
        self.bind(on_release=lambda _: on_add())





