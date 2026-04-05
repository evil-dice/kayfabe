from shows.model import Show
from shows.manager import ShowManager
from state.universe import Universe
import random

# Create multiple companies
shows = [
    {
        'name': "Dynamite",
        'gm': "Tony Khan",
        'alias': "Dynamite",
        'theme': "dynamite_theme.mp3",
        'duration': 120,
        'saveslot': 0,
        'logo': "assets/images/dynamite.png"
    },
    {
        'name': "Collision",
        'gm': "Tony Khan",
        'alias': "Collision",
        'theme': "collision_theme.mp3",
        'duration': 120,
        'saveslot': 0,
        'logo': "assets/images/collision.png"
    }
]


# Add them to the manager
MANAGER=ShowManager()
for show in shows:
    MANAGER.new(show['name'], show['alias'], show['logo'], show['gm'], show['saveslot'], show['theme'], show['duration'])
    print(show)

print("All shows generated.")


# Step 3: Load from disk
# MANAGER.load(0)

# print(f"Loaded {len(companies)} companies:")
# for c in companies:
#     print(f"- {c.name} ({c.alias}) owned by {c.owner} in slot {c.saveslot}")

# Step 4: Set it as current
# Universe().company = random.choice(companies)
# print(f"\nCurrent Selection is:")
# print(f"{Universe().company.name}")
# print(f"Alias: {Universe().company.alias}")
# print(f"Owner: {Universe().company.owner}")
# print(f"Slot:  {Universe().company.saveslot}")
# print(f"Logo:  {Universe().company.logo}")
