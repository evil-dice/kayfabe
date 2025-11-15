# core/roster_importer.py

import csv
from models.wrestler import Wrestler
from core.roster_manager import RosterManager

def import_csv_to_roster(csv_path, save_folder):
    manager = RosterManager()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            name = row.get("name")
            alignment = row.get("alignment", "neutral")
            stats = {
                "workrate": int(row.get("workrate", 1)),
                "charisma": int(row.get("charisma", 1)),
                "technique": int(row.get("technique", 1))
            }
            keywords = [kw.strip() for kw in row.get("traits", "").split(",") if kw.strip()]
            gimmick = row.get("gimmick", "")
            description = row.get("description", "")
            catchphrase = row.get("catchphrase", "")

            wrestler = Wrestler(
                name=name,
                alignment=alignment,
                keywords=keywords,
                stats=stats,
                description=description,
                catchphrase=catchphrase
            )
            manager.add(wrestler)

    manager.save_to_folder(save_folder)
