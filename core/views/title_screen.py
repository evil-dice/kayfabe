# Framework
from kivy.uix.screenmanager       import Screen
from kivy.graphics                import Rectangle, Color
from kivy.core.window             import Window
from kivy.uix.relativelayout      import RelativeLayout
from kivy.uix.floatlayout         import FloatLayout

# Modules
from companies.model              import Company
from companies.manager            import CompanyManager
from companies.views.company_editor import CompanyEditor
from core.views.universe_selector import UniverseSelector
from core.widgets.panel           import Panel
from core.widgets.labels          import BodyLabel, FieldLabel, CaptionLabel
from core.widgets.buttons         import MainMenuButton
from state.universe               import Universe
from utils.realsizehint           import RealSizeHint

class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background Layer
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(source="assets/images/titlescreen3.png", pos=self.pos, size=Window.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # UI Layer
        self.root = FloatLayout()
        self.add_widget(self.root)

        # Content area
        self.content = Panel(orientation='vertical', shrink_to_fit=True, size_hint_x=0.3, pos_hint={'center_x':0.29, 'center_y':0.35}, spacing=2, radius=[20])
        
        self.root.add_widget(self.content)

        # Main Menu
        self.MainMenu_Label = BodyLabel("Select an option to get started:", halign="center")

        # Define buttons
        self.MainMenu_New = MainMenuButton(text="NEW", label_to_update=self.MainMenu_Label, hover_text="Start a new universe.")
        self.MainMenu_Continue = MainMenuButton(text="CONTINUE", label_to_update=self.MainMenu_Label, hover_text="Pick up where you left off.")
        self.MainMenu_Load = MainMenuButton(text="LOAD", label_to_update=self.MainMenu_Label, hover_text="Choose a Universe.")
        self.MainMenu_Import = MainMenuButton(text="IMPORT", label_to_update=self.MainMenu_Label, hover_text="Load a shared or downloaded Universe file.")
        self.MainMenu_Export = MainMenuButton(text="EXPORT", label_to_update=self.MainMenu_Label, hover_text="Save your Universe to share with others.")
        self.MainMenu_Version = CaptionLabel("Version 0.1", halign="left")

        # Assign methods
        self.MainMenu_New.bind(on_release=self.new_universe)
        self.MainMenu_Load.bind(on_release=self.show_universe_selector)
        self.MainMenu_Continue.bind(on_release=self.show_gameplay_screen)

        # Add buttons
        self.content.add_widget(self.MainMenu_Label)
        self.content.add_widget(self.MainMenu_New)
        self.content.add_widget(self.MainMenu_Continue)
        self.content.add_widget(self.MainMenu_Load)
        self.content.add_widget(self.MainMenu_Import)
        self.content.add_widget(self.MainMenu_Export)
        self.add_widget(self.MainMenu_Version)

        # Get company metadata
        self.companies = CompanyManager().list_slots

        # # Add "New" slot
        # self.new_company = NewSaveSlot(on_add=None, size_hint_y=1)
        # self.container.add_widget(self.new_company)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def show_universe_selector(self, instance):
        self.universe_select = UniverseSelector()
        self.universe_select.open()

    def new_universe(self, *args):
        # Create a fresh Company
        Universe().company = Company(name="New Company")

        # Switch to editor screen
        Universe().change_screen("company_editor")
    
    def show_gameplay_screen(self, *args):
        Universe().change_screen("gameplay_hub")


