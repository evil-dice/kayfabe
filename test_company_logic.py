from companies.model import Company
from companies.manager import CompanyManager
from state.universe import Universe
import random

# Create multiple companies
companies = [
    {
        'name': "All Elite Wrestling",
        'owner': "Tony Khan",
        'alias': "AEW",
        'saveslot': 0,
        'logo': "assets/images/aew.png"
    },
    {
        'name': "World Wrestling Entertainment",
        'owner': "Triple H",
        'alias': "WWE",
        'saveslot': 1,
        'logo': "assets/images/wwe.png"
    },
    {
        'name': "Impact Wrestling",
        'owner': "Billy Corgan",
        'alias': "Impact!",
        'saveslot': 2,
        'logo': "assets/images/impact.png"
    }
]


# Add them to the manager
MANAGER=CompanyManager()
for company in companies:
    MANAGER.new(company['name'], company['alias'], company['logo'], company['owner'], company['saveslot'])
    print(company)

print("All companies saved.")


# Step 3: Load a random single one from disk
MANAGER.load(random.choice([0, 1, 2]))

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
