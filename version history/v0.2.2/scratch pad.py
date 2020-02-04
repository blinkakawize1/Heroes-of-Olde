class CreatureClass:
    def __init__(self, details):
        self.details = details

    def __getitem__(self, key):
        return self.details[key]

    def __setitem__(self, key, value):
        self.details[key] = value

class NpcClass(CreatureClass):
    pass

class PlayerClass(CreatureClass):
      pass

PlayerData = {'name': "Player",
              'quests': ''}

OldManData = {'name': "Old man",
              'dialogue': 'OldManDialogue'}

OldMan = NpcClass(OldManData)
Player = PlayerClass(PlayerData)

Player['quests'] = 'that'

print(Player['quests'])


