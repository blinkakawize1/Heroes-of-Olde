from dialogueM import *

class npc:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

#averton npcs instanced
OldMan= npc("Old Man", []) 
Villager = npc("Villager", TestDialogue)
