class player:
    def __init__(self, name, health, items, location):
        self.name = "default"
        self.health = health
        self.items = []
        self.location = None

Player = player("Player", 100, [], None)

def player_status():
    print(f"""Current location: {Player.location.name}
Health: {Player.health}""")
