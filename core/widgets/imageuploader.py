from kivy.uix.boxlayout import BoxLayout
from kivy.uix
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.metrics import dp

class ImagePreview(ButtonBehavior, BoxLayout):
    def __init__(self, initial_source=None, **kwargs):
        super().__init__(orientation='vertical', spacing=10, size_hint=(1, None), width=dp(240), pos_hint={'center_x': 0.5, 'center_y':0.5}, **kwargs)

        # Image widget
        self.image = Image(
            source=initial_source or '',
            size_hint_x=None,
            size_hint_y=None,
            pos_hint={'center_x': 0.5, 'center_y':0.5},
            height=200,
            width=200,
            # allow_stretch=True,
            # keep_ratio=True
        )
        self.add_widget(self.image)

        # Browse button
        self.browse_button = Button(
            text='Browse Image',
            size_hint_x=None,
            size_hint_y=None,
            width=200,
            height=30,
            pos_hint={'center_x': 0.5, 'center_y':0.5}
        )
        self.browse_button.bind(on_release=self.open_filechooser)
        self.add_widget(self.browse_button)

    def open_filechooser(self, *args):
        chooser = FileChooserListView(filters=['*.png', '*.jpg', '*.jpeg'], path='.')

        # Preview image widget
        preview = Image(size_hint_y=None, height=200, allow_stretch=True, keep_ratio=True)

        # Layout: chooser + preview + confirm button
        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(chooser)
        layout.add_widget(preview)

        confirm_button = Button(text='Select', size_hint_y=None, height=40)
        layout.add_widget(confirm_button)

        popup = Popup(title='Select Image', content=layout, size_hint=(0.7, 0.7))

        # Live preview on selection
        def on_selection(instance, selection):
            if selection:
                preview.source = selection[0]
                preview.reload()

        chooser.bind(selection=on_selection)

        # Confirm selection
        def on_confirm(instance):
            selection = chooser.selection
            if selection:
                self.image.source = selection[0]
                self.image.reload()
                popup.dismiss()

        confirm_button.bind(on_release=on_confirm)
        popup.open()
