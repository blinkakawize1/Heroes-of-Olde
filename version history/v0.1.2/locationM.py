class Location:
    def __init__(self, name, description, subloc, items, npcs):
        self.name = name
        self.description = description
        self.subloc = subloc
        self.items = items
        self.npcs = npcs

  
Averton = Location("Averton", "A welcoming place for new adventurers.", [], [], []) 

Domarus = Location("Domarus", "A lonely place.", [], [], [])

Tilsdale = Location("Tilsdale", "A Traveler's hub.", [], [], [])

Averton.subloc = [Domarus, Tilsdale]

Domarus.subloc = [Averton, Tilsdale]

Tilsdale.subloc = [Averton, Domarus]
