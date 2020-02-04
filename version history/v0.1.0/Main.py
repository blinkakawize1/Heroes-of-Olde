from Player import *
from Locations import *
import os
import array

def main():
    
    intro()

    game()
    
    exit_console()


def intro():
    
    inputContinue = input("Welcome to Fantasy World. Prepare yourself for adventure!\n\nType 'c' to continue.\n")

    while inputContinue != "c":
        inputContinue = input("\nInvalid choice. Type 'c' to continue.\n")
        if inputContinue == "c":
            break

    os.system('cls')

    Player.name = input("What is your name, chosen one?\n")

    os.system('cls')
    
    inputBegin = input(f"Hail, {Player.name}. Your journey awaits you.\n\nType 'b' to begin.\n")

    while inputBegin != "b":
        inputBegin = input("\nInvalid Choice. Type 'b' to begin.\n")
        if inputBegin == "b":
            break

    os.system('cls')


def exit_console():
    
    inputExit = input("Exit console? y/n\n")
    
    while inputExit != "y":
        inputExit = input("\nInvalid choice. Exit console? y/n\n")
        if inputExit == "y":
            exit()

def game():
    
    Player.location = Averton

    options_list()
    
    


def options_list():
    
    Options = [1, 2, 3]
    
    for index, element in enumerate(Player.location.canTravel, 1):
        Options.append(element)
        print(index, "\b.", element.name)

    try:
        userInput = int(input("\nWhich item?\n"))
    except ValueError:
        while True:
            try:
                userInput = int(input("\nInvalid input. Which item?\n"))
                break
            except ValueError:
                pass

    userChoice = Player.location.canTravel[userInput - 1]
    
    print(f"\n{userChoice.name}")

    
main()
