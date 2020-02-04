import playerM

def actions_menu():
    Actions = {1: "Explore", 2: "Travel", 3: "Look", 4: "Examine", 5: "Talk"}

    for key, value in Actions.items():
        print(key, "\b.", value)

    input()

    travel_menu()

def travel_menu():
    
    Options = []
    #Prints the travel destinations available from player's
    #current location into a numbered list
    for index, element in enumerate(playerM.Player.location.subloc, 1):
        Options.append(element)
        print(index, "\b.", element.name)

    try:
        userInput = int(input("\nWhich item?\n"))
    #if user puts in a string, this catches the error and
    #returns input validation loop
    except ValueError:
        while True:
            try:
                userInput = int(input("\nInvalid choice. Which item?\n"))
                break
            except ValueError:
                pass
    #if user inputs a number not within range of the length
    #of the Options list it returns this input validation
    while userInput - 1 not in range(len(Options)):
        try:
            userInput = int(input("\nInvalid choice. Which item?\n"))
        except ValueError:
            while True:
                try:
                    userInput = int(input("\nInvalid choice. Which item?\n"))
                    break
                except ValueError:
                    pass

    userChoice = playerM.Player.location.subloc[userInput - 1]

    print(f"You travel to {userChoice.name}.")
