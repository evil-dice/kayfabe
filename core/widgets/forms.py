from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from core.widgets.labels import FieldLabel, FormField

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

# class FieldRow(GridLayout):
#     def __init__(self, label_text, **kwargs):
#         super().__init__(cols=2, spacing=spacing, size_hint_y=None, size_hint_x=1, **kwargs)

#         self.bind(minimum_height=self.setter('height'))

#         # Label: fixed width
#         self.label = FieldLabel(
#             text=label_text,
#             size_hint_x=None,
#             width=label_width
#         )
#         self.add_widget(self.label)

#         # Field: fills remaining space
#         self.field = TextInput(
#             size_hint_x=1,
#             size_hint_y=None,
#             height=field_height,
#             multiline=False,
#             background_color=(0.2, 0.2, 0.2, 1),
#             foreground_color=(1, 1, 1, 1),
#             cursor_color=(1, 0, 0, 1),
#             padding=(10, 10)
#         )
#         self.add_widget(self.field)

class FieldRow(BoxLayout):
    def __init__(self, labeltext, **kwargs):
        super().__init__()

        # Set properties
        self.orientation = 'horizontal'
        self.spacing = 0
        self.size_hint_x = 1
        self.size_hint_y = None
        self.padding = (0, 5)
        self.bind(minimum_height=self.setter('height'))

        # define widgets
        label = FieldLabel(text=f"{labeltext}:", size_hint_x=None, width=130)
        field = FormField()

        # Align label height with field height
        label.height = field.height

        # add widgets
        self.add_widget(label)
        self.add_widget(field)

class ButtonRow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
        
        # Set properties
        self.orientation = 'horizontal'
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
        


