class Board:
    def __init__(self):
        self.board = self.initialize_board()
    
    def initialize_board(self):
        board = {}
        for i in ["A","B","C","D","E","F","G","H"]:
            board[i] = {}
            for j in ["1","2","3","4","5","6","7","8"]:    
                board[i][j] = "O"
        return board