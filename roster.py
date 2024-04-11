# Imports
import csv

# Global vars

# Classes
class Wrestler:
    def __init__(self, name, alignment, workrate, charisma, gimmick, traits):
        self.name = name
        #self.shortname = shortname
        #self.alias = alias
        self.alignment = alignment
        self.workrate = workrate
        self.charisma = charisma
        self.gimmick = gimmick
        self.traits = traits

# [Import Roster] Use CSV to populate Roster object with data
from csv import DictReader
FullRoster = list()

def import_roster():
    filename = "testroster.csv"
    roster = open(filename, 'r')
    reader = DictReader(roster, delimiter=";")
    for character in reader:
        FullRoster.append(character)
    return FullRoster

def view_roster():
    for character in FullRoster:
        print(character)

# [Add Wrestler] Add a wrestler to the roster
def add_wrestler(name, alignment, workrate, charisma, gimmick, traits):
    new_wrestler = Wrestler(name, alignment, workrate, charisma, gimmick, traits)
    new_wrestler = new_wrestler.__dict__
    FullRoster.append(new_wrestler)

# [Filter Roster] Group wrestlers by traits for randomized Angles and Matches
filtered_roster = []

def filter_roster(*traits):
    global filtered_roster
    filtered_roster = FullRoster
    for trait in traits:
        filtered_roster = [x for x in FullRoster if trait in x.values()]
    return filtered_roster

# [Delete Wrestler] Remove a wrestler from the roster
def delete_wrestler(name):
    for wrestler in FullRoster:
        if wrestler['name'] == name:
            FullRoster.remove(wrestler)
            break

# [Edit Wrestler] Edit the attributes of an existing wrestler
def edit_wrestler(name, **kwargs):
    # Load a dict variable of the original stats by name
    for wrestler in FullRoster:
        if wrestler['name'] == name:
            wrestler.update(kwargs)
    return filter_roster(name)

# [Set Tag Team] Set one or more wrestlers to be a part of a tag team
def set_tagteam(tagteam, *members):
    for member in members:
        edit_wrestler(member, tagteam=tagteam)
    return filter_roster(tagteam)

# [Set Faction] Set one or more wrestlers to be part of a faction
def set_faction(faction, *members):
    for member in members:
        edit_wrestler(member, faction=faction)
    return filter_roster(faction)

# [Set Manager] Add a manager to one or more wrestlers
def set_manager(manager, *clients):
    for client in clients:
        edit_wrestler(client, manager=manager)
    return filter_roster(client, manager)


# TEST CODE BELOW THIS LINE
import_roster() #works

add_wrestler('Bray Wyatt', 'Heel', 2, 3, 'Supernatural', 'Cult Leader') #works
add_wrestler('John Cena', 'Face', 2, 2, 'Heroic', 'Veteran') #works

edit_wrestler('John Cena', alignment='Face', workrate=3, charisma=1)

print(FullRoster)

view_roster()

delete_wrestler('Cody Rhodes')

filter_roster('Heel')

set_tagteam('Cody & Wyatt', 'Cody Rhodes', 'Bray Wyatt')

set_faction('The New Family', 'Cody Rhodes', 'Bray Wyatt', 'Dustin Rhodes')            

set_faction('', 'Cody Rhodes')

set_manager('Brandi Rhodes','Cody Rhodes')

print(FullRoster[0]['name'])








with open('testroster.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        roster.append(Wrestler(row[0], row[1]))





#Grab Roster file data
roster_database = pd.read_csv('Roster.csv')

roster = pd.DataFrame(data=roster_database)

print(roster_full['FULLNAME', 'ALIGNMENT'])