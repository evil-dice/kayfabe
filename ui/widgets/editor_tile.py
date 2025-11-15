from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Sample Usage:
# tile = EditorTileButton("images/companylogo.png", "AEW", self.launch_company_editor)

class EditorTileButton(Button):
    def __init__(self, icon_path, label_text, on_launch, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, None)
        self.size = (150, 150)
        self.padding = 10
        self.spacing = 5

        self.icon = Image(source=icon_path, allow_stretch=True, keep_ratio=False)
        self.label = Label(text=label_text, font_size='14sp', size_hint=(1, None), height=30)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.icon)
        layout.add_widget(self.label)
        self.add_widget(layout)

        self.bind(on_release=on_launch)

    def update_icon(self, new_path):
        self.icon.source = new_path
        self.icon.reload()

    def update_label(self, new_text):
        self.label.text = new_text
