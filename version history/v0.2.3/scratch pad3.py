class LocationClass:
    def __init__(self, name, description, sublocations, objects, npcs):
        self.name = name
        self.description = description
        self.sublocations = sublocations
        self.objects = objects
        self.npcs = npcs

Averton = LocationClass(name= "Averton",
                        description= "A welcoming place for new adventurers.",
                        sublocations= ['Domarus', 'Tilsdale'],
                        objects= [],
                        npcs= ['OldMan', 'Villager'])


print(Averton.name)


