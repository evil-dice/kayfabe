# Kayfabe Logic System
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

#Angles