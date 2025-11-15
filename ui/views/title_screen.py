from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.label import Label
from ui.widgets.content_area import ContentArea

from core.company import Company 
from core.company_manager import CompanyManager
from state.universe import Universe
from ui.widgets.company_tile import CompanyTile
from ui.widgets.company_selector import CompanySelector

class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background Layer
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(source="assets/images/Titlescreen.png", pos=self.pos, size=Window.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # UI Layer
        self.content_area = ContentArea()
        self.add_widget(self.content_area)

        # Load companies
        self.company_manager = CompanyManager()
        self.company_manager.load_all()

        # Label Box
        self.title_label = Label(text="Select Company", font_size='18sp', size_hint=(1, None), height=30)
        self.content_area.layout.add_widget(self.title_label, index=0)  # Add at the top

        # Selector
        self.selector = CompanySelector(
            on_edit=self.manage_company,
            on_play=self.play_company,
            on_delete=self.delete_company,
            on_new=self.create_new_company
        )
        self.content_area.layout.add_widget(self.selector)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def manage_company(self, company):
        print(f"⚙️ Managing company: {company.name}")

    def play_company(self, company):
        Universe().company = company
        Universe().initialize()
        print(f"🎮 Playing company: {company.name}")

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
