
class Player:

    def __init__(self):
        self.boat_x_position = "A"
        self.boat_y_position = "1"
        self.boat_r_position = "x"
        self.x_col = ["A","B","C","D","E","F","G","H"]
        self.y_col = ["1","2","3","4","5","6","7","8"]
        
    def move_boat_right(self):
        xIndex = self.x_col.index(self.boat_x_position)
        self.boat_x_position = self.x_col[xIndex + 1]
        return (self.boat_x_position, self.boat_y_position)

    def move_boat_left(self):
        xIndex = self.x_col.index(self.boat_x_position)
        self.boat_x_position = self.x_col[xIndex - 1]
        return (self.boat_x_position, self.boat_y_position)

    def move_boat_up(self):
        yIndex = self.y_col.index(self.boat_y_position)
        self.boat_y_position = self.y_col[yIndex - 1]
        return (self.boat_x_position, self.boat_y_position)

    def move_boat_down(self):
        yIndex = self.y_col.index(self.boat_y_position)
        self.boat_y_position = self.y_col[yIndex + 1]
        return (self.boat_x_position, self.boat_y_position)
 
