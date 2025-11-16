from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from companies.model import Company
from companies.manager import CompanyManager
from state.universe import Universe

class CompanyEditor(Screen):
    def __init__(self, company=None, **kwargs):
        super().__init__(**kwargs)
        self.company = company or Company(name="", owner="", saveslot=self.get_next_slot())
        self.manager = CompanyManager()

        # Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(layout)

        # Fields
        self.name_input = TextInput(text=self.company.name, hint_text="Company Name", multiline=False)
        self.alias_input = TextInput(text=getattr(self.company, "alias", ""), hint_text="Alias", multiline=False)
        self.owner_input = TextInput(text=self.company.owner, hint_text="Owner", multiline=False)
        self.logo_input = TextInput(text=self.company.logo, hint_text="Logo Path", multiline=False)

        layout.add_widget(Label(text="Company Name"))
        layout.add_widget(self.name_input)
        layout.add_widget(Label(text="Alias"))
        layout.add_widget(self.alias_input)
        layout.add_widget(Label(text="Owner"))
        layout.add_widget(self.owner_input)
        layout.add_widget(Label(text="Logo Path"))
        layout.add_widget(self.logo_input)

        # Logo preview
        self.logo_preview = Image(source=self.company.logo, size_hint=(None, None), size=(200, 200))
        layout.add_widget(self.logo_preview)

        # Save button
        save_btn = Button(text="Save Company", size_hint=(1, None), height=50)
        save_btn.bind(on_release=self.save_company)
        layout.add_widget(save_btn)

        # Update logo preview on change
        self.logo_input.bind(text=self.update_logo_preview)

    def update_logo_preview(self, instance, value):
        self.logo_preview.source = value

    def get_next_slot(self):
        self.manager.load_all()
        return len(self.manager.get_all())

    def save_company(self, *args):
        # Update fields into self.company
        self.company.name = self.name_input.text
        self.company.alias = self.alias_input.text
        self.company.owner = self.owner_input.text
        self.company.logo = self.logo_input.text

        if self.company not in self.company_manager.get_all():
            # New company
            self.company.saveslot = self.get_next_slot()
            self.company_manager.add(self.company)

        # Persist all companies
        self.company_manager.save_all()

        Universe().company = self.company
        # Navigate to next screen (e.g. ShowPlanner or TitleScreen)

        if self.on_save:
            self.on_save(self.company)
    
    def load_company(self, company):
        """Populate fields with an existing company."""
        self.company = company
        Universe().company = company
        self.name_input.text = company.name
        self.alias_input.text = getattr(company, "alias", "")
        self.owner_input.text = company.owner
        self.logo_input.text = company.logo

    def new_company(self):
        """Clear fields for a new company."""
        self.company = Company(name="", owner="", saveslot=self.get_next_slot())
        Universe().company = self.company
        self.name_input.text = ""
        self.alias_input.text = ""
        self.owner_input.text = ""
        self.logo_input.text = ""
