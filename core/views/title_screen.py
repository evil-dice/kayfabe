# Framework
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.floatlayout   import FloatLayout
from kivy.uix.gridlayout    import GridLayout
from kivy.uix.button        import Button
from kivy.graphics          import Rectangle, Color
from kivy.core.window       import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label         import Label
from kivy.uix.scrollview    import ScrollView


# Modules
from companies.model        import Company 
from companies.manager      import CompanyManager
from state.universe         import Universe
# from companies.widgets.company_selector import CompanySelector
from core.widgets.panel     import Panel
from core.widgets.labels    import BodyLabel, FieldLabel
from core.widgets.tile      import Tile
from core.widgets.saveslot  import SaveSlot, NewSaveSlot
from core.widgets.buttons   import MainMenuButton


class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background Layer
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(source="assets/images/titlescreen3.png", pos=self.pos, size=Window.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # UI Layer
        self.root = RelativeLayout()
        self.add_widget(self.root)

        # Content area
        self.content = Panel(orientation='vertical', size_hint=(0.35, 0.4), pos_hint={'center_x':0.29, 'center_y':0.35}, spacing=2, radius=[20])
        self.root.add_widget(self.content)

        # Main Menu
        self.MainMenu_Label = BodyLabel("Select an option to get started:", halign="center")
        self.MainMenu_New = MainMenuButton(text="NEW", label_to_update=self.MainMenu_Label, hover_text="Start a new universe.")
        self.MainMenu_Continue = MainMenuButton(text="CONTINUE", label_to_update=self.MainMenu_Label, hover_text="Pick up where you left off.")
        self.MainMenu_Load = MainMenuButton(text="LOAD", label_to_update=self.MainMenu_Label, hover_text="Choose a Universe.")
        self.MainMenu_Import = MainMenuButton(text="IMPORT", label_to_update=self.MainMenu_Label, hover_text="Load a shared or downloaded Universe file.")
        self.MainMenu_Export = MainMenuButton(text="EXPORT", label_to_update=self.MainMenu_Label, hover_text="Save your Universe to share with others.")
        self.MainMenu_Version = FieldLabel("Version 0.1", halign="center")

        self.content.add_widget(self.MainMenu_Label)
        self.content.add_widget(self.MainMenu_New)
        self.content.add_widget(self.MainMenu_Continue)
        self.content.add_widget(self.MainMenu_Load)
        self.content.add_widget(self.MainMenu_Import)
        self.content.add_widget(self.MainMenu_Export)
        self.content.add_widget(self.MainMenu_Version)

        # Get company metadata
        self.companies = CompanyManager().list_slots()

        # # Add "New" slot
        # self.new_company = NewSaveSlot(on_add=None, size_hint_y=1)
        # self.container.add_widget(self.new_company)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def manage_company(self, company):
        print(f"Managing company: {company.name}")

    def play_company(self, company):
        Universe().company = company
        Universe().initialize()
        print(f"Playing company: {company.name}")

    def delete_company(self, index):
        company = self.company_manager.get(index)
        name = company.name
        self.company_manager.delete(index)
        self.company_manager.save_all()
        self.selector.refresh()
        print(f"🗑️ Deleted company: {name}")
    
    def create_new_company(self):
        print("🆕 Creating a new company...")
        Universe().company = Company(name="", owner="", saveslot=self.company_manager.count())
        self.manager.current = "company_editor"

    def launch_editor(self, company):
        print(f"🛠️ Launching editor for {company.name}")
