import random

'''some developer notes: in this module is data for all game objects,
first the classes are declared, then the objects are insantiated with empty arrays,
and then lastly the arrays are defined. (I had to define arrays seperately,
because I could not put a variable into an objekt array until it had first been created'''

class location:
    def __init__(self, name, descrip, sublocs, objekts, npcs, nonactions):
        self.name = name
        self.descrip = descrip
        self.sublocs = sublocs
        self.objekts = objekts
        self.npcs = npcs
        self.nonactions = nonactions

class objekt:
    def __init__(self, name, descrip):
        self.name = name
        self.descrip = descrip

class npc:
    def __init__(self, name, greets, quests):
        self.name = name
        self.greets = greets
        self.quests = quests

#locations instanced
Averton = location("Averton", "A welcoming place for new adventurers.", [], [], [], ['Examine'])
Domarus = location("Domarus", "A lonely place.", [], [], [], ['Talk'])
Tilsdale = location("Tilsdale", "A Traveler's hub.", [], [], [], ['Talk'])

#objekt instanced
Barrel = objekt("Barrel", "A wooden barrel.")
Crate = objekt("Crate", "A wooden crate.")
OddTileOnTheWall = objekt("Odd tile on the wall", "This tile doesn't match the others.")

#npc greetings instanced and defined
AvertonPersonGreets = ["Ho thar.", "G'day."]

#averton npcs instanced
OldMan= npc("Old Man", AvertonPersonGreets, [])
Villager = npc("Villager", AvertonPersonGreets, [])

#location sublocs defined
Averton.sublocs = [Domarus, Tilsdale]
Domarus.sublocs = [Averton, Tilsdale]
Tilsdale.sublocs = [Averton, Domarus]

#location npcs defined
Averton.npcs = [OldMan, Villager]

#location objekts defined
Averton.objekts = [] #<- Instancing averton with an empty array did not register, so I have to define objekts attribute seperately
Domarus.objekts = [Barrel, Crate]
Tilsdale.objekts = [OddTileOnTheWall]

#objekts defined

#quest dialogue
SpiderNestAsk = """Spiders are infesting our town. A scout spotted their nest nearby, but no one here
                        is brave enough to go and fight them."""

SpiderNestPcResponse1 = "What's wrong?"

SpiderNestNpcResponse1 = """Spiders are infesting our town. A scout spotted their nest nearby, but no one here
                            is brave enough to go and fight them."""

SpiderNestPcResponse2 = "Ok, I will help you."




                  
            


