
class Player:

    def __init__(self, name="name"):
        self.boat_x_position = "A"
        self.boat_y_position = "1"
        self.boat_r_position = "x"
        self.x_col = ["A","B","C","D","E","F","G","H"]
        self.y_col = ["1","2","3","4","5","6","7","8"]
        self.name = name
        self.opponent_boat_location = ("A","1","x")
        
    def move_boat_right(self):
        xIndex = self.x_col.index(self.boat_x_position)
        self.boat_x_position = self.x_col[xIndex + 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def move_boat_left(self):
        xIndex = self.x_col.index(self.boat_x_position)
        self.boat_x_position = self.x_col[xIndex - 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def move_boat_up(self):
        yIndex = self.y_col.index(self.boat_y_position)
        self.boat_y_position = self.y_col[yIndex - 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def move_boat_down(self):
        yIndex = self.y_col.index(self.boat_y_position)
        self.boat_y_position = self.y_col[yIndex + 1]
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)
 
    def move_boat(self, move):
        if move is "w":
            self.move_boat_up()
        if move is "a":
            self.move_boat_left()
        if move is "s":
            self.move_boat_down()
        if move is "d":
            self.move_boat_right()
        if move is "r":
            self.rotate_boat()
        if move is "e":
            print("Save Board for user")
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def rotate_boat(self):
        if self.boat_r_position is "y":
            self.boat_r_position = "x"
        else:
            self.boat_r_position = "y"
        return (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def get_boat_location(self):
        return  (self.boat_x_position, self.boat_y_position, self.boat_r_position)

    def set_opponent_boat_location(self, x, y, r):
        ...