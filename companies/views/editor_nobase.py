from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from companies.model import Company
from core.widgets.panel import Panel
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from companies.manager import CompanyManager
from core.widgets.labels import FieldLabel, Header, BodyText, FormField
from core.widgets.forms import FieldRow, ButtonRow
from core.widgets.imageuploader import ImagePreview
from state.universe import Universe

class CompanyEditor(Screen):
    def __init__(self, on_save=None, on_cancel=None, **kwargs):
        super().__init__(**kwargs)

        # Setup
        self.company_manager = CompanyManager()
        self.company = Universe().company or Company(name="", owner="", saveslot=self.get_next_slot())
        Universe().company = self.company  # Ensure it's set globally

        self.on_save = on_save
        self.on_cancel = on_cancel

        # Background
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(source="assets/images/company.png", pos=self.pos, size=Window.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # UI Layer
        root = FloatLayout()
        self.add_widget(root)

        # UI Elements
        form = Panel(width=400)
        form.pos_hint = {'center_x': 0.25, 'center_y': 0.5}
        root.add_widget(form)
        
        # Fields
        self.name_input = FormField(text=self.company.name, hint_text="Company Name", multiline=False)
        self.alias_input = FormField(text=getattr(self.company, "alias", ""), hint_text="Alias", multiline=False)
        self.owner_input = FormField(text=self.company.owner, hint_text="Owner", multiline=False)
        self.logo_input = FormField(text=self.company.logo, hint_text="Logo Path", multiline=False)

        form.add_widget(Header(text="Edit a Company"))
        form.add_widget(FieldRow("Company Name"))
        form.add_widget(FieldRow("Abbreviation"))
        form.add_widget(FieldRow("Company Owner"))
        form.add_widget(FieldRow("Logo Path"))


        # Logo preview
        # self.logo_preview = Image(source=self.company.logo, size_hint=(None, None), size=(200, 200))
        form.add_widget(ImagePreview(initial_source=self.company.logo))
        # form.add_widget(self.logo_preview)


        # Button Section
        form.add_widget(ButtonRow(size_hint_y=1, pos_hint={'center_x': 0.5, 'center_y': 0.5})) # Make real buttons later
        # Save button
        # save_btn = Button(text="Save", size_hint=(0.5, None), height=50)
        # save_btn.bind(on_release=self.save_company)
        # form.add_widget(save_btn)

        # Save button
        # cancel_btn = Button(text="Cancel", size_hint=(0.5, None), height=50)
        # cancel_btn.bind(on_release=self.save_company)
        # form.add_widget(cancel_btn)

        # Update logo preview on change
        # self.logo_input.bind(text=self.update_logo_preview)

    # def update_logo_preview(self, instance, value):
    #     self.logo_preview.source = value

    def get_next_slot(self):
        self.company_manager.load_all()
        return len(self.company_manager.get_all())

    def save_company(self, *args):
        self.company.name = self.name_input.text
        self.company.alias = self.alias_input.text
        self.company.owner = self.owner_input.text
        self.company.logo = self.logo_input.text
        self.company.saveslot = self.get_next_slot()

        self.company_manager.add(self.company)
        self.company_manager.save_all()

        if self.on_save:
            self.on_save(self.company)

        Universe().company = self.company
        # Navigate to next screen (e.g. ShowPlanner or TitleScreen)
    
    def cancel(self, *args):
        if self.on_cancel:
            self.on_cancel()
    
    def on_pre_enter(self): # Reload fields each time this is opened
        self.company = Universe().company
        self.name_input.text = self.company.name
        self.alias_input.text = getattr(self.company, "alias", "")
        self.owner_input.text = self.company.owner
        self.logo_input.text = self.company.logo
        # self.logo_preview.source = self.company.logo
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

