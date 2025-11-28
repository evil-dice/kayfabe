from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.metrics import dp
from kivy.properties import StringProperty

from core.widgets.labels import FieldLabel

class Header(Label):
    def __init__(self, text, **kwargs):
        super().__init__(text=text, font_size=24, bold=True, **kwargs)


class Field(BoxLayout):
    def __init__(self, label, attr, target, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.attr = attr
        self.target = target
        self.label = Label(text=label)
        self.input = TextInput(text=getattr(target, attr, ""), multiline=False)
        self.add_widget(self.label)
        self.add_widget(self.input)

    def get_value(self):
        return self.input.text

    def apply(self):
        setattr(self.target, self.attr, self.get_value())


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class FormField(TextInput):
    def __init__(self, size_hint=(1, None), height=30, multiline=False, **kwargs):
        super().__init__()

        # Fill width, fixed height
        self.size_hint = size_hint      # Fill width of parent, Disable vertical scaling
        self.height = height            # Explicit height
        self.multiline = multiline

# class FieldRow(BoxLayout):
#     value = StringProperty("")  # reactive property

#     def __init__(self, labeltext, bind_to=None, **kwargs):
#         super().__init__(orientation='horizontal',
#                          size_hint_x=1, size_hint_y=None,
#                          spacing=5, height=30, **kwargs)

#         # Label
#         label = FieldLabel(text=f"{labeltext}:", size_hint_y=None,
#                            valign="middle", height=30)

#         # Field
#         self.field = FormField(multiline=False)

#         # Bind field text ↔ value property
#         self.field.bind(text=self.setter("value"))
#         self.bind(value=self._update_field)

#         # # If a property to bind to was passed, connect it
#         # if bind_to is not None:
#         #     bind_to.bind(value=self.setter("value"))
#         #     self.bind(value=lambda inst, val: setattr(bind_to, "value", val))

#         self.add_widget(label)
#         self.add_widget(self.field)

#     def _update_field(self, instance, value):
#         self.field.text = value

class FieldRow(BoxLayout):
    def __init__(self, labeltext, target=None, attr=None, **kwargs):
        super().__init__(orientation='horizontal', size_hint_x=1, size_hint_y=None, spacing=5, height=30, **kwargs)

        self.target = target
        self.attr = attr

        # Label
        label = FieldLabel(text=f"{labeltext}:", size_hint_y=None, height=30, valign="middle", pos_hint={'center_y':0.5})

        # Field
        self.field = FormField()

        # Initialize field text from target attribute
        if self.target and self.attr:
            self.field.text = str(getattr(self.target, self.attr, ""))

            # Bind field changes → update model
            self.field.bind(text=self._update_model)

        self.add_widget(label)
        self.add_widget(self.field)

    def _update_model(self, instance, value):
        if self.target and self.attr:
            setattr(self.target, self.attr, value)

# class ImageFieldRow(BoxLayout):
#     '''Couples to ImagePreview on the same screen.'''
#     def __init__(self, preview=None, **kwargs):
#         super().__init__(orientation='horizontal', spacing=5, **kwargs)

#         self.preview = preview  # optional ImagePreview to sync with

#         # Text field
#         self.field = FormField(multiline=False, size_hint_x=1)
#         self.field.bind(text=self._on_text_change)
#         self.add_widget(self.field)

#         # Browse button
#         browse_btn = Button(text="Browse", size_hint_x=None, width=80)
#         browse_btn.bind(on_release=self.open_filechooser)
#         self.add_widget(browse_btn)

#     def _on_text_change(self, instance, value):
#         if self.preview:
#             self.preview.source = value

#     def open_filechooser(self, *args):
#         chooser = FileChooserListView(filters=['*.png','*.jpg','*.jpeg'], path='.')
#         popup = Popup(title='Select Image', content=chooser, size_hint=(0.7,0.7))

#         def on_selection(instance, selection):
#             if selection:
#                 path = selection[0]
#                 self.field.text = path  # update field
#                 if self.preview:
#                     self.preview.source = path
#                 popup.dismiss()

#         chooser.bind(on_submit=on_selection)
#         popup.open()

class ImageFieldRow(BoxLayout):
    filepath = StringProperty('')  # event-driven property

    def __init__(self, labeltext, target=None, attr=None, **kwargs):
        super().__init__(orientation='horizontal', spacing=5, height=30, size_hint_y=None, **kwargs)

        self.target = target
        self.attr = attr

        # Label
        label = FieldLabel(text=f"{labeltext}:", size_hint_x=0.2, size_hint_y=None, height=30)

        # Field
        self.field = FormField(size_hint_x=0.7)
        self.field.bind(text=self._on_text_change)

        # Browse button
        browse_btn = Button(text="Browse", size_hint_y=None, height=30, size_hint_x=0.2)
        browse_btn.bind(on_release=self.open_filechooser)

        self.add_widget(label)
        self.add_widget(self.field)
        # self.add_widget(browse_btn)

        # Initialize from target
        if self.target and self.attr:
            self.filepath = str(getattr(self.target, self.attr, ""))
            self.field.text = self.filepath

    def _on_text_change(self, instance, value):
        self.filepath = value
        if self.target and self.attr:
            setattr(self.target, self.attr, value)

    def open_filechooser(self, *args):
        chooser = FileChooserListView(filters=['*.png','*.jpg','*.jpeg'], path='.')
        popup = Popup(title='Select Image', content=chooser, size_hint=(0.7,0.7))

        def on_selection(instance, selection):
            if selection:
                path = selection[0]
                self.filepath = path
                self.field.text = path
                popup.dismiss()

        chooser.bind(on_submit=on_selection)
        popup.open()

class ButtonRow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation = 'horizontal', pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        
        # Set properties
        # self.orientation = 'horizontal'
        self.spacing = 10
        self.size_hint_x = 1
        self.size_hint_y = None
        self.padding = (0, 10)
        self.bind(minimum_height=self.setter('height'))

        save_btn = Button(text="OK", size_hint=(None, None), width=100, height=30)
        # save_btn.bind(on_release=None)
        
        cancel_btn = Button(text="Cancel", size_hint=(None, None), width=100, height=30)
        # cancel_btn.bind(on_release=None)
        
        self.add_widget(save_btn)
        self.add_widget(cancel_btn)
        


