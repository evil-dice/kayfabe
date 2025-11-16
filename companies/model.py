# core/company.py
# Company represents the meta data and save slot of a Universe. 

from pathlib import Path

class Company:
    def __init__(self, name="New Company", alias=None, logo="assets/images/genericcompany.png", owner="", saveslot=None):
        self.name = name
        self.alias = alias if alias else name
        self.logo = logo
        self.owner = owner
        self.saveslot = saveslot
        self.savepath = Path(f"savedata/{self.saveslot}") if saveslot is not None else None

    def to_dict(self):
        return {
            "name": self.name,
            "alias": self.alias,
            "logo": self.logo,
            "owner": self.owner,
            "saveslot": self.saveslot,
            "savepath": str(self.savepath) if self.savepath else None
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", "New Company"),
            alias=data.get("alias"),
            logo=data.get("logo", "assets/images/genericcompany.png"),
            owner=data.get("owner", ""),
            saveslot=data.get("saveslot")
        )
