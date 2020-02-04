TestQuest = {

    '1': ["I heard there is something going on in the town nearby.",

          [("What is it?", '2'),
           ("I want to ask you something else.", 'TestDialogue')]],

    '2': ["They are in need of help.",

          [("I will go and investigate.", 'AnnounceQuest', 'AnnounceItem', 'TestDialogue'),
           ("I don't have time to help them.", 'TestDialogue')]]}

TestDialogue = {

    '1': ["What do you want to know?",
          
          [("What is your name?", '2'),
           ("How do I leave this place?", '3'),
           ("Why are you here?", '4'),
           ("I will be going now.", 'Exit'),
           ("Have you heard any rumors lately?", 'TestQuest')]],

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
          
          [("I want to ask you something else.", '1')]]}

DataDict = {
    #dialogues
    'TestDialogue': TestDialogue,
    'TestQuest': TestQuest,

    #announcements
    'AnnounceQuest': "Obtained quest",
    'AnnounceItem': "Obtained item",

    #exit
    'Exit': 'Exit'}

