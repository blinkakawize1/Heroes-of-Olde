import playerM
import os
import random

def actions_main():

    def actions():
        availableActions = ["Explore", "Travel", "Examine", "Talk"]
        
        if playerM.Player.location.nonactions:
            for element in playerM.Player.location.nonactions:
                availableActions.remove(element)
                
        for index, element in enumerate(availableActions, 1):
                print(index, "\b.", element)
                
        userInput = input_validation(availableActions, actionString[0])
        
        actionMap[availableActions[userInput - 1]]()
        
    def explore():
        print("\nThis feature is not finished yet.\n")
        actions()

    def travel():
        print()
        for index, element in enumerate(playerM.Player.location.sublocs, 1):
            print(index, "\b.", element.name)

        userInput = input_validation(playerM.Player.location.sublocs, actionString[1])
        
        userChoice = playerM.Player.location.sublocs[userInput - 1]
        playerM.Player.location = userChoice
        os.system('cls')
        playerM.player_status()
        print(f"You traveled to {userChoice.name}.\n")
        actions()

    def examine():
        print()
        for index, element in enumerate(playerM.Player.location.objekts, 1):
            print(index, "\b.", element.name)

        userInput = input_validation(playerM.Player.location.objekts, actionString[2])
        
        userChoice = playerM.Player.location.objekts[userInput - 1]
        os.system('cls')
        playerM.player_status()
        print(f"{userChoice.descrip}\n")
        actions()
                            
    def talk():
        print()
        for index, element in enumerate(playerM.Player.location.npcs, 1):
            print(index, "\b.", element.name)
            
        userInput = input_validation(playerM.Player.location.npcs, actionString[3])
        
        userChoice = playerM.Player.location.npcs[userInput - 1]
        os.system('cls')
        playerM.player_status()
        print(f"{random.choice(userChoice.greets)}\n")
        actions()

    def input_validation(actionList, actionString):
        try:
            userInput = int(input(f"\n{actionString} "))
        except ValueError:
            while True:
                try:
                    userInput = int(input(f"\nInvalid choice. {actionString} "))
                    break
                except ValueError:
                    pass
                
        while userInput - 1 not in range(len(actionList)):
            try:
                userInput = int(input(f"\nInvalid choice. {actionString} "))
            except ValueError:
                while True:
                    try:
                        userInput = int(input(f"\nInvalid choice. {actionString} "))
                        break
                    except ValueError:
                        pass
                    
        return userInput
    
    actionMap = {"Explore": explore, "Travel": travel, "Examine": examine, "Talk": talk}
    actionString = ["Do what?", "Go where?", "Examine what?", "Talk to whom?"]
    actions()
