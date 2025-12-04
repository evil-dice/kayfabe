# company_editor.py

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.button import Button

from companies.manager import CompanyManager
from core.widgets.panel import Panel
from core.widgets.labels import FieldLabel
from state.universe import Universe
from core.widgets.labels import HeaderLabel, BodyLabel
from core.widgets.forms import FieldRow  # your improved FieldRow
from core.widgets.forms import ImageFieldRow
from core.widgets.imageselectwithpreview import ImagePreview
from core.widgets.containers import Row

class CompanyEditor(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Bind to Universe instance
        self.universe = Universe()
        self.universe.bind(company=self._on_company_changed)

        # Background Layer
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(source="assets/images/company.png", pos=self.pos, size=Window.size)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # UI Layer
        root = FloatLayout()
        self.add_widget(root)

        # Panel
        self.form = Panel(padding=30, shrink_to_fit=True, size_hint_x=0.3, pos_hint = {'center_x': 0.3, 'center_y': 0.5})
        root.add_widget(self.form)
    
    def _on_company_changed(self, instance, company):
        self.populate_fields(company)
    
    def populate_fields(self, company):
        self.form.clear_widgets()
        if not company:
            return
        # Title
        self.form.add_widget(HeaderLabel(text="Company Details", halign="left"))

        # Fields
        self.form.add_widget(FieldRow("Name", target=company, attr="name"))
        self.form.add_widget(FieldRow("Alias", target=company, attr="alias"))
        self.form.add_widget(FieldRow("Owner", target=company, attr="owner"))

        # Define and add image upload
        self.form.add_widget(ImagePreview(target=company, attr="logo"))

        # Define Button Area
        # self.button_row = BoxLayout(orientation="horizontal", size_hint=(None, 1), height=30)
        self.button_row = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=30,
            spacing=10,
            pos_hint={'center_x': 0.5}
        )

        # Define Buttons
        ok_btn = Button(text="OK", size_hint=(1, None), height=30)
        ok_btn.bind(on_release=lambda *args: (CompanyManager().save(Universe().company), Universe().change_screen(Universe().previous_screen)))
        
        cancel_btn = Button(text="Cancel", size_hint=(1, None), height=30)
        cancel_btn.bind(on_release=lambda *args: Universe().change_screen(Universe().previous_screen))

        # Add to layout 
        self.form.add_widget(self.button_row)
        self.button_row.add_widget(ok_btn)
        self.button_row.add_widget(cancel_btn)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
