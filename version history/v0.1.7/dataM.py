import random

'''some developer notes: in this module is data for all game objects,
first the classes are declared, then the objects are insantiated with empty arrays,
and then lastly the arrays are defined. (I had to define arrays seperately,
because I could not put a variable into an objekt array until it had first been created'''

class Location:
    def __init__(self, name, descrip, subloc, objekt, npc, nonaction):
        self.name = name
        self.descrip = descrip
        self.subloc = subloc
        self.objekt = objekt
        self.npc = npc
        self.nonaction = nonaction

class Objekt:
    def __init__(self, name, descrip):
        self.name = name
        self.descrip = descrip

class Npc:
    def __init__(self, name, greet):
        self.name = name
        self.greet = greet

#locations instanced
Averton = Location("Averton", "A welcoming place for new adventurers.", [], [], [], ['Examine'])
Domarus = Location("Domarus", "A lonely place.", [], [], [], ['Talk'])
Tilsdale = Location("Tilsdale", "A Traveler's hub.", [], [], [], ['Talk'])

#objekt instanced
Barrel = Objekt("Barrel", "A wooden barrel.")
Crate = Objekt("Crate", "A wooden crate.")
OddTileOnTheWall = Objekt("Odd tile on the wall", "This tile doesn't match the others.")

#npc greetings instanced and defined
AvertonPersonGreet = ["Ho thar.", "G'day."]

#averton npcs instanced
OldMan= Npc("Old Man", AvertonPersonGreet)
Villager = Npc("Villager", AvertonPersonGreet)

#location sublocs defined
Averton.subloc = [Domarus, Tilsdale]
Domarus.subloc = [Averton, Tilsdale]
Tilsdale.subloc = [Averton, Domarus]

#location npcs defined
Averton.npc = [OldMan, Villager]

#location objekts defined
Averton.objekt = [] #<- Instancing averton with an empty array did not register, so I have to define objekts attribute seperately
Domarus.objekt = [Barrel, Crate]
Tilsdale.objekt = [OddTileOnTheWall]

#objekts defined

#quest dialogue
SpiderNestNpcAsk = """Spiders are infesting our town. A scout spotted their nest nearby, but no one here
                        is brave enough to go and fight them."""

SpiderNestPcResponse1 = "What's wrong?"

SpiderNestNpcResponse1 = """Spiders are infesting our town. A scout spotted their nest nearby, but no one here
                            is brave enough to go and fight them."""

SpiderNestPcResponse2 = "Ok, I will help you."




                  
            


