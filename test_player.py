from player import *

def test_get_boat_location():
    player = Player()
    assert player.get_boat_location() == ("A", "1", "x")

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
    assert player.rotate_boat() == ("A", "1", "y")

def test_move_boat():
    player = Player()
    assert player.move_boat("s") == ("A", "2", "x")

def test_set_boat_location():
    player = Player()
    assert player.set_opponent_boat_location(("B", "5", "y")) ==  ("B", "5", "y")

def test_get_name():
    player = Player()
    assert player.get_name() == "name"

def test_get_board():
    player = Player()
    assert player.get_board() == {'A': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'C': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'B': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'E': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'D': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'G': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'F': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'H': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}}

def test_fire_missile_hit():
    player = Player()
    player.set_opponent_boat_location(("A","1","x"))
    assert player.fire_missile("A","1") == True

def test_fire_missile_false():
    player = Player()
    player.set_opponent_boat_location(("A","1","x"))
    assert player.fire_missile("E","1") == False

def test_has_player_won_false():
    player = Player()
    player.set_opponent_boat_location(("A","1","x"))
    assert player.has_player_won() == False

def test_has_player_won_true():
    player = Player()
    player.set_opponent_boat_location(("A","1","x"))
    player.fire_missile("A","1")
    player.fire_missile("B","1")
    player.fire_missile("C","1")
    assert player.has_player_won() == True