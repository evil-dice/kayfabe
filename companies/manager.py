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
    
    def first_available_slot():
        # Set the save slot
        root = Path(SAVEPATH)
        slots = sorted(int(p.name) for p in root.iterdir() if p.is_dir() and p.name.isdigit())
        for i, slot in enumerate(slots):
            if i != slot:
                saveslot = i
                return saveslot

    def new(self):
        '''Creates a new company object in the first open slot.'''
        
        # Generate new company
        new_company = Company()
        print(new_company)

        # add to list
        self._companies.append(new_company)

        # Save to disk
        self.save(new_company)

        # Set it as active
        Universe().company = new_company
        
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

                # Update Universe singleton
                Universe().company = Company.from_dict(data)

                print(f"{Universe().company.name} successfully loaded to Universe")
                return Universe().company

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
