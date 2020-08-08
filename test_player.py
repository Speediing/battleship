from player import *

def test_move_boat_right():
    player = Player()
    assert player.move_boat_right() == ("B", "1", "x")

def test_move_boat_left():
    player = Player()
    player.move_boat_right()
    assert player.move_boat_left() == ("A", "1", "x")

def test_move_boat_down():
    player = Player()
    assert player.move_boat_down() == ("A", "2", "x")

def test_move_boat_up():
    player = Player()
    player.move_boat_down()
    assert player.move_boat_up() == ("A", "1", "x")

def test_rotate_boat():
    player = Player()
    player.rotate_boat()
    assert player.rotate_boat() == ("A", "1", "y")