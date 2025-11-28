# widgets/company_selector.py

from kivy.uix.boxlayout   import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.button      import Button
from kivy.uix.label       import Label

from core.widgets.labels  import Header, FieldLabel
# from companies.widgets.company_tile import CompanyTile
from companies.manager    import CompanyManager
from core.widgets.panel   import Panel
from core.widgets.buttons import ImageButton
from core.widgets.tile    import Tile
from state.universe       import Universe


class CompanySelector(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, **kwargs)

        # Manager
        self.manager = CompanyManager()

        # Get company list
        self.companies = self.manager.list_slots()

        # Set current index
        self.index = -1

        # Root for Layout Positioning
        self.root = BoxLayout()
        self.add_widget(self.root)

        # # # Layout row 1
        # self.row = BoxLayout(orientation='horizontal', size_hint=(1, 1), pos_hint={'center_x': 0.25, 'center_y': 0.25})
        # self.root.add_widget(self.row)

        # Define widgets
        self.prev_btn = Button(text='<', size_hint=(None, 0.5), width=30, pos_hint={'center_y': 0.5})
        self.next_btn = Button(text='>', size_hint=(None, 0.5), width=30, pos_hint={'center_y': 0.5})
        self.prev_btn.bind(on_release=lambda _: self.move(-1))
        self.next_btn.bind(on_release=lambda _: self.move(1))
        self.tile = Tile(Universe().company, self.launch_editor)

        # Add to Row 1
        self.root.add_widget(self.prev_btn)
        self.root.add_widget(self.tile)
        self.root.add_widget(self.next_btn)


    def move(self, step):
        self.index = (self.index + step) % len(self.companies)
        self.refresh_ui()

    def refresh_ui(self):
        slot = self.companies[self.index]
        self.tile.update(slot)

    def launch_editor():
        print("This should launch to an editor screen")




# class CompanySelector(BoxLayout):
#     def __init__(self, on_edit, on_play, on_delete, on_new, **kwargs):
#         super().__init__(orientation='vertical', spacing=10, **kwargs)

#         # Set a manager, and use it to get all companies plus a blank spot for new
#         self.manager = CompanyManager()
#         self.companies = self.manager.list_slots()

# class CompanySelector(BoxLayout):
#     def __init__(self, on_select=None, on_new=None, **kwargs):
#         super().__init__(orientation='vertical', spacing=10, **kwargs)

#         self.manager = CompanyManager()
#         self.slots = self.manager.list_slots()
#         self.index = 0

#         # Title
#         self.add_widget(Header(text="Select Company",
#                               size_hint=(1, None), height=30))

#         # Carousel row
#         row = BoxLayout(orientation='horizontal', spacing=10,
#                         size_hint=(1, None), height=220)
#         self.prev_btn = Button(text='<', size_hint=(None, 1), width=50)
#         self.next_btn = Button(text='>', size_hint=(None, 1), width=50)
#         self.tile = CompanyTile(self.slots[self.index], self.launch_editor)

#         self.prev_btn.bind(on_release=lambda _: self.move(-1))
#         self.next_btn.bind(on_release=lambda _: self.move(1))

#         row.add_widget(self.prev_btn)
#         row.add_widget(self.tile)
#         row.add_widget(self.next_btn)
#         self.add_widget(row)

#         # External callbacks
#         self.on_select = on_select
#         self.on_new = on_new

#         self.refresh_ui()

#     def move(self, step):
#         self.index = (self.index + step) % len(self.slots)
#         self.refresh_ui()

#     def refresh_ui(self):
#         slot = self.slots[self.index]
#         self.tile.update(slot)

#     def launch_editor(self, slot_meta):
#         if slot_meta["name"] is None:
#             self.on_new()
#         else:
#             company = self.manager.load(slot_meta["slot"])
#             self.on_select(company)
