# test_roster_import.py

from core.roster_importer import import_csv_to_roster
from core.roster_manager import RosterManager

csv_path = "data/Testroster.csv"
save_folder = "savedata/0/roster"

# Import from CSV and save as JSON files
import_csv_to_roster(csv_path, save_folder)

# Load roster from JSON files
manager = RosterManager()
manager.load_from_folder(save_folder)

# Print summary
print("Imported Wrestlers:")
for w in manager.get_all():
    print(f"- {w.name} ({w.alignment})")
    print(f"  Brand: {w.brand} | Division: {w.division}")
    print(f"  Keywords: {w.keywords}")
    print(f"  Stats: {w.stats}")
    print(f"  Titles: {w.championships}")
    print(f"  Accolades: {w.accolades}")
    print(f"  Record: {w.wins}-{w.losses}-{w.draws} | Rank: {w.rank}")
    print()
