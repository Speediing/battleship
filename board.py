#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Board:
    def __init__(self):
        self.board = self.initialize_board()
        self.x_col = ["A","B","C","D","E","F","G","H"]
        self.y_col = ["1","2","3","4","5","6","7","8"]
    
    def initialize_board(self):
        """
        Initializes an empty board

        Returns:
            Dictionary to represent board state
        """
        board = {}
        for i in ["A","B","C","D","E","F","G","H"]:
            board[i] = {}
            for j in ["1","2","3","4","5","6","7","8"]:    
                board[i][j] = "*"
        return board

    def place_boat(self,x,y,rotation):
        """
        Places a boat on the board

        Args:
            x: x value of the boat origin. Should be of ["A","B","C","D","E","F","G","H"]
            y: y value of the boat origin. Should be of ["1","2","3","4","5","6","7","8"]
            rotation: rotation of boat. Should be of ["x", "y"]
        Returns:
            Dictionary to represent board state with boat
        """
        xIndex = self.x_col.index(x)
        yIndex = self.y_col.index(y)
        if rotation is "x":
            self.board[x][y] = "🚢"
            self.board[self.x_col[xIndex+1]][y] = "🚢"
            self.board[self.x_col[xIndex+2]][y] = "🚢"
        if rotation is "y":
            self.board[x][y] = "🚢"
            self.board[x][self.y_col[yIndex+1]] = "🚢"
            self.board[x][self.y_col[yIndex+2]] = "🚢"
        return self.board