# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from state.universe import Universe
from ui.widgets.navbar import SimpleNavBar
from ui.views.title_screen import TitleScreen
from ui.views.CompanyEditor import CompanyEditor

class WrestleVerseApp(App):
    def build(self):
        Window.size = (1280, 720)  # Optional: set default window size
        sm = ScreenManager()
        sm.add_widget(TitleScreen(name="title"))
        sm.add_widget(CompanyEditor(name="company_editor"))

        nav = SimpleNavBar(screen_names=["title", "company_editor"], screen_manager=sm)

        root = BoxLayout(orientation='vertical')
        root.add_widget(nav)
        root.add_widget(sm)

        def toggle_nav(_, screen_name):
            if screen_name == "title" and nav in root.children:
                root.remove_widget(nav)
            elif screen_name != "title" and nav not in root.children:
                root.add_widget(nav, index=len(root.children))  # Add at top

        Universe().bind(active_screen=toggle_nav)
        Universe().active_screen = "title"

        return root

if __name__ == "__main__":
    WrestleVerseApp().run()