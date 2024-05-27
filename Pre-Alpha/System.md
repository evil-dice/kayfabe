# Kayfabe
In this application, the idea is to simulate Kayfabe, the in-universe Watsonian wrestling logic that powers wrestling show's storylines and events. This is done by using **Wrestlers**, who are used for roles in different **Angles**, which lead to **Matches** held on **Shows**. 

## Wrestlers
**Wrestlers** are the building blocks of a Show in Kayfabe. A Wrestler consists of these attributes, which are used to select them as groups by various functions in the came. 

* **Superstar Name** - Self-explantory

* **Brand** - The wrestler's current contracted show
* **Divison** - Mens or Womens
* **Traits** - Describes unique details about the wrestler's style or character. Traits are a comma-separated array.

* **Star Power** - This is how "over" a wrestler is. It is represented as a star rating, each point of star power equates to 1/4 star (so the scale is up to 20). The star rating of a wrestler determines their position on the card.
    * 1 Star or less = Jobber
    * 1-2 Stars = Low Card
    * 2-3 Stars = Mid Card
    * 3-4 Stars = Main Event
    * 4-5 Stars = Legend
* **Heat** - Heat is a measure of a wrestler's alignment. It is shown as a meter, from fully face (-10) to fully heel (+10), with a small tweener section in the middle. Some angles or segments will add or remove heat from a wrestler (leading hopefully to a natural turns).
* **In-Ring** - This is a star rating determining the wrestler's ability to go in the ring. It is used when simulating matches. 
* **Character** - A star rating of a wrestler's ability to be effective during non-wrestling segments. 

* **Manager** - Associated character as a manager.
* **TagTeam** - Lists their tag team, if any.
* **Faction** - Any factions the character is a member of.
* **Championship** - Any titles held by the character. 
* **Accolades** - Non-title Accolades (King of the Ring, Number 1 Contender, etc.)
* **Wins** - Self-explanatory
* **Losses** - Self-explanatory
* **Draws** - Self-explanatory
* **Rank** - The character's ranking based on their record

## Matches
Wrestlers are arranged into **Matches**. Each match is fought between a number of opposing **Sides**, each consisting of one or more Wrestlers selected as  **Participants**, and can be an element of Shows or Angles. 

Matches have the following properties:

* **Participants** - Numberof Wrestlers per Side
* **Sides** - Number of opponents in the match
* **Division** - There are four divisions which bind the participants of matches: Mens Single, Mens Tag, Womens Single, and Womens Tag. 
* **MatchType** - Matchtype is a data table that determines the match ruleset, number of sides, and participants per side. 
* **
* 


# Top Down Object Logic
A show is a collection of matches and segments.

A segment is an object containing different wrestlers and promos or other TV segment descriptions.

A match is an object that consists of wrestlers who are arranged into sides, stipulations, and results.

A side is one or more wrestlers sharing a goal in a given segment. Most commonly this is the people facing each other in matches.

# Mike's idea
The idea that came from talking to Mike was very simple. Randomized lists for different match elements, and you just click them and cycle through them. The elements will be very broad -- less "swerve cuts a promo from hangman's baby nursery" and more "The heel has made it personal by messing with family". This will allow you to just cycle through a few of them until it creates an interesting story. You can similarly cycle through match finishes or random events of different types. 

# UX Order of Operations
## Default mode, "Booker Mode" ( Match First, then Angle)
1. Number of participants is selected
    * Defines how many Wrestlers are in the match
2. Match Type is selected
    * A list of Matchtype options filtered based on the number of Participants
    * Defines the Sides of the match
    * Defines how many Participants are on each Side
    * A Ruleset can optionally added to the match (Hell in a Cell, Ladder, TLC, etc.)
3. Participants are chosen
    * Self-explanatory...Defines who is in the match
4. Optional: An Angle is generated. 
    * Angles are filtered to match Participants in the match (i.e., a match with no Heels would not ever generate an angle using a Heel, etc.)
    * You can also just type your own in for one-offs, allowing you to take a broad angle and make it more specific

# Match Type Details
One on One
Tag Team
Triple Threat
Fatal 4-Way
Five
Six


# MATCH Objects
A match is a dictionary with the following elements

* Type - the matchtype string
* Participants - an array where selected participants get copied to
* Sides - Sides determine which slots on the array are assigned to which team (i.e, 2 sides to a match with 4 participants will split the participants array every 2 elements)
* Stipulations - An array for the match's ruleset (Normal, Ladder, Elimination, etc)


# GUI Planning 
Elements of a "Universe":
* Federation name, acronym, and logo
* Personnel (Owner, GM, Commissioner, etc.)
* Shows (Name, image, logo, GM)
* Championships (Title, Stipulation if any, image)
* Events (collections of matches)
* Schedule - how often events occur

## Widget List
* Event
* Match
* Rankings
* 

## Different views within app
* **Initial Screen**
    * Continue: Resume current universe
    * New Universe: Start a new universe
    * Load Universe: Load a different universe
    * Edit Universe: Change your settings for the current universe
    * Delete Universe: Delete current universe
* **Universe Main Screen**
    * Summary Screen: Looks vaguely like a website
        * Current Champions
        * Rankings
        * Summaries of recent angles 
        * Previous Event: Shows results of previous event
        * Coming Up: Shows your next event. Can click to edit and book matches. 
* **"Creative Department" (Angle Editor)**
    * articipant slots
    



# Screens and Windows

## Main Screen Views
* Title Screen
* Company
* Roster
* Creative
* Booking
* Play Universe

## Pop Up Windows
* Save and Load Universe
* Edit Show
* Edit Event
* Edit Wrestler

