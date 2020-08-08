#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from board import *

def test_board():
    test_board = Board()
    assert test_board.board == {
   "A":{
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"
   },
   "B":{    
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"},
   "C":{    
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"},
   "D":{    
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"},
   "E":{    
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"},
   "F":{    
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"},
   "G":{   
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"},
   "H":{   
    "1":"*",
    "2":"*",
    "3":"*",
    "4":"*",
    "5":"*",
    "6":"*",
    "7":"*",
    "8":"*"}
}

def test_place_boat():
    test_board = Board()
    assert test_board.place_item("B","3","x", "🚢") == {'A': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'C': {'1': '*', '3': '🚢', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'B': {'1': '*', '3': '🚢', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'E': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'D': {'1': '*', '3': '🚢', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'G': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'F': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'H': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}}

def test_place_missile():
    test_board = Board()
    assert test_board.place_missile("B","3", "⭕") == {'A': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'C': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'B': {'1': '*', '3': '⭕', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'E': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'D': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'G': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'F': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}, 'H': {'1': '*', '3': '*', '2': '*', '5': '*', '4': '*', '7': '*', '6': '*', '8': '*'}}