from Player import *
from Locations import *
import os
import array

def main():
    
    intro()

    game()
    
    exit_console()

#handles the beginning of the game, prologue, character creation
def intro():
    
    inputContinue = input("Welcome to Fantasy World. Prepare yourself for adventure!\n\nType 'b' to begin.\n")
    #input validation
    while inputContinue != "b":
        inputContinue = input("\nInvalid choice. Type 'b' to begin.\n")
        if inputContinue == "b":
            break

    os.system('cls')

    Player.name = input("What is your name, chosen one?\n")

    os.system('cls')
    
    inputBegin = input(f"Hail, {Player.name}. Your journey awaits you.\n\nType 'v' to venture forth.\n")
    #input validation
    while inputBegin != "v":
        inputBegin = input("\nInvalid Choice. Type 'v' to venture forth.\n")
        if inputBegin == "v":
            break

    os.system('cls')

#just used for development to pause console so it doesn't close immediately
def exit_console():
    
    inputExit = input("\nExit console? y/n\n")
    #input validation
    while inputExit != "y":
        inputExit = input("\nInvalid choice. Exit console? y/n\n")
        if inputExit == "y":
            exit()
#sub-main loop
def game():
    
    Player.location = Averton

    options_list()
    
    


def options_list():
    
    Options = []
    #Prints the travel destinations available from player's
    #current location into a numbered list
    for index, element in enumerate(Player.location.canTravel, 1):
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
    
    userChoice = Player.location.canTravel[userInput - 1]
    
    print(f"\n{userChoice.name}")

    
main()
