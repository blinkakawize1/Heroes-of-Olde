'''some developer notes: in this module is data for all game objects,
first the classes are declared, then the objects are insantiated with empty arrays,
and then lastly the arrays are defined. (I had to define arrays seperately,
because I could not put a variable into an objekt array until it had first been created'''

class Location:
    def __init__(self, name, descript, subloc, objekt, npc):
        self.name = name
        self.descript = descript
        self.subloc = subloc
        self.object = objekt
        self.npc = npc

class Objekt:
    def __init__(self, name, descript):
        self.name = name
        self.descript = descript

class Npc:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
        
#locations instanced
Averton = Location("Averton", "A welcoming place for new adventurers.", [], [], [])
Domarus = Location("Domarus", "A lonely place.", [], [], [])
Tilsdale = Location("Tilsdale", "A Traveler's hub.", [], [], [])

#objekt instanced
Barrel = Objekt("Barrel", "A wooden barrel.")
Crate = Objekt("Crate", "A wooden crate.")
OddTileOnTheWall = Objekt("Odd tile on the wall", "This tile doesn't match the others.")

#averton npcs instanced
OldMan= Npc("Old Man", [])
Villager = Npc("Villager", [])

#npc greetings instanced and defined
AvertonManGreeting = ["Ho thar.", "G'day."]

#npcs defined
OldMan.greeting = AvertonManGreeting[0]
Villager.greeting = AvertonManGreeting[1]

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





                  
            


