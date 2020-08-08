from board import *

class Game:
    def __init__(self):
        self.player1_board = Board()
        self.player2_board = Board()


    def render_board_with_boat(self, x, y, rotation):
        """
        Renders the board with the chosen boat location

        Args:
            x: x value of the boat origin. Should be of ["A","B","C","D","E","F","G","H"]
            y: y value of the boat origin. Should be of ["1","2","3","4","5","6","7","8"]
            rotation: rotation of boat. Should be of ["x", "y"]

        Returns:
            String ready to be printed to console
        """
        dummy_board = Board()
        dummy_board.place_boat(x, y, rotation)
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
        