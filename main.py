import os
from game import *
def main():
    os.system('clear')
    player1_name = input('Enter player 1 name: ')
    player2_name = input('Enter player 2 name: ')
    game = Game()
    game.start_game(player1_name, player2_name)
    
main()