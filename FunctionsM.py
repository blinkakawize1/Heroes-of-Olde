from DataM import *
import os
import random

#game intro
def intro():
    '''print("Welcome to Fantasy World. Prepare yourself for adventure!")
    print()
    os.system('pause')
    os.system('cls')
    print("What is your name, chosen one? ")
    print()
    os.system('cls')
    print(f"Hail, {Player['Name']}. Your journey awaits you.")
    print()
    os.system('pause')
    os.system('cls')'''
    
#main actions menu
def main_actions():
    actionMap = {'Explore': explore,
                 'Travel': travel,
                 'Examine': examine,
                 'Talk': talk}
    availableActions = actions_filter()
    print()
    for index, element in enumerate(availableActions, 1):
            print(index, "\b.", element)
    userInput = input_validation(availableActions, "Do what? ")
    if userInput != 'other menu':
        return actionMap[userInput]()
    else:
        pass
    
def actions_filter():
    availableActions = ['Explore', 'Travel', 'Examine', 'Talk']
    if not DataMap[Player['Location']]['Explorable']:
        availableActions.remove('Explore')
    if not DataMap[Player['Location']]['Sub-locations']:
        availableActions.remove('Travel')
    if not DataMap[Player['Location']]['Objects']:
        availableActions.remove('Examine')
    if not DataMap[Player['Location']]['Npcs']:
        availableActions.remove('Talk')
    return availableActions

def player_status():
    if Player['Location'] != '':
        print(f"""Location: {DataMap[Player['Location']]['Name']}              (p)layer / (o)ptions
Health: {Player['Health']}""")
    if Player['Target'] != '':
        print(f"Target: {DataMap[Player['Target']]['Name']}")
        
#other menus
def inventory():
    for index, element in enumerate(Player['Inventory'], 1):
            print(index, "\b.", DataMap[element]['Name'])
    os.system('pause')

#main actions
def explore():
    print("\nThis feature is not finished yet.")
    main_actions()

def travel():
    print()
    for index, element in enumerate(DataMap[Player['Location']]['Sub-locations'], 1):
        print(index, "\b.", DataMap[element]['Name'])
    userInput = input_validation(DataMap[Player['Location']]['Sub-locations'], "Go where? ")
    Player['Location'] = userInput
    os.system('cls')
    player_status()
    print(f"\nYou traveled to {DataMap[Player['Location']]['Name']}.")
    main_actions()
    
def examine():
    print()
    for index, element in enumerate(DataMap[Player['Location']]['Objects'], 1):
        print(index, "\b.", DataMap[element]['Name'])
    userInput = input_validation(DataMap[Player['Location']]['Objects'], "Examine what? ")
    os.system('cls')
    player_status()
    print(f"\n{DataMap[userInput]['Description']}")
    main_actions()
                
def talk():
    print()
    for index, element in enumerate(DataMap[Player['Location']]['Npcs'], 1):
        print(index, "\b.", DataMap[element]['Name'])
    userInput = input_validation(DataMap[Player['Location']]['Npcs'], "Talk to whom? ")
    Player['Target'] = userInput
    os.system('cls')
    dialogue(DataMap[DataMap[Player['Target']]['Dialogue']])

#dialogue menu
def dialogue(curDialogue):
    cur = '1'
    announcements = []
    while cur != 'Exit':
        os.system('cls')
        player_status()
        print()
        if announcements:
            for element in announcements:
                print(element)
            print()
            announcements = []
        print(curDialogue[cur][0])
        print()
        for index, element in enumerate(curDialogue[cur][1], 1):
            print(index, "\b.", element[0])
        userInput = input_validation(curDialogue[cur][1], "Say what? ")
        if userInput != 'other menu':
            for key in userInput:
                element = DataMap.get(key)
                if isinstance(element, str):
                    if element == 'Exit':
                        os.system('cls')
                        player_status()
                        print()
                        print(curDialogue[cur])
                        print()
                        os.system('pause')
                        cur = 'Exit'
                    else:
                        announcements.append(element)
                if key.isdigit():
                    cur = key
                if isinstance(element, dict):
                    curDialogue = element
                    cur = '1'
    Player['Target'] = ''
    os.system('cls')
    player_status()
    main_actions()

#input validation
def input_validation(actionList, actionString):
    print()
    userInput = input(actionString)
    while True:
        if userInput.isdigit() and 0 < int(userInput) <= len(actionList):
            return actionList[int(userInput) - 1]
        elif userInput == 'p':
            player_info()
            return 'other menu'
        elif userInput == 'o':
            pass
        userInput = input(f"Invalid choice. {actionString}")

#player info / options
def player_info():
    os.system('cls')
    player_status()
    print()
    print(f"""Name: {Player['Name']}
Race: {Player['Race']}
Health: {Player['Health']}
Mana: {Player['Mana']}""")
    print()
    playerInfoMenu = ['Inventory', 'Quests']
    for index, element in enumerate(playerInfoMenu, 1):
        print(index, '\b.', element)
    userInput = input_validation(playerInfoMenu, "Which option? ")
    if userInput == playerInfoMenu[0]:
        os.system('cls')
        player_status()
        print()
        inventory()
