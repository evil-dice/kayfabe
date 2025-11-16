from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior

class CompanyTile(ButtonBehavior, BoxLayout):
    def __init__(self, company, on_press_callback, **kwargs):
        super().__init__(orientation='vertical', size_hint=(1, 1), spacing=5, padding=5, **kwargs)
        self.company = company
        self.on_press_callback = on_press_callback

        self.logo = Image(source=company.logo, allow_stretch=False, keep_ratio=True)
        self.name = Label(text=company.name, font_size='14sp', size_hint=(1, None), height=30)

        self.add_widget(self.logo)
        self.add_widget(self.name)
        

    def on_press(self):
        self.on_press_callback(self.company)

    def update(self, new_company):
        self.company = new_company

        if new_company is None:
            self.logo.source = "assets/images/genericcompany.png"
            self.name.text = "New Company..."
        else:
            self.logo.source = new_company.logo
            self.name.text = new_company.name

        self.logo.reload()

    
    