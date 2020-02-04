#locations
Averton = {'Name': "Averton",
           'Description': "A welcoming place for new adventurers.",
           'Explorable': False,
           'Sub-locations': ['Domarus', 'Tilsdale'],
           'Objects': [],
           'Npcs': ['Villager']}

Domarus = {'Name': "Domarus",
           'Description': "A lonely place.",
           'Explorable': False,
           'Sub-locations': ['Averton', 'Tilsdale'],
           'Objects': ['Barrel', 'Crate'],
           'Npcs': ['OldMan']}

Tilsdale = {'Name': "Tilsdale",
            'Description': "A traveler's hub.",
            'Explorable': False,
            'Sub-locations': ['Averton', 'Domarus'],
            'Objects': ['OddTile'],
            'Npcs': []}

#npcs
OldMan = {'Name': "Old man",
          'Dialogue': 'OldManDialogue'}

Villager = {'Name': "Villager",
            'Dialogue': 'VillagerDialogue'}

#objects
Barrel = {'Name': "Barrel",
          'Description': "A wooden barrel."}

Crate = {'Name': "Crate",
         'Description': "A wooden crate."}

OddTile = {'Name': "Odd tile on the wall",
           'Description': "This tile doesn't match the others."}

#player
Player = {'Name': '',
          'Race': '',
          'Health': 100,
          'Inventory': [],
          'Quests': [],
          'Location': '',
          'Target': '',

          'LeftHand': '',
          'RightHand': '',
          'Head': '',
          'Torso': '',
          'Legs': '',
          'Feet': '',
          'Hands': '',
          'LeftEar': '',
          'RightEar': '',
          'Neck': '',
          'LeftFinger': '',
          'RightFinger': '',
          'Extra': ''}

#dialogues
VillagerQuest = {'1': ["I heard there is something going on in the town nearby.",

                       [("What is it?", '2'),
                        ("I want to ask you something else.", 'VillagerDialogue')]],

                 '2': ["They are in need of help.",
                       
                       [("I will go and investigate.", 'AnnounceQuest', 'AnnounceItem', 'VillagerDialogue'),
                        ("I don't have time to help them.", 'VillagerDialogue')]]}



VillagerDialogue = {'1': ["What do you want to know?",
                          
                          [("What is your name?", '2'),
                           ("How do I leave this place?", '3'),
                           ("Why are you here?", '4'),
                           ("I will be going now.", '8', 'Exit'),
                           ("Have you heard any rumors lately?", 'VillagerQuest')]],

                    '2': ["My name is [name].",

                          [("That's a weird name.", '5'),
                           ("I want to ask you something else.", '1')]],
                    
                    '3': ["There is only one way to leave this place, and it's through that door.",

                          [("What's on the other side?", '7'),
                           ("I want to ask you something else.", '1')]],
                    
                    '4': ["I am here to help you leave this place.",

                          [("Awfully nice of you.", '1'),
                           ("What do you get out of it?", '6')]],
                    
                    '5': ["That's not very nice.",
                    
                          [("I want to ask you something else.", '1')]],
                    
                    '6': ["I do not get anything out of it. It is my purpose here, to help you.",
                    
                          [("I want to ask you something else.", '1')]],
                    
                    '7': ["You will have to find that out for yourself.",
                          
                          [("I want to ask you something else.", '1')]],

                    '8': "G'day to you."}



OldManDialogue = {'1': ["Huh? What? Did you say something?",
                      
                        [("How old are you?", '2'),
                         ("Can you tell me about this place?", '3'),
                         ("I will be going now.", '4', 'Exit')]],
                
                  '2': ["Oh, I am old. I've watched the trees here grow.",
                          
                        [("I want to ask you something else.", '1')]],

                  '3': ["""This place has been my home for decades. It's a common place; I wouldn't say it's bad, and I wouldn't say it's good either.""",
                          
                        [("I want to ask you something else.", '1')]],

                  '4': "Bye bye!"}
#datamap
DataMap = {#locations
           'Averton': Averton,
           'Domarus': Domarus,
           'Tilsdale': Tilsdale,
           
           #objects
           'Barrel': Barrel,
           'OddTile': OddTile,
           'Crate': Crate,

           #npcs
           'OldMan': OldMan,
           'Villager': Villager,

           #dialogues
           'VillagerDialogue': VillagerDialogue,
           'VillagerQuest': VillagerQuest,
           'OldManDialogue': OldManDialogue,
           'AnnounceQuest': "Obtained quest",
           'AnnounceItem': "Obtained item",
           'Exit': 'Exit'}
