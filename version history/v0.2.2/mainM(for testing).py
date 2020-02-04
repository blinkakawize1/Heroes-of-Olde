from dataM import *
import actionsM
import os
import array

def main():
    Player['location'] = 'Averton'
    game()
    exit_console()

def game():
    player_status()
    actionsM.actions_main()
    
def exit_console():
    inputExit = input("\nType 'x' to exit. ")
    while inputExit != "x":
        inputExit = input("Invalid choice. Type 'x' to exit. ")
    exit()
            
main()
