from player import *

def test_move_boat_right():
    player = Player()
    assert player.move_boat_right() == "B"