# core/roster.py

class Wrestler:
    def __init__(
        self,
        name,
        alignment="neutral",
        keywords=None,
        stats=None,
        description="",
        catchphrase="",
        momentum=0,
        alignment_score=0.0,
        brand="",
        division="Mens",
        manager="",
        tag_team="",
        faction="",
        championships=None,
        accolades=None,
        wins=0,
        losses=0,
        draws=0,
        rank=0
    ):
        self.name = name
        self.alignment = alignment
        self.keywords = keywords or []
        self.stats = stats or {"power": 1, "technique": 1, "charisma": 1}
        self.description = description
        self.catchphrase = catchphrase
        self.momentum = momentum
        self.alignment_score = alignment_score

        self.brand = brand
        self.division = division
        self.manager = manager
        self.tag_team = tag_team
        self.faction = faction
        self.championships = championships or []
        self.accolades = accolades or []

        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.rank = rank

    def to_dict(self):
        return {
            "name": self.name,
            "alignment": self.alignment,
            "keywords": self.keywords,
            "stats": self.stats,
            "description": self.description,
            "catchphrase": self.catchphrase,
            "momentum": self.momentum,
            "alignment_score": self.alignment_score
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            alignment=data.get("alignment", "neutral"),
            keywords=data.get("keywords", []),
            stats=data.get("stats", {}),
            description=data.get("description", ""),
            catchphrase=data.get("catchphrase", ""),
            momentum=data.get("momentum", 0),
            alignment_score=data.get("alignment_score", 0.0)
        )
