# Imports
import pandas as pd
import csv

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

# [Add Wrestler] Add a wrestler to the roster
def add_wrestler(name, alignment, workrate, charisma, gimmick, traits):
    new_wrestler = Wrestler(name, alignment, workrate, charisma, gimmick, traits)
    new_wrestler = new_wrestler.__dict__
    FullRoster.append(new_wrestler)

# [Delete Wrestler] Remove a wrestler from the roster
def delete_wrestler(name):
    for character in FullRoster:
        if character['name'] == name:
            FullRoster.remove(character)
            break

# [Edit Wrestler] Edit the attributes of an existing wrestler
    pass


# TEST CODE
import_roster()
add_wrestler('Bray Wyatt', 'Heel', 2, 3, 'Supernatural', 'Cult Leader')
print(FullRoster)
for character in FullRoster:
    print(character)

delete_wrestler('Cody Rhodes')


print(FullRoster[0]['name'])








with open('testroster.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        roster.append(Wrestler(row[0], row[1]))





#Grab Roster file data
roster_database = pd.read_csv('Roster.csv')

roster = pd.DataFrame(data=roster_database)

print(roster_full['FULLNAME', 'ALIGNMENT'])