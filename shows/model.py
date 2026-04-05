# core/company.py
# Company represents the meta data and save slot of a Universe. 
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.event import EventDispatcher
from pathlib import Path
from config.config import SAVEPATH

class Show(EventDispatcher):
    name = StringProperty("New Show")
    alias = StringProperty("")
    logo = StringProperty("assets/images/genericshow1.png")
    theme = StringProperty(None, allownone=True)
    gm = ObjectProperty()
    duration = NumericProperty(120, min=30, max=180) # 60, 90, 120, 150, 180
    # titles
    # roster
    # staff
    # booking
    saveslot = StringProperty(None, allownone=True)
    savepath = StringProperty(None, allownone=True)

    def __init__(self, name="New Show", alias="",
                 logo="assets/images/genericshow1.png",
                 gm=None, duration=120, theme=None, saveslot=None, **kwargs):
        super().__init__(**kwargs)

        # Initialize properties
        self.name = name
        self.alias = alias
        self.logo = logo
        self.gm = gm
        self.duration = duration
        self.theme = theme
        self.saveslot = str(saveslot) if saveslot is not None else ""
        self.savepath = f"{SAVEPATH}/{self.saveslot}/shows" if saveslot is not None else ""
        self._path = Path(self.savepath) if self.savepath else None # private path used for file operations

    def __str__(self):
        return f"Show(name={self.name}, GM={self.gm}, logo={self.logo}, theme={self.theme}, duration={self.duration}, slot={self.saveslot})"

    def to_dict(self):
        return {
            "name": self.name,
            "alias": self.alias,
            "logo": self.logo,
            "gm": self.gm,
            "theme": self.theme,
            "duration": self.duration,
            "saveslot": self.saveslot,
            "savepath": str(self.savepath) if self.savepath else None
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", "New Show"),
            alias=data.get("alias"),
            logo=data.get("logo", "assets/images/genericshow2.png"),
            gm=data.get("gm", ""),
            theme=data.get("theme", ""),
            duration=data.get("duration", 120),
            saveslot=data.get("saveslot")
        )