class player:
    def __init__(self, name, health, items, location, target):
        self.name = name
        self.health = health
        self.items = []
        self.location = location
        self.target = target

Player = player('default', 100, [], 'default', 'default')

def player_status():
    print(f"""Location: {Player.location.name}
Health: {Player.health}""")
    if Player.target != 'default':
        print(f"Target: {Player.target.name}")
