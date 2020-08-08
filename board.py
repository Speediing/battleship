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

    def place_item(self,x,y,rotation,item):
        """
        Places a boat on the board

        Args:
            x: x value of the boat origin. Should be of ["A","B","C","D","E","F","G","H"]
            y: y value of the boat origin. Should be of ["1","2","3","4","5","6","7","8"]
            rotation: rotation of boat. Should be of ["x", "y"]
            item: value of what is to be put.
        Returns:
            Dictionary to represent board state with boat
        """
        xIndex = self.x_col.index(x)
        yIndex = self.y_col.index(y)
        if rotation == "x":
            self.board[x][y] = item
            self.board[self.x_col[xIndex+1]][y] = item
            self.board[self.x_col[xIndex+2]][y] = item
        if rotation == "y":
            self.board[x][y] = item
            self.board[x][self.y_col[yIndex+1]] = item
            self.board[x][self.y_col[yIndex+2]] = item
        return self.board

    def place_missile(self,x,y,item):
        """
        Places a boat on the board

        Args:
            x: x value of the missile. Should be of ["A","B","C","D","E","F","G","H"]
            y: y value of the missile. Should be of ["1","2","3","4","5","6","7","8"]
            item: value of what is to be put.
        Returns:
            Dictionary to represent board state with missiles
        """
        self.board[x][y] = item
        return self.board

    def get_position(self,x,y):
        return self.board[x][y]