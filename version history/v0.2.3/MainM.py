from DataM import *
from FunctionsM import *
import os
import array

def intro():
    '''inputContinue = input("Welcome to Fantasy World. Prepare yourself for adventure!\n\nType 'b' to begin. ")
    while inputContinue != "b":
        inputContinue = input("\nInvalid choice. Type 'b' to begin. ")
        if inputContinue == "b":
            break
    os.system('cls')
    Player['Name'] = input("What is your name, chosen one? ")
    os.system('cls')
    inputBegin = input(f"Hail, {Player['Name']}. Your journey awaits you.\n\nType 'v' to venture forth. ")
    while inputBegin != "v":
        inputBegin = input("\nInvalid Choice. Type 'v' to venture forth. ")
        if inputBegin == "v":
            break
    os.system('cls')'''
    Player['Location'] = 'Averton'
    
def main():
    intro()
    player_status()
    main_actions()
    exit_console()
    
def exit_console():
    inputExit = input("\nType 'x' to exit. ")
    while inputExit != "x":
        inputExit = input("Invalid choice. Type 'x' to exit. ")
    exit()
    
main()
