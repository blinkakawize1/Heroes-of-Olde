from objektsM import *
from npcsM import *

class location:
    def __init__(self, name, descrip, sublocs, objekts, npcs):
        self.name = name
        self.descrip = descrip
        self.sublocs = sublocs
        self.objekts = objekts
        self.npcs = npcs

#locations instanced
Averton = location("Averton", "A welcoming place for new adventurers.", [], [], [])
Domarus = location("Domarus", "A lonely place.", [], [], [])
Tilsdale = location("Tilsdale", "A Traveler's hub.", [], [], [])

#location sublocs defined
Averton.sublocs = [Domarus, Tilsdale]
Domarus.sublocs = [Averton, Tilsdale]
Tilsdale.sublocs = [Averton, Domarus]

#location objekts defined
Averton.objekts = [] #<- Instancing averton with an empty array did not register, so I have to define objekts attribute seperately
Domarus.objekts = [Barrel, Crate]
Tilsdale.objekts = [OddTileOnTheWall]

#location npcs defined
Averton.npcs = [OldMan, Villager]
