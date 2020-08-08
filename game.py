from board import *
from player import *
import os

class Game:

    def start_game(self, player_1_name, player_2_name):
        """
        Starts a new Game and loops until either player has made a winning move

        Args:
            player_1_name: name of player 1
            player_2_name: name of player 2
            
        """
        player_1 = Player(player_1_name)
        player_2 = Player(player_2_name)
        player_1_boat_location = self.place_boat(player_1)
        player_2_boat_location = self.place_boat(player_2)
        player_1.set_opponent_boat_location(player_2_boat_location)
        player_2.set_opponent_boat_location(player_1_boat_location)
        while 1:
            if (self.take_turn(player_1)): break
            if (self.take_turn(player_2)): break

    def take_turn(self, player):
        """
        Player makes a move

        Args:
            player: player object who will take their turn

        Returns:
            Boolean of whether the user has made a winning move
        """
        os.system('clear')
        print(self.render_board(player.get_board() ))
        fire_spot = input(player.get_name()+ " it's time to pick a location to fire! Enter your location like: 'B5'\n\n")
        while 1:
            if self.validate_missile_input(fire_spot) == True:
                break
            else:
                fire_spot = input(player.get_name()+ " your location was incorrectly formatted! Enter your location like: 'B5'\n\n")
        result = player.fire_missile(fire_spot[0], fire_spot[1])
        os.system('clear')
        print(self.render_board(player.get_board()))
        if result:
            input("You hit their ship, nice job! Press enter to end your turn")
        else:
            input("You missed :( Press enter to end your turn")
        if player.has_player_won():
            print(player.get_name() + " has sunk the battle ship and won!")
            return True
        return False

    def place_boat(self, player):
        """
        Allows a player to pick the location of their boat

        Args:
            player: player object who will pick the location

        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """
        os.system('clear')
        print(player.get_name()+ " it's time to pick your ship's location! \nUse W to go up, \nS to go down, \nA to go left, \nD to go right, \nand R to rotate your ship 90 degrees. \nPress E when you have made your decision!\n\n")
        boat_location = player.get_boat_location()
        (x, y, r) = boat_location
        print(self.render_board_with_boat( x, y, r))
        while 1:
            move = input('')
            os.system('clear')
            print(player.get_name()+ " it's time to pick your ship's location! \nUse W to go up, \nS to go down, \nA to go left, \nD to go right, \nand R to rotate your ship 90 degrees. \nPress E when you have made your decision!\n\n")
            boat_location = player.move_boat(move)
            (x, y, r) = boat_location
            print(self.render_board_with_boat( x, y, r))
            if move == "e":
                break
        return player.get_boat_location()

    def render_board_with_boat(self, x, y, rotation):
        """
        Renders the board with the chosen boat location when starting the game

        Args:
            x: x value of the boat origin. Should be of ["A","B","C","D","E","F","G","H"]
            y: y value of the boat origin. Should be of ["1","2","3","4","5","6","7","8"]
            rotation: rotation of boat. Should be of ["x", "y"]

        Returns:
            String ready to be printed to console
        """
        dummy_board = Board()
        dummy_board.place_item(x, y, rotation, "🚢")
        return self.render_board(dummy_board.board)

    def render_board(self, board):
        """
        Takes in a board and renders it to a string for the console

        I had to use ugly multiline strings to get the tests to work here. 
        TODO Refactor to use single line string and escape characters

        Args:
            board: board object to be rendered

        Returns:
            String ready to be printed to console
        """

        board_string = '''
   |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
'''
        for i in ["1","2","3","4","5","6","7","8"]:  
            board_string += '''-
''' 
            board_string += i
            board_string += "  "
            for j in ["A","B","C","D","E","F","G","H"]:
                board_string += "    "
                board_string += board[j][i]
                board_string += "   "
            board_string += '''
-
            
'''
        return board_string

    def validate_missile_input(self, input):
        if(input[0] in ["A","B","C","D","E","F","G","H"] and input[1] in ["1","2","3","4","5","6","7","8"]):
            return True
        else:
            return False