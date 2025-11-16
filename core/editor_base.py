from kivy.uix.screenmanager import Screen
from kivy.event import EventDispatcher

class EditorBase(Screen, EventDispatcher):
    def __init__(self, manager, model_class, **kwargs):
        """
        manager: the singleton manager (e.g. CompanyManager, WrestlerManager)
        model_class: the class for new items (e.g. Company, Wrestler)
        """
        super().__init__(**kwargs)
        self.manager = manager
        self.model_class = model_class
        self.item = None
        self.current_index = None

    def load_item(self, item, index=None):
        """Populate fields with an existing item."""
        self.item = item
        self.current_index = index
        self.populate_fields(item)

    def new_item(self):
        """Clear fields for a new item."""
        self.item = self.model_class()
        self.current_index = self.manager.count()
        self.clear_fields()

    def save_item(self):
        """Save current item back to manager and persist."""
        self.update_item_from_fields(self.item)

        if self.item not in self.manager.get_all():
            self.manager.add(self.item)

        self.manager.save_all()
        return self.item

    # --- Hooks for subclasses ---
    def populate_fields(self, item):
        """Fill UI fields from item attributes."""
        raise NotImplementedError

    def clear_fields(self):
        """Reset UI fields to blank/default."""
        raise NotImplementedError

    def update_item_from_fields(self, item):
        """Write UI field values back into item."""
        raise NotImplementedError
