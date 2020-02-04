import playerM
import os
import random

def actions_main():

    def actions():
        print()
        availableActions = ["Explore", "Travel", "Examine", "Talk"]
        availableActions = actions_populate()
        for index, element in enumerate(availableActions, 1):
                print(index, "\b.", element)
        userInput = input_validation(availableActions, "Do what? ")
        actionMap[availableActions[userInput]]()
        
    def explore():
        print("\nThis feature is not finished yet.")
        actions()

    def travel():
        print()
        for index, element in enumerate(playerM.Player.location.sublocs, 1):
            print(index, "\b.", element.name)
        userInput = input_validation(playerM.Player.location.sublocs, "Go where? ")
        playerM.Player.location = playerM.Player.location.sublocs[userInput]
        os.system('cls')
        playerM.player_status()
        print(f"You traveled to {playerM.Player.location.name}.")
        actions()
        
    def examine():
        print()
        for index, element in enumerate(playerM.Player.location.objekts, 1):
            print(index, "\b.", element.name)
        userInput = input_validation(playerM.Player.location.objekts, "Examine what? ")
        os.system('cls')
        playerM.player_status()
        print(f"{playerM.Player.location.objekts[userInput].descrip}")
        actions()
                            
    def talk():
        print()
        for index, element in enumerate(playerM.Player.location.npcs, 1):
            print(index, "\b.", element.name)
        userInput = input_validation(playerM.Player.location.npcs, "Talk to whom? ")
        os.system('cls')
        playerM.player_status()
        print(f"{random.choice(playerM.Player.location.npcs[userInput].greets)}")
        actions()

    def input_validation(actionList, actionString):
        print()
        userInput = input(actionString)
        while True:
            if userInput.isdigit() and 0 < int(userInput) <= len(actionList):
                return int(userInput) - 1
            userInput = input(f"\nInvalid choice. {actionString}")
    
    def actions_populate():
        availableActions = ["Explore", "Travel", "Examine", "Talk"]
        if not playerM.Player.location.sublocs:
            availableActions.remove("Travel")
        if not playerM.Player.location.objekts:
            availableActions.remove("Examine")
        if not playerM.Player.location.npcs:
            availableActions.remove("Talk")
        return availableActions

    actionMap = {"Explore": explore, "Travel": travel, "Examine": examine, "Talk": talk}
    actions()
