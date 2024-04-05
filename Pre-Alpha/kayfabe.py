import csv
import random

# Get Angles file, append into List of Dictionaries for processing
anglesFile = open('Angles copy.csv', 'r')
reader = csv.DictReader(anglesFile)
allAngles = list()
for dictionary in reader:
    allAngles.append(dictionary)

# Get Roster file, append into List of Dictionaries for processing
rosterFile = open('Roster.csv', 'r')
reader = csv.DictReader(rosterFile)
FullRoster = list()
for dictionary in reader:
    FullRoster.append(dictionary)

#CLASSES
class Participant:
  def __init__(self, name, side, slot):
    self.name = name
    self.side = side
    self.slot = slot

#SET SIDES AND ASSIGN PARTICIPANTS

# Set Division boundaries ... WORKS
# Boundary is default values for basic things if not otherwise specified when choosing a wrestler
Boundary = {'Division': "Mens", 'TagTeam': False}
def set_boundary(Division=None, TagTeam=None):
    if Division == None:
        Boundary['Division'] = random.choice(["Mens","Womens"])
    else:
        Boundary['Division'] = Division
    if TagTeam == None:
        Boundary['TagTeam'] = random.choice([True,False])
    else:
        Boundary['TagTeam'] = TagTeam




# Grab a unique angle ... works
angle = random.choice(allAngles)

# Get list of participants per side ... works
angle_sides = [int(x) for x in angle['SIDES'].split("v" or "+") if x.isdigit()]

# Define total number of cast ... works
angle_slots = sum(angle_sides)

# Iterate through role filters, creating list from each ... works but might not be needed
rolefilters = {}
count = 0
while count != angle_slots:
    count += 1
    filterslot = "ROLE"+str(count)
    rolefilters.update({filterslot: angle[filterslot]})

# Apply filters and fill in Role slots ... WIP
# Remember list comprehension formula: 
# new_list = [expression for member in iterable (if conditional)]
def get_character():
    # Apply boundaries for male/female with overrides
    filteredroster = [x for x in FullRoster 
                      if x['DIVISION'] == Boundary['Division']]
    
    #filter for character attributes ... working!!!
    filteredroster = [x for x in filteredroster if x['ALIGNMENT'] == Alignment
                      if x['KEYWORD1'] == 'Arrogant']


    filteredroster = [x for x in filteredroster
                      if x == any(filteredroster.values)]

    
    # TEST VAR ONLY
    for whatever in filteredroster:
        print(whatever['FULLNAME'])



# Assign Roles to Sides
for side in angle_sides:
    roles_to_assign = int(side)
    while roles_to_assign > 0:
        Wrestler(filter)


# Get count of participants
for side in angle_sides(
    currentside = int(side)
    while currentside > 0:
        
)



slot1 = Participant()



# Populate list of participants
for side in angle_sides:



# WRESTLERS


def Wrestler(Contract, Alignment, Role, Gender, TagTeam, Faction, Championship, Manager, Tags):
    #Set up roster duplicate for filtering...
    FilteredRoster = []

    

    #Copy characters who match filtered attributes to filtered copy of roster

    #
    for i in FullRoster:
        if (i['CONTRACT'] == Contract and
            i['ALIGNMENT'] == Alignment and
            i['ROLE'] == Role and
            i['GENDER'] == Gender and
            i['TAGTEAM'] == TagTeam and
            i['FACTION'] == Faction and
            i['CHAMPIONSHIP'] == (Championship) and
            i['MANAGER'] == Manager and
            i['TAGS'] == Tags):
                FilteredRoster.append(i)

    #Select one wrester name from what remains
    SelectedWrestler = random.choice(FilteredRoster)

    #Return their name
    return(SelectedWrestler['SUPERSTAR'])

### WOOO THIS WORKS!!!!!
#Test variables...
Alignment = 'Heel'
Role = 'MainEvent'
Sex = 'F'
FilteredRoster = []
for i in FullRoster:
    if (i['ALIGNMENT'] == Alignment and
        i['ROLE'] == Role and
        i['SEX'] == Sex):
            FilteredRoster.append(i)

    
##ANGLE

# Grab a unique angle
angle = random.choice(allAngles)

# Get list of participants per side
angle_sides = [int(x) for x in angle['SIDES'].split("v" or "+") if x.isdigit()]

# Populate list of participants
for side in angle_sides:
    
    side# = [ ]
angle_roles = []
while angle_sides[0] > 0:



for side in angle_sides:


# Get number of Sides in Angle
if angle['SIDE']
angle.count('Side')


# Set number of Sides
class Side():
    def __init__(name, Num_of_Participants):

# Display Angle title
print(angle['ANGLE'])



# Create class of Participants
class Participant():
   def __init__(name, side):
      self.name = name
      self.side = side

# Fill Roles for Angle
# 1. Get number of participants
Number_of_Roles = int(angle['PARTICIPANTS'])

# 2. Spawn Participants
while Number_of_Roles > 0:
    Role1 = Participant()

For 

# Grab up to 8 unique participants and put them in a List
while Number_of_Participants > 0:
    Participants = []
    Participants.append(random.choice(FullRoster))
    Number_of_Participants = Number_of_Participants - 1
else:
    for Participant in Participants:
        print(Participant['SUPERSTAR'])

# Show participants to verify


# Print Angle summary
print(angle['DESCRIPTION'])




## ANGLE PARTICIPANTS



##TEST CASES

# Wrestler Function

# Wrestler Function with Filters

# Wrestler Function for Tag Teams

# Angle Function





