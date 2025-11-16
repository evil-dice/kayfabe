from companies.model import Company
from companies.manager import CompanyManager
from state.universe import Universe
import random

# Create multiple companies
companies = [
    Company(name="All Elite Wrestling", owner="Tony Khan", alias="AEW", saveslot=0, logo="assets/images/aew.png"),
    Company(name="World Wrestling Entertainment", owner="Triple H", alias="WWE", saveslot=1, logo="assets/images/wwe.png"),
    Company(name="Impact Wrestling", owner="Billy Corgan", alias="Impact!", saveslot=2, logo="assets/images/impact.png")
]

# Add them to the manager
# manager = CompanyManager()
for company in companies:
    CompanyManager().add(company)

# Save to disk
CompanyManager().save_all()

print("All companies saved.")


# Step 3: Reload from disk
CompanyManager().load_all()
companies = CompanyManager().get_all()

print(f"Loaded {len(companies)} companies:")
for c in companies:
    print(f"- {c.name} ({c.alias}) owned by {c.owner} in slot {c.saveslot}")

# Step 4: Assign to Universe
Universe().company = random.choice(companies)
print(f"\nCurrent Selection is:")
print(f"{Universe().company.name}")
print(f"Alias: {Universe().company.alias}")
print(f"Owner: {Universe().company.owner}")
print(f"Slot:  {Universe().company.saveslot}")
print(f"Logo:  {Universe().company.logo}")
