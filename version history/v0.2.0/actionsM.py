import playerM
import os
import random

def actions_main():

    def actions():
        availableActions = ['Explore', 'Travel', 'Examine', 'Talk']
        availableActions = actions_populate()
        enumerate_actions(availableActions)
        userInput = input_validation(availableActions, "Do what? ")
        actionMap[availableActions[userInput]]()
        
    def explore():
        print("\nThis feature is not finished yet.")
        actions()

    def travel():
        enumerate_actions_options(playerM.Player.location.sublocs)
        userInput = input_validation(playerM.Player.location.sublocs, "Go where? ")
        playerM.Player.location = playerM.Player.location.sublocs[userInput]
        userChoice = playerM.Player.location.sublocs[userInput]
        os.system('cls')
        playerM.player_status()
        print(f"\nYou traveled to {userChoice.name}.")
        actions()
        
    def examine():
        enumerate_actions_options(playerM.Player.location.objekts)
        userInput = input_validation(playerM.Player.location.objekts, "Examine what? ")
        userChoice = playerM.Player.location.objekts[userInput]
        os.system('cls')
        playerM.player_status()
        print(f"\n{userChoice.descrip}")
        actions()
                            
    def talk():
        enumerate_actions_options(playerM.Player.location.npcs)
        userInput = input_validation(playerM.Player.location.npcs, "Talk to whom? ")
        userChoice = playerM.Player.location.npcs[userInput]
        os.system('cls')
        playerM.player_status()
        dialogue(userChoice.dialogue)

    def dialogue(curDialogue):
        cur = '1'
        while cur != "exit":
            os.system('cls')
            playerM.player_status()
            print()
            print(curDialogue[cur][0])
            enumerate_dialogue_options(curDialogue[cur][1])
            userInput = input_validation(curDialogue[cur][1], "Say what? ")
            if len(curDialogue[cur][1][userInput]) == 3:
                curDialogue[cur][1][userInput][2]()
            cur = curDialogue[cur][1][userInput][1]

    def input_validation(actionList, actionString):
        print()
        userInput = input(actionString)
        while True:
            if userInput.isdigit() and 0 < int(userInput) <= len(actionList):
                return int(userInput) - 1
            userInput = input(f"\nInvalid choice. {actionString}")
    
    def actions_populate():
        availableActions = ['Explore', 'Travel', 'Examine', 'Talk']
        if not playerM.Player.location.sublocs:
            availableActions.remove('Travel')
        if not playerM.Player.location.objekts:
            availableActions.remove('Examine')
        if not playerM.Player.location.npcs:
            availableActions.remove('Talk')
        return availableActions
    
    def enumerate_dialogue_options(optionsList):
        print()
        for index, element in enumerate(optionsList, 1):
                print(index, "\b.", element[0])
                
    def enumerate_actions(optionsList):
        print()
        for index, element in enumerate(optionsList, 1):
                print(index, "\b.", element)

    def enumerate_actions_options(optionsList):
        print()
        for index, element in enumerate(optionsList, 1):
                print(index, "\b.", element.name)

        
    actionMap = {'Explore': explore, 'Travel': travel, 'Examine': examine, 'Talk': talk}
    actions()
