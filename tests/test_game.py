from termitactoe.player import Player
from termitactoe.game import Game

def test_win_row():
    p1 = Player("A", "X")
    p2 = Player("B", "O")
    g = Game(p1, p2)
    g.board = [["X","X","X"],
               [" ","O"," "],
               [" "," ","O"]]
    assert g.check_winner(0,0) == True

def test_draw():
    p1 = Player("A","X")
    p2 = Player("B","O")
    g = Game(p1,p2)
    g.board = [["X","O","X"],
               ["X","O","O"],
               ["O","X","X"]]
    assert g.is_draw() == True