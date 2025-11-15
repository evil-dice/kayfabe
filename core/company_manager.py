# core/company_manager.py

import json
from pathlib import Path
from core.company import Company

class CompanyManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._companies = []
        return cls._instance

    def load_all(self, folder="savedata"):
        self._companies = []
        root = Path(folder)
        for slot in root.glob("*"):
            company_file = slot / "company.json"
            if company_file.exists():
                with open(company_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    company = Company.from_dict(data)
                    self._companies.append(company)

    def save_all(self, folder="savedata"):
        root = Path(folder)
        for company in self._companies:
            slot = root / str(company.saveslot)
            slot.mkdir(parents=True, exist_ok=True)
            with open(slot / "company.json", "w", encoding="utf-8") as f:
                json.dump(company.to_dict(), f, indent=4)

    def get_all(self):
        return self._companies

    def add(self, company):
        self._companies.append(company)

    def delete(self, index):
        if not self.is_new(index):
            del self._companies[index]

    def get_with_new_slot(self):
        '''Returns all companies plus a sentinel for UI use.'''
        return self._companies + [None]
    
    def get(self, index):
        '''Returns the company at a given index, or None if it's the new slot.'''
        if index < len(self._companies):
            return self._companies[index]
        return None

    def is_new(self, index):
        '''Checks if the index refers to the “New Company” slot:'''
        return index >= len(self._companies)

    def count(self):
        return len(self._companies)

