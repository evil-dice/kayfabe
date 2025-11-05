# Imports
import csv
from csv import DictReader, DictWriter
import json

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

# [Load Roster] Use CSV to populate Roster object with data ... now with file select dialog!
import tkinter as TK


Wrestlers = {}
def import_roster(filename = "data\Testroster.csv"):
    ''' Imports a CSV file of Wrestlers to your Universe save slot files'''
    data = open(filename, 'r')
    input = DictReader(data, delimiter=";")
    for superstar in input:
        Name = superstar['name']
        #del superstar['name']
        Wrestlers[Name] = Wrestler(**superstar).__dict__

    with open('data\wrestlers.json', 'w') as f:
        json.dump(Wrestlers, f)
    return Wrestlers

def export_roster():
    pass

# FullRoster = list()
# def load_roster():
#     # filename = TK.filedialog.askopenfilename(
#     #     filetypes=(
#     #         ("CSV files", "*.csv"),
#     #         ("All Files", "*.*")
#     #     )
#     # )
#     filename = "data\Testroster.csv"
#     roster = open(filename, 'r')
#     reader = DictReader(roster, delimiter=";")
#     for character in reader:
#         FullRoster.append(character)
#     return FullRoster

def view_roster():
    for wrestler in Wrestlers:
        print(wrestler)

# [Add Wrestler] Add a wrestler to the roster
def add_wrestler(name, alignment, workrate, charisma, gimmick, traits):
    new_wrestler = Wrestler(name, alignment, workrate, charisma, gimmick, traits)
    new_wrestler = new_wrestler.__dict__
    FullRoster.append(new_wrestler)

# [Save Roster] Saves the current roster to roster.csv datafile
def save_roster():
    keys = FullRoster[0].keys()

    with open("data\roster.csv", 'w', newline='') as datafile:
        writer = DictWriter(datafile, fieldnames=keys, delimiter=';')
        writer.writeheader()
        writer.writerows(FullRoster)


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