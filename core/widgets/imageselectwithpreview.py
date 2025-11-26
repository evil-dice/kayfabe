from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.properties import StringProperty

class ClickableImage(ButtonBehavior, Image):
    """An Image that behaves like a button."""
    pass


class ImagePreview(BoxLayout):
    source = StringProperty('')

    def __init__(self, target=None, attr=None,
                 size_hint_x=1, size_hint_y=None, height=200, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.size_hint_x = size_hint_x
        self.size_hint_y = size_hint_y
        self.height = height

        self.target = target
        self.attr = attr

        # Clickable image
        self.image = ClickableImage(
            source="assets/images/no_image.png",
            size_hint=(None, None),
            height=200, width=200,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.image.bind(on_release=self.open_filechooser)
        self.add_widget(self.image)

        # Keep image in sync with source property
        self.bind(source=self._update_image)

        # Initialize from target if provided
        if self.target and self.attr:
            self.source = str(getattr(self.target, self.attr, ""))

    def _update_image(self, instance, value):
        self.image.source = value or "assets/images/no_image.png"
        self.image.reload()

    def open_filechooser(self, *args):
        chooser = FileChooserListView(filters=['*.png','*.jpg','*.jpeg'], path='.')

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
        def on_selection(instance, selection, *args):
            if selection:
                preview.source = selection[0]
                preview.reload()

        chooser.bind(selection=on_selection)

        # Confirm selection
        def on_confirm(instance):
            selection = chooser.selection
            if selection:
                path = selection[0]
                self.source = path
                if self.target and self.attr:
                    setattr(self.target, self.attr, path)
                popup.dismiss()

        confirm_button.bind(on_release=on_confirm)
        popup.open()

