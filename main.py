# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from state.universe import Universe
from core.widgets.navbar import SimpleNavBar
# from shell.title_screen import TitleScreen
from core.views.title_screen import TitleScreen
from companies.views.company_editor import CompanyEditor

class WrestleVerseApp(App):
    def build(self):
        Window.size = (1280, 720)  # Optional: set default window size
        
        # Bind Universe.active_screen to ScreenManager.current
        universe = Universe()
        universe.bind(active_screen=lambda inst, val: setattr(sm, "current", val))

        sm = ScreenManager()
        sm.add_widget(TitleScreen(name="title"))
        sm.add_widget(CompanyEditor(name="company_editor"))

        # nav = SimpleNavBar(screen_names=["title", "company_editor"], screen_manager=sm)

        root = BoxLayout(orientation='vertical')
        # root.add_widget(nav)
        root.add_widget(sm)
        return root

if __name__ == "__main__":
    WrestleVerseApp().run()