import playerM
import dataM
import actionsM
import os
import array

def main():
    intro()
    game()
    exit_console()

def intro():
    inputContinue = input("Welcome to Fantasy World. Prepare yourself for adventure!\n\nType 'b' to begin. ")
    while inputContinue != "b":
        inputContinue = input("\nInvalid choice. Type 'b' to begin. ")
        if inputContinue == "b":
            break
    os.system('cls')
    playerM.Player.name = input("What is your name, chosen one? ")
    os.system('cls')
    inputBegin = input(f"Hail, {playerM.Player.name}. Your journey awaits you.\n\nType 'v' to venture forth. ")
    while inputBegin != "v":
        inputBegin = input("\nInvalid Choice. Type 'v' to venture forth. ")
        if inputBegin == "v":
            break
    os.system('cls')
    playerM.Player.location = dataM.Averton

def game():
    playerM.player_status()
    actionsM.actions_main()
    
def exit_console():
    inputExit = input("\nType 'x' to exit. ")
    while inputExit != "x":
        inputExit = input("\nInvalid choice. Type 'x' to exit. ")
        if inputExit == "x":
            exit()
            
main()
