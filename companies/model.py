# core/company.py
# Company represents the meta data and save slot of a Universe. 
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.event import EventDispatcher
from pathlib import Path
from config.config import SAVEPATH

class Company(EventDispatcher):
    name = StringProperty("New Company")
    alias = StringProperty("")
    logo = StringProperty("assets/images/no_image.png")
    owner = StringProperty("")
    saveslot = StringProperty(None, allownone=True)
    savepath = StringProperty(None, allownone=True)

    def __init__(self, name="New Company", alias="",
                 logo="assets/images/no_image.png",
                 owner="", saveslot=None, **kwargs):
        super().__init__(**kwargs)

        # Initialize properties
        self.name = name
        self.alias = alias
        self.logo = logo
        self.owner = owner
        self.saveslot = str(saveslot) if saveslot is not None else ""
        self.savepath = f"{SAVEPATH}/{self.saveslot}" if saveslot is not None else ""
        self._path = Path(self.savepath) if self.savepath else None # private path used for file operations

    def __str__(self):
        return f"Company(name={self.name}, owner={self.owner}, logo={self.logo}, slot={self.saveslot})"

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


class _oldCompany:
    def __init__(self, name="New Company", alias=None, logo="assets/images/genericcompany.png", owner="", saveslot=None):
        self.name = name
        self.alias = alias if alias else name
        self.logo = logo
        self.owner = owner
        self.saveslot = saveslot
        self.savepath = Path(f"{SAVEPATH}/{self.saveslot}") if saveslot is not None else None
    
    def __str__(self):
        '''Return a clear string'''
        return f"Company(name={self.name}, owner={self.owner}, logo={self.logo}, slot={self.saveslot})"

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
