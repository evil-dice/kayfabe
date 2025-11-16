# core/roster_manager.py

import json
from pathlib import Path
from roster.model import Wrestler

class RosterManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._roster = []
        return cls._instance

    def load_from_folder(self, folder_path):
        self._roster = []
        folder = Path(folder_path)
        for file in folder.glob("*.json"):
            with open(file, "r") as f:
                data = json.load(f)
                wrestler = Wrestler.from_dict(data)
                self._roster.append(wrestler)

    def save_to_folder(self, folder_path):
        folder = Path(folder_path)
        folder.mkdir(parents=True, exist_ok=True)
        for wrestler in self._roster:
            file_path = folder / f"{wrestler.name.replace(' ', '_').lower()}.json"
            with open(file_path, "w") as f:
                json.dump(wrestler.to_dict(), f, indent=4)

    def add(self, wrestler: Wrestler):
        self._roster.append(wrestler)

    def get_all(self):
        return self._roster

    def filter_by_keywords(self, *keywords):
        return [w for w in self._roster if all(k in w.keywords for k in keywords)]
