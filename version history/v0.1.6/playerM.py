class player:
    def __init__(self, name, health, inventory, location):
        self.name = "default"
        self.health = health
        self.inventory = []
        self.location = None

Player = player("Player", 100, [], None)
