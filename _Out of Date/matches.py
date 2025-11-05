import csv

# Logic

# Classes
class Match:
    def __init__(self, title, sides, division, participants, rules, finish):
        self.title = title
        self.sides = sides
        self.division = division
        self.participants = participants
        self.rules = rules
        self.finish = finish

# TODO [Wrestler Selection List] Show a list of wrestlers to select from



# TODO Initialize an empty match
def init_match(sides,participantsperside):
    while sides > 0:
        side = []
        for 

# Global Variables
divisions = ['Men','Women']


def set_division(division):
    selected_division = []
    pass
    return selected_division

def add_participant():
    pass




# [Set_Division]
Division = 'Men'

# [Build Match Framework]
selected_matchtype = '1 on 1'

# WIP Build sides, with slots for each
for matchtype in MatchTypes:
    if matchtype['matchtype'] == selected_matchtype:
        match_details = matchtype.copy()
HowManySides = int(match_details['sides'])
HowManyParticipants = int(match_details['participants'])
SlotsPerSide = int(HowManyParticipants / HowManySides)
# WIP... Need to iterate for each side and construct slots. Each side becomes a List of Wrestler Names. 
Participants = list()
sideCounter = Sides
while sideCounter > 0:
    sideCounter = sideCounter - 1






Rules = ('Normal')




# [Init_Matchtypes] Pull in CSV of match type info
from csv import DictReader
MatchTypes = list()

def import_matchtypes():
    filename = "data\matchtypes.csv"
    if not MatchTypes:
        match_types = open(filename, 'r')
    reader = DictReader(match_types, delimiter=";")
    for match_type in reader:
        MatchTypes.append(match_type)
    return MatchTypes




# TODO [Build out a match logic] ...
def book_match():
    participants = ()
    participants_count = len(participants)
    for participant

# TODO [Create a new match]
def add_match(matchtype, division, participants, sides, stipulations, winconditions, finish):
    new_matchtype = Match(name, sides, division, participants, stipulations, winconditions, finish)
    new_matchtype = new_matchtype.__dict__
    MatchTypes.append(new_matchtype)


# Add a participant to a match
add_Participant():
    pass

available_matchtypes = []

# WIP [Filter for Participants]
def filter_matchtypes(participants):
    available_matchtypes = MatchTypes
    for type in MatchTypes:
        sides = int(row['sides'])
        slotsperside = int(row['slotsperside'])

        participants = sides * slotsperside
        available_matchtypes = [x for x in MatchTypes if sides in x['sides']()]
    return available_matchtypes




# []

# []

# []

# [Experimental Stuff] This is just to test ideas...
# [Roll Teams, Participants into one single var]
matchtype = "30"
sides = matchtype.split('v')
for side in sides:
    side = int(side)
    init_side(side)