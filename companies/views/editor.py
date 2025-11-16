from companies.manager import CompanyManager
from companies.model import Company
from core.widgets.forms import FormField
from core.widgets.panel import Panel
from core.editor_base import EditorBase

class CompanyEditor(EditorBase):
    def __init__(self, **kwargs):
        super().__init__(manager=CompanyManager(), model_class=Company, **kwargs)

        # UI setup
        self.name_input = FormField(hint_text="Company Name")
        self.owner_input = FormField(hint_text="Owner")
        self.logo_input = FormField(hint_text="Logo Path")

        form = Panel(width=400)
        form.add_widget(self.name_input)
        form.add_widget(self.owner_input)
        form.add_widget(self.logo_input)
        self.add_widget(form)

    def populate_fields(self, company):
        self.name_input.text = company.name
        self.owner_input.text = company.owner
        self.logo_input.text = company.logo

    def clear_fields(self):
        self.name_input.text = ""
        self.owner_input.text = ""
        self.logo_input.text = ""

    def update_item_from_fields(self, company):
        company.name = self.name_input.text
        company.owner = self.owner_input.text
        company.logo = self.logo_input.text