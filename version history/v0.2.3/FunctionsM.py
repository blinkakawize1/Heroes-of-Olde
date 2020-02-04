from DataM import *
import os
import random

#main actions menu
def main_actions():
    actionMap = {'Explore': explore, 'Travel': travel, 'Examine': examine, 'Talk': talk}
    availableActions = ['Explore', 'Travel', 'Examine', 'Talk']
    availableActions = actions_populate()
    print()
    for index, element in enumerate(availableActions, 1):
            print(index, "\b.", element)
    userInput = input_validation(availableActions, "Do what? ")
    actionMap[availableActions[userInput]]()

def actions_populate():
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
    print(f"""Location: {DataMap[Player['Location']]['Name']}
Health: {Player['Health']}""")
    if Player['Target'] != '':
        print(f"Target: {DataMap[Player['Target']]['Name']}")

#actions
def explore():
    print("\nThis feature is not finished yet.")
    main_actions()

def travel():
    print()
    for index, element in enumerate(DataMap[Player['Location']]['Sub-locations'], 1):
        print(index, "\b.", DataMap[element]['Name'])
    userInput = input_validation(DataMap[Player['Location']]['Sub-locations'], "Go where? ")
    Player['Location'] = DataMap[Player['Location']]['Sub-locations'][userInput]
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
    print(f"\n{DataMap[DataMap[Player['Location']]['Objects'][userInput]]['Description']}")
    main_actions()
    
                        
def talk():
    print()
    for index, element in enumerate(DataMap[Player['Location']]['Npcs'], 1):
        print(index, "\b.", DataMap[element]['Name'])
    userInput = input_validation(DataMap[Player['Location']]['Npcs'], "Talk to whom? ")
    Player['Target'] = DataMap[Player['Location']]['Npcs'][userInput]
    os.system('cls')
    dialogue(DataMap[DataMap[Player['Target']]['Dialogue']])

#dialogue choices menu
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
        for key in curDialogue[cur][1][userInput]:
            element = DataMap.get(key)
            if isinstance(element, str):
                if element == 'Exit':
                    os.system('cls')
                    player_status()
                    print()
                    print(curDialogue[cur])
                    print()
                    inputExit = input("Type 'c' to continue. ")
                    while inputExit != "c":
                        inputExit = input("Invalid choice. Type 'c' to continue. ")
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
            return int(userInput) - 1
        userInput = input(f"Invalid choice. {actionString}")
