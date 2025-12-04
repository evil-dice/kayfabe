# Modal load screen from main menu

# Framework
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.floatlayout   import FloatLayout
from kivy.uix.gridlayout    import GridLayout
from kivy.uix.button        import Button
from kivy.graphics          import Rectangle, Color
from kivy.core.window       import Window
from kivy.uix.label         import Label
from kivy.uix.scrollview    import ScrollView

# Modules
from companies.model        import Company 
from companies.manager      import CompanyManager
from state.universe         import Universe
from core.widgets.panel     import Panel
from core.widgets.labels    import BodyLabel, FieldLabel
from core.widgets.tile      import Tile
from core.widgets.saveslot  import SaveSlot
from core.widgets.buttons   import MainMenuButton

# Modules

# Examples
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button

# scrollview = ScrollView(size_hint=(1, None), size=(400, 300))

# layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
# layout.bind(minimum_height=layout.setter('height'))

# for i in range(20):
#     layout.add_widget(Button(text=f"Slot {i}", size_hint_y=None, height=40))

# scrollview.add_widget(layout)

class UniverseSelector(ModalView):
    def __init__(self, **kwargs):
        super().__init__(auto_dismiss=True, size_hint=(0.85, 0.85), **kwargs)
        self.background = ""          # no image
        self.background_color = (0,0,0,0)  # fully transparent

        # set initial size to 85% of window
        self.size = (Window.width * 0.85, Window.height * 0.85)

        # update size if window resizes
        Window.bind(size=self._update_size)

        # UI Layer
        self.root = ScrollView(size=self.size)
        self.add_widget(self.root)

        # Content area
        self.content = GridLayout(cols=6, spacing=10, size_hint=(1, 1))
        # self.content.bind(minimum_height=self.content.setter('height'))
        self.root.add_widget(self.content)

        # Add content
        for company in CompanyManager().list_slots():
            # Create save slot
            self.slot = SaveSlot(company, company['name'], company['slot'])
            self.slot.bind(on_saveslot_selected=self._slot_selected)
            self.content.add_widget(self.slot)

    def _update_size(self, window, size):
        self.size = (self.size[0] * 0.85, self.size[1] * 0.85)
    
    def _slot_selected(self, slot, company):
        print("SaveSlot clicked. Company updated:")
        print(Universe().company)

        # Close modal
        self.dismiss()
        
        # optionally trigger navigation to gameplay screen here
        Universe().change_screen("company_editor") # Testing... send to editor screen to check details

        