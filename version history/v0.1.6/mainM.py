import playerM
import dataM
import actionM
import os
import array

def main():
    intro()
    game()
    exit_console()

#handles the beginning of the game, prologue, character creation
def intro():
    
    inputContinue = input("Welcome to Fantasy World. Prepare yourself for adventure!\n\nType 'b' to begin. ")
    #input validation
    while inputContinue != "b":
        inputContinue = input("\nInvalid choice. Type 'b' to begin. ")
        if inputContinue == "b":
            break

    os.system('cls')
    playerM.Player.name = input("What is your name, chosen one? ")
    os.system('cls')
    
    inputBegin = input(f"Hail, {playerM.Player.name}. Your journey awaits you.\n\nType 'v' to venture forth. ")
    #input validation
    while inputBegin != "v":
        inputBegin = input("\nInvalid Choice. Type 'v' to venture forth. ")
        if inputBegin == "v":
            break

    os.system('cls')
    playerM.Player.location = dataM.Averton

#just used for development to pause console so it doesn't close immediately
def exit_console():
    inputExit = input("\nType 'x' to exit. ")
    #input validation
    while inputExit != "x":
        inputExit = input("\nInvalid choice. Type 'x' to exit. ")
        if inputExit == "x":
            exit()
            
#sub-main loop
def game():
    actionM.player_status()
    actionM.actions_menu()

main()
