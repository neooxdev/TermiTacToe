from termitactoe.player import Player
from termitactoe.game import Game
from termitactoe.utils import get_move_input

def main():
    print("=== Welcome to TermiTacToe ===")
    p1_name = input("Enter name for Player 1 (X): ")
    p2_name = input("Enter name for Player 2 (O): ")
    player1 = Player(p1_name, "X")
    player2 = Player(p2_name, "O")

    game = Game(player1, player2)
    game.display_board()

    while not game.winner and not game.is_draw():
        current_player = game.players[game.current_player_index]
        row, col = get_move_input(current_player)
        if not game.make_move(row, col):
            print("That spot is already taken. Try again.")
        game.display_board()

    if game.winner:
        print(f"🎉 {game.winner.name} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()