from termitactoe.player import Player

def test_player_creation():
    p = Player("Alice", "X")
    assert p.name == "Alice"
    assert p.symbol == "X"
