
from board import *

class Player:

    def __init__(self, name="name"):
        self.board = Board()
        self.opponent_board = Board()
        self.boat_x_position = "A"
        self.boat_y_position = "1"
        self.boat_r_position = "x"
        self.x_col = ["A","B","C","D","E","F","G","H"]
        self.y_col = ["1","2","3","4","5","6","7","8"]
        self.name = name
        self.opponent_boat_location = ("A","1","x")
        self.missile_hits = 0
        
    def get_name(self):
        """
        Gets name of player

        Returns:
            String of Name of Player
        """  
        return self.name

    def move_boat_right(self):
        """
        Move player boat location right 1
        
        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """  
        #Catch for going over the edge
        if self.boat_x_position == "F" and self.boat_r_position == "x":
            self.boat_x_position = "A"
        else:
            xIndex = self.x_col.index(self.boat_x_position)
            self.boat_x_position = self.x_col[xIndex + 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def move_boat_left(self):
        """
        Move player boat location left 1
        
        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """  
        #Catch for going over the edge
        if self.boat_x_position == "A" and self.boat_r_position == "x":
            self.boat_x_position = "F"
        else:
            xIndex = self.x_col.index(self.boat_x_position)
            self.boat_x_position = self.x_col[xIndex - 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def move_boat_up(self):
        """
        Move player boat location up 1
        
        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """  
        #Catch for going over the edge
        if self.boat_y_position == "1" and self.boat_r_position == "y":
            self.boat_y_position = "7"
        yIndex = self.y_col.index(self.boat_y_position)
        self.boat_y_position = self.y_col[yIndex - 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def move_boat_down(self):
        """
        Move player boat location down 1
        
        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """  
        #Catch for going over the edge
        if self.boat_y_position == "6" and self.boat_r_position == "y":
            self.boat_y_position = "1"
        else:
            yIndex = self.y_col.index(self.boat_y_position)
            self.boat_y_position = self.y_col[yIndex + 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)
 
    def move_boat(self, move):
        """
        Takes user input and decides how to move boat

        Args:
            move: String of either W,A,S,D or R 

        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """  
        if move == "w":
            self.move_boat_up()
        if move == "a":
            self.move_boat_left()
        if move == "s":
            self.move_boat_down()
        if move == "d":
            self.move_boat_right()
        if move == "r":
            self.rotate_boat()
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def rotate_boat(self):
        """
        Rotate boat 90 degrees

        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """  
        #Move boat back if rotation will push it off the edge
        if ((self.boat_y_position == "7" ) and (self.boat_r_position == "x")):
            self.move_boat_up()
        if ((self.boat_y_position == "8" ) and (self.boat_r_position == "x")):
            self.move_boat_up()
            self.move_boat_up() 
        if ((self.boat_x_position == "G" ) and (self.boat_r_position == "y")):
            self.move_boat_left()
        if ((self.boat_x_position == "H" ) and (self.boat_r_position == "y")):
            self.move_boat_left()
            self.move_boat_left()
        #Perform rotation
        if self.boat_r_position == "y":
            self.boat_r_position = "x"
        else:
            self.boat_r_position = "y"
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def get_boat_location(self):
        """
        Gets the boats location

        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the boat 
        """  
        return  (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def get_board(self):
        """
        Gets the current board

        Returns:
            Dictionary of current board
        """  
        return  self.board.board


    def set_opponent_boat_location(self, location):
        """
        Gets name of player

        Args:
            location: Tuple of (x_location, y_location, rotation) of the location of the opponents boat 

        Returns:
            Tuple of (x_location, y_location, rotation) of the location of the opponents boat 
        """  
        self.opponent_boat_location = location
        self.opponent_board.place_item(location[0],location[1],location[2],"x")
        return  (self.opponent_boat_location)
   
    def fire_missile(self, x, y):
        opponent_spot = self.opponent_board.get_position(x,y)
        if opponent_spot == "x":
            self.board.place_missile(x,y,"🚢")
            self.missile_hits += 1
            return True
        else:
            self.board.place_missile(x,y,"⭕")
            return False
    
    def has_player_won(self):
        if (self.missile_hits >= 3):
            return True
        else:
            return False
        