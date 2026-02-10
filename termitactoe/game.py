class Game:
    def __init__(self, player1, player2):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]
        self.current_player_index = 0
        self.winner = None

    def display_board(self):
        print()
        for i in range(3):
            row = " | ".join(self.board[i])
            print(" " + row)
            if i < 2:
                print("---+---+---")
        print()

    def make_move(self, row, col):
        if self.board[row][col] != " ":
            return False
        self.board[row][col] = self.players[self.current_player_index].symbol
        if self.check_winner(row, col):
            self.winner = self.players[self.current_player_index]
        self.current_player_index = 1 - self.current_player_index
        return True

    def check_winner(self, row, col):
        sym = self.board[row][col]
        # Check row
        if all(self.board[row][c] == sym for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == sym for r in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.board[i][i] == sym for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == sym for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[r][c] != " " for r in range(3) for c in range(3)) and self.winner is None