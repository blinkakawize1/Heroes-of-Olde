from dataM import *
import os
import random

def actions_main():
    
    def actions():
        availableActions = ['Explore', 'Travel', 'Examine', 'Talk']
        availableActions = actions_populate()
        print()
        for index, element in enumerate(availableActions, 1):
                print(index, "\b.", element)
        userInput = input_validation(availableActions, "Do what? ")
        ActionMap[availableActions[userInput]]()
        
    def explore():
        print("\nThis feature is not finished yet.")
        actions()

    def travel():
        print()
        for index, element in enumerate(DataMap[Player['location']]['sub-locations'], 1):
            print(index, "\b.", DataMap[element]['name'])
        userInput = input_validation(DataMap[Player['location']]['sub-locations'], "Go where? ")
        Player['location'] = DataMap[Player['location']]['sub-locations'][userInput]
        os.system('cls')
        player_status()
        print(f"\nYou traveled to {DataMap[Player['location']]['name']}.")
        actions()
        
    def examine():
        print()
        for index, element in enumerate(DataMap[Player['location']]['objects'], 1):
            print(index, "\b.", DataMap[element]['name'])
        userInput = input_validation(DataMap[Player['location']]['objects'], "Examine what? ")
        os.system('cls')
        player_status()
        print(f"\n{DataMap[DataMap[Player['location']]['objects'][userInput]]['description']}")
        actions()
                            
    def talk():
        print()
        for index, element in enumerate(DataMap[Player['location']]['npcs'], 1):
            print(index, "\b.", DataMap[element]['name'])
        userInput = input_validation(DataMap[Player['location']]['npcs'], "Talk to whom? ")
        Player['target'] = DataMap[Player['location']]['npcs'][userInput]
        os.system('cls')
        dialogue(DataMap[DataMap[Player['target']]['dialogue']])
        
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
        Player['target'] = ''
        os.system('cls')
        player_status()
        actions()
        
    def input_validation(actionList, actionString):
        print()
        userInput = input(actionString)
        while True:
            if userInput.isdigit() and 0 < int(userInput) <= len(actionList):
                return int(userInput) - 1
            userInput = input(f"Invalid choice. {actionString}")
    
    def actions_populate():
        availableActions = ['Explore', 'Travel', 'Examine', 'Talk']
        if not DataMap[Player['location']]['explorable']:
            availableActions.remove('Explore')
        if not DataMap[Player['location']]['sub-locations']:
            availableActions.remove('Travel')
        if not DataMap[Player['location']]['objects']:
            availableActions.remove('Examine')
        if not DataMap[Player['location']]['npcs']:
            availableActions.remove('Talk')
        return availableActions
                
    ActionMap = {'Explore': explore, 'Travel': travel, 'Examine': examine, 'Talk': talk}
    actions()
