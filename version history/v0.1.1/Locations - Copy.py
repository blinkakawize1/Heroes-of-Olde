from Items import *

class Location:
    def __init__(self, name, description, canTravel, items):
        self.name = name
        self.description = description
        self.canTravel = canTravel
        self.items = items


Averton = Location("Averton", "A welcoming place for new adventurers.", [], []) 

Domarus = Location("Domarus", "A lonely place.", [], [])

Tilsdale = Location("Tilsdale", "A Traveler's hub.", [], [])

Averton.canTravel = [Domarus, Tilsdale]
Averton.items = []

Domarus.canTravel = [Averton, Tilsdale]
Domarus.items = []
