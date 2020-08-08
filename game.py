from board import *

class Game:
    def __init__(self):
        self.player1_board = Board()
        self.player2_board = Board()

    def render_board(self, board):
        """
        Takes in a board and renders it to a string for the console

        I had to use ugly multiline strings to get the tests to work. 
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
        