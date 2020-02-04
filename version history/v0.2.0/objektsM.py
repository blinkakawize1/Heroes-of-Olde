class objekt:
    def __init__(self, name, descrip):
        self.name = name
        self.descrip = descrip

#objekt instanced
Barrel = objekt("Barrel", "A wooden barrel.")
Crate = objekt("Crate", "A wooden crate.")
OddTileOnTheWall = objekt("Odd tile on the wall", "This tile doesn't match the others.")
