# companies/manager.py

import json
from pathlib import Path
from config.config import SAVEPATH
from companies.model import Company
from state.universe import Universe

class CompanyManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._companies = []
            cls._instance._current = None
        return cls._instance
    
    def new(self, name, alias, logo, owner, saveslot):
        '''Creates a new company object in the first open slot.'''

        # Set the save slot
        root = Path(SAVEPATH)
        slots = sorted(int(p.name) for p in root.iterdir() if p.is_dir() and p.name.isdigit())
        for i, slot in enumerate(slots):
            if i != slot:
                saveslot = i
        
        # Generate new company
        new_company = Company(name, alias, logo, owner, saveslot)

        # add to list
        self._companies.append(new_company)

        # Save to disk
        self.save(new_company)

        # Output to console
        return new_company

    def save(self, company):
        '''Writes the company details to disk as a JSON file.'''
        slot = Path(SAVEPATH) / str(company.saveslot)
        slot.mkdir(parents=True, exist_ok=True)
        with open(slot / "company.json", "w", encoding="utf-8") as f:
            json.dump(company.to_dict(), f, indent=4)

    def save_all(self):
        for company in self._companies:
            self.save(company.to_dict())

    def load(self, slot):
        '''Loads a JSON file with company data to memory.'''
        company_datafile = Path(SAVEPATH) / str(slot) / "company.json"
        if company_datafile.exists():
            with open(company_datafile, "r", encoding="utf-8") as f:
                data = json.load(f)
                company = Company.from_dict(data)
                self._companies.append(company)

                # Update Universe singleton
                # self.select(company)
                Universe().current_company = company

                print(f"{Universe().current_company.name} successfully loaded to Universe")
                return company

    def load_all(self):
        pass

    def list_slots(self):
        """Return lightweight metadata for all save slots."""
        root = Path(SAVEPATH)
        slots = []
        for folder in root.iterdir():
            if folder.is_dir() and (folder / "company.json").exists():
                with open(folder / "company.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    slots.append({
                        "slot": int(folder.name),
                        "name": data.get("name"),
                        "alias": data.get("alias"),
                        "logo": data.get("logo"),
                    })
            else:
                # If no company.json, treat as empty slot
                slots.append({
                    "slot": int(folder.name),
                    "name": None,
                    "alias": None,
                    "logo": None,
                })
        return sorted(slots, key=lambda s: s["slot"])

    def select(self, company):
        """Sets a company as the current one."""
        Universe().current_company = company


    # def select(self, index):
    #     if 0 <= index < len(self._companies):
    #         self._current = self._companies[index]
    #     else:
    #         self._current = None
    #     return self._current

# class CompanyManager:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance._companies = []
#         return cls._instance

#     def load_all(self, folder="savedata"):
#         '''
#         Clears company list and loads all JSON companies from application's installed folder. 
#         '''
#         self._companies = []
#         root = Path(folder)
#         for slot in root.glob("*"):
#             company_file = slot / "company.json"
#             if company_file.exists():
#                 with open(company_file, "r", encoding="utf-8") as f:
#                     data = json.load(f)
#                     company = Company.from_dict(data)
#                     self._companies.append(company)

#     def save_all(self, folder="savedata"):
#         '''
#         Saves each company to disk as JSOn files. 
#         '''
#         root = Path(folder)
#         for company in self._companies:
#             slot = root / str(company.saveslot)
#             slot.mkdir(parents=True, exist_ok=True)
#             with open(slot / "company.json", "w", encoding="utf-8") as f:
#                 json.dump(company.to_dict(), f, indent=4)

#     def get_all(self):
#         return self._companies

#     def add(self, company):
#         self._companies.append(company)

#     def delete(self, index):
#         if not self.is_new(index):
#             del self._companies[index]

#     def get_with_new_slot(self):
#         '''Returns all companies plus a sentinel for UI use.'''
#         return self._companies + [None]
    
#     def get(self, index):
#         '''Returns the company at a given index, or None if it's the new slot.'''
#         if index < len(self._companies):
#             return self._companies[index]
#         return None

#     def is_new(self, index):
#         '''Checks if the index refers to the “New Company” slot:'''
#         return index >= len(self._companies)

#     def count(self):
#         return len(self._companies)

