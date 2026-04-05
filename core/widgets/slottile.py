from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from state.universe import Universe

class SlotTile(BoxLayout):
    def __init__(self, slot_name, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.slot_name = slot_name
        self.refresh()

    def refresh(self):
        self.clear_widgets()
        universe = Universe()

        slot_obj = getattr(universe, self.slot_name)

        if slot_obj and getattr(slot_obj, "logo_path", None):
            # Show logo image
            self.add_widget(Image(source=slot_obj.logo_path))
        else:
            # Show + button
            self.add_widget(Button(text="+", on_press=self.open_editor))

    def open_editor(self, *args):
        # Replace with your screen manager navigation
        print(f"Open editor for {self.slot_name}")