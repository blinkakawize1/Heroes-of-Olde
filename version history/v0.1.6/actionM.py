import playerM
import os
import random

def player_status():
    print(f"""Current location: {playerM.Player.location.name}
Health: {playerM.Player.health}\n""")
    
def actions_menu():
    #a dictionary of actions
    #the for loop iterates each key in the dictionary
    #he last line runs the function of whichever action string the user chose
    
    actions = {"Explore": explore, "Travel": travel, "Examine": examine, "Talk": talk}
    availableActions = ["Explore", "Travel", "Examine", "Talk"]
    
    for index, element in enumerate(availableActions, 1):
        print(index, "\b.", element)

    try:
        userInput = int(input("\nWhich action? "))
    except ValueError:
        while True:
            try:
                userInput = int(input("\nInvalid choice. Which action? "))
                break
            except ValueError:
                pass

    while userInput - 1 not in range(len(availableActions)):
        try:
            userInput = int(input("\nInvalid choice. Which action? "))
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Which action? "))
                    break
                except ValueError:
                    pass
                
    actions[availableActions[userInput - 1]]()
    
def explore():
    print("\nThis feature is not finished yet.\n")
    actions_menu()

def travel():
    #makes a new line
    print()
    #Prints the travel destinations available from player's
    #current location into a numbered list
    
    for index, element in enumerate(playerM.Player.location.subloc, 1):
        print(index, "\b.", element.name)

    try:
        userInput = int(input("\nWhich location? "))
    #if user puts in a string, this catches the error and
    #returns input validation loop
    except ValueError:
        while True:
            try:
                userInput = int(input("\nInvalid choice. Which location? "))
                break
            except ValueError:
                pass
    #if user inputs a number not within range of the length
    #of the Options list it returns this input validation
    while userInput - 1 not in range(len(playerM.Player.location.subloc)):
        try:
            userInput = int(input("\nInvalid choice. Which location? "))
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Which location? "))
                    break
                except ValueError:
                    pass

    userChoice = playerM.Player.location.subloc[userInput - 1]
    playerM.Player.location = userChoice
    os.system('cls')
    player_status()
    print(f"You traveled to {userChoice.name}.\n")
    actions_menu()

def examine():
    #checks to see if there are any objects in current location
    if not playerM.Player.location.objekt:
        os.system('cls')
        player_status()
        print("There is nothing here.\n")
        actions_menu()
        
    else:
        #makes a new line
        print()
        #Prints the objekts available from player's
        #current location into a numbered list
        for index, element in enumerate(playerM.Player.location.objekt, 1):
            print(index, "\b.", element.name)

        try:
            userInput = int(input("\nExamine what? "))
        #if user puts in a string, this catches the error and
        #returns input validation loop
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Examine what? "))
                    break
                except ValueError:
                    pass
        #if user inputs a object not within range of the length
        #of the Options list it returns this input validation
        while userInput - 1 not in range(len(playerM.Player.location.objekt)):
            try:
                userInput = int(input("\nInvalid choice. Examine what? "))
            except ValueError:
                while True:
                    try:
                        userInput = int(input("\nInvalid choice. Examine what? "))
                        break
                    except ValueError:
                        pass
                    
        userChoice = playerM.Player.location.objekt[userInput - 1]
        os.system('cls')
        player_status()
        print(f"{userChoice.descrip}\n")
        actions_menu()
        
def talk():
    #checks to see if there are any objects in current location
    if not playerM.Player.location.npc:
        os.system('cls')
        player_status()
        print("There is no-one here.\n")
        actions_menu()
        
    else:
        #makes a new line
        print()
        #Prints the objekts available from player's
        #current location into a numbered list
        for index, element in enumerate(playerM.Player.location.npc, 1):
            print(index, "\b.", element.name)

        try:
            userInput = int(input("\nTalk to who? "))
        #if user puts in a string, this catches the error and
        #returns input validation loop
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Talk to who? "))
                    break
                except ValueError:
                    pass
        #if user inputs a object not within range of the length
        #of the Options list it returns this input validation
        while userInput - 1 not in range(len(playerM.Player.location.npc)):
            try:
                userInput = int(input("\nInvalid choice. Talk to who? "))
            except ValueError:
                while True:
                    try:
                        userInput = int(input("\nInvalid choice. Talk to who? "))
                        break
                    except ValueError:
                        pass
                    
        userChoice = playerM.Player.location.npc[userInput - 1]
        os.system('cls')
        player_status()
        npcGreet = random.choice(userChoice.greet)
        print(f"{npcGreet}\n")
        actions_menu()
