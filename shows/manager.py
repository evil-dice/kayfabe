# shows/manager.py

import json
from pathlib import Path
from config.config import SAVEPATH
from shows.model import Show
from state.universe import Universe

class ShowManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._shows = []
            cls._instance._showslots = Universe().all_shows()
            cls._instance._currentslot = None
        return cls._instance
    
    def new(self, **kwargs):
        '''Creates a new show object in the first open slot.'''
        
        # Output to console
        return new_show

    def save(self, show):
        '''Writes the show details to disk as a JSON file.'''
        slot = Path(SAVEPATH) / str(show.saveslot)
        slot.mkdir(parents=True, exist_ok=True)
        with open(slot / "show.json", "w", encoding="utf-8") as f:
            json.dump(show.to_dict(), f, indent=4)

    def save_all(self):
        for show in self._shows:
            self.save(show.to_dict())

    # def load(self, slot):
    #     '''Loads a JSON file with company data to memory.'''
        

    #     company_datafile = Path(SAVEPATH) / str(slot) / "company.json"
    #     if company_datafile.exists():
    #         with open(company_datafile, "r", encoding="utf-8") as f:
    #             data = json.load(f)

    #             # Update Universe singleton
    #             Universe().company = Company.from_dict(data)

    #             print(f"{Universe().company.name} successfully loaded to Universe")
    #             return Universe().company

    # def load_all(self):
    #     pass

    # def list_slots(self):
    #     """Return lightweight metadata for all save slots."""
    #     root = Path(SAVEPATH)
    #     slots = []
    #     for folder in root.iterdir():
    #         if folder.is_dir() and (folder / "company.json").exists():
    #             with open(folder / "company.json", "r", encoding="utf-8") as f:
    #                 data = json.load(f)
    #                 slots.append({
    #                     "slot": int(folder.name),
    #                     "name": data.get("name"),
    #                     "alias": data.get("alias"),
    #                     "logo": data.get("logo"),
    #                 })
    #         else:
    #             # If no company.json, treat as empty slot
    #             slots.append({
    #                 "slot": int(folder.name),
    #                 "name": None,
    #                 "alias": None,
    #                 "logo": None,
    #             })
    #     return sorted(slots, key=lambda s: s["slot"])

    # def select(self, show):
    #     """Sets a company as the current one."""
    #     Universe().current_company = company
