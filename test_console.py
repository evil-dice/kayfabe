# test_console.py

# test company
from core.company import Company

def test_company_creation():
    print("Creating a new company...")
    c = Company(name="AEW", alias="All Elite Wrestling", owner="Tony Khan", saveslot=0)
    
    print("\nCompany object:")
    print(c)

    print("\nCompany as dictionary:")
    print(c.to_dict())

    print("\nReconstructing from dictionary...")
    data = c.to_dict()
    c2 = Company.from_dict(data)
    print(c2.to_dict())

if __name__ == "__main__":
    test_company_creation()