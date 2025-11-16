# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from companies.widgets.company_tile import CompanyTile
from kivy.uix.button import Button

# class CompanySelector(ScrollView):
#     def __init__(self, companies, on_select, **kwargs):
#         super().__init__(**kwargs)
#         # Set up grid
#         self.grid = GridLayout(cols=3, spacing=10, size_hint_y=1)
       
#         self.grid.bind(minimum_height=self.grid.setter('height'))
#         self.add_widget(self.grid)

#         for company in companies:
#             tile = CompanyTile(company, on_select, size=(512, 512))
#             self.grid.add_widget(tile)

# class CompanySelector(BoxLayout):
#     def __init__(self, companies, on_select, **kwargs):
#         super().__init__(orientation='horizontal', **kwargs)

#         self.prev_btn = Button(text='<', on_release=self.previous_company, size_hint=(None, 1), width=50)
#         self.next_btn = Button(text='>', on_release=self.next_company, size_hint=(None, 1), width=50)

#         self.scroll = ScrollView(size_hint=(1, 1))
#         self.grid = GridLayout(cols=3, spacing=10, size_hint_y=None)
#         self.grid.bind(minimum_height=self.grid.setter('height'))
#         self.scroll.add_widget(self.grid)

#         self.add_widget(self.prev_btn)
#         self.add_widget(self.scroll)
#         self.add_widget(self.next_btn)

#         for company in companies:
#             tile = CompanyTile(company, on_select, size=(512, 512))
#             self.grid.add_widget(tile)

# widgets/company_selector.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from companies.widgets.company_tile import CompanyTile
from companies.manager import CompanyManager

class CompanySelector(BoxLayout):
    def __init__(self, on_edit, on_play, on_delete, on_new, **kwargs):
        super().__init__(orientation='vertical', spacing=10, **kwargs)

        # Set a manager, and use it to get all companies plus a blank spot for new
        self.manager = CompanyManager()
        self.companies = self.manager.get_with_new_slot()
        self.currentslot = 0

        # Label
        self.label = Label(text="Select Company", font_size='18sp', size_hint=(1, None), height=30)
        self.add_widget(self.label)

        # Carousel row
        self.carousel = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=220)
        self.add_widget(self.carousel)

        self.prev_btn = Button(text='<', size_hint=(None, 1), width=50)
        self.next_btn = Button(text='>', size_hint=(None, 1), width=50)
        self.tile = CompanyTile(self.get_current_company(), self.launch_editor)

        self.prev_btn.bind(on_release=self.previous)
        self.next_btn.bind(on_release=self.next)

        self.carousel.add_widget(self.prev_btn)
        self.carousel.add_widget(self.tile)
        self.carousel.add_widget(self.next_btn)

        # Button row
        self.button_row = BoxLayout(size_hint=(1, None), height=50, spacing=10)
        self.edit_btn = Button(text='Edit')
        self.play_btn = Button(text='Play')
        self.delete_btn = Button(text='Delete')

        self.edit_btn.bind(on_release=self.edit)
        self.play_btn.bind(on_release=self.play)
        self.delete_btn.bind(on_release=self.delete)

        self.button_row.add_widget(self.edit_btn)
        self.button_row.add_widget(self.play_btn)
        self.button_row.add_widget(self.delete_btn)
        self.add_widget(self.button_row)

        # External callbacks
        self.on_edit = on_edit
        self.on_play = on_play
        self.on_delete = on_delete
        self.on_new = on_new

        self.refresh_ui()

    def get_current_company(self):
        return self.manager.get(self.currentslot)

    def get_current_index(self):
        return self.currentslot
    
    def select(self, index):
        '''Jump to a specific slot.'''
        if 0 <= index < len(self.companies):
            self.currentslot = index
            self.refresh_ui()
    
    def refresh(self):
        self.companies = self.manager.get_with_new_slot()
        self.currentslot = min(self.currentslot, len(self.companies) - 1)
        self.refresh_ui()

    def is_new_company(self):
        return self.get_current_company() is None

    def previous(self, instance):
        self.currentslot = (self.currentslot - 1) % len(self.companies)
        self.refresh_ui()

    def next(self, instance):
        self.currentslot = (self.currentslot + 1) % len(self.companies)
        self.refresh_ui()

    def refresh_ui(self):
        self.tile.update(self.get_current_company())
        if self.is_new_company():
            self.edit_btn.text = "New"
            self.play_btn.disabled = True
            self.delete_btn.disabled = True
        else:
            self.edit_btn.text = "Edit"
            self.play_btn.disabled = False
            self.delete_btn.disabled = False

    def edit(self, instance):
        if self.is_new_company():
            self.on_new()
        else:
            self.on_edit(self.get_current_company())

    def play(self, instance):
        if not self.is_new_company():
            self.on_play(self.get_current_company())

    def delete(self, instance):
        if not self.is_new_company():
            self.on_delete(self.currentslot)

    def launch_editor(self, company):
        if company:
            self.on_edit(company)
