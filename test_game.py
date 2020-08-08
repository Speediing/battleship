#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from game import *
from player import *
import io

def test_render_empty_game():
    test_game = Game()
    empty_board = {'A': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}, 'B': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}, 'C': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}, 'D': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}, 'E': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}, 'F': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}, 'G': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}, 'H': {'1': '*', '2': '*', '3': '*', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*'}}
    assert test_game.render_board(empty_board) == ('''
   |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
-
1      *       *       *       *       *       *       *       *   
-
            
-
2      *       *       *       *       *       *       *       *   
-
            
-
3      *       *       *       *       *       *       *       *   
-
            
-
4      *       *       *       *       *       *       *       *   
-
            
-
5      *       *       *       *       *       *       *       *   
-
            
-
6      *       *       *       *       *       *       *       *   
-
            
-
7      *       *       *       *       *       *       *       *   
-
            
-
8      *       *       *       *       *       *       *       *   
-
            
''')

def test_render_game_boat_x():
    test_game = Game()
    assert test_game.render_board_with_boat("A","1","x") == ('''
   |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
-
1      🚢       🚢       🚢       *       *       *       *       *   
-
            
-
2      *       *       *       *       *       *       *       *   
-
            
-
3      *       *       *       *       *       *       *       *   
-
            
-
4      *       *       *       *       *       *       *       *   
-
            
-
5      *       *       *       *       *       *       *       *   
-
            
-
6      *       *       *       *       *       *       *       *   
-
            
-
7      *       *       *       *       *       *       *       *   
-
            
-
8      *       *       *       *       *       *       *       *   
-
            
''')

def test_render_game_boat_y():
    test_game = Game()
    assert test_game.render_board_with_boat("A","1","y") == ('''
   |   A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |
-
1      🚢       *       *       *       *       *       *       *   
-
            
-
2      🚢       *       *       *       *       *       *       *   
-
            
-
3      🚢       *       *       *       *       *       *       *   
-
            
-
4      *       *       *       *       *       *       *       *   
-
            
-
5      *       *       *       *       *       *       *       *   
-
            
-
6      *       *       *       *       *       *       *       *   
-
            
-
7      *       *       *       *       *       *       *       *   
-
            
-
8      *       *       *       *       *       *       *       *   
-
            
''')

def test_validate_missile_input_true():
    test_game = Game()
    assert test_game.validate_missile_input("A1") == True


def test_validate_missile_input_false():
    test_game = Game()
    assert test_game.validate_missile_input("Bad") == False