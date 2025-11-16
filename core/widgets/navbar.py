from kivy.uix.boxlayout import BoxLayout
from state.universe import Universe
from kivy.uix.button import Button

class SimpleNavBar(BoxLayout):
    def __init__(self, screen_manager, screen_names, **kwargs):
        super().__init__(orientation='horizontal', spacing=10, size_hint_y=None, height=50, **kwargs)
        self.sm = screen_manager
        self.buttons = {}

        for name in screen_names:
            btn = Button(
                text=name.title(),
                size_hint_x=1,
                background_color=(0.2, 0.2, 0.2, 1),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_release=lambda btn, name=name: self.switch_to(name))
            self.buttons[name] = btn
            self.add_widget(btn)

        self.sm.bind(current=self.update_active)

    def switch_to(self, name):
        self.sm.current = name

    def update_active(self, *args):
        for name, btn in self.buttons.items():
            if name == self.sm.current:
                btn.background_color = (0.4, 0.4, 0.8, 1)  # Active
            else:
                btn.background_color = (0.2, 0.2, 0.2, 1)  # Inactive
