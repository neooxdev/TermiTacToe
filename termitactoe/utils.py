def get_move_input(player):
    while True:
        try:
            move = input(f"{player.name} ({player.symbol}), enter row and column (0-2) separated by space: ")
            row, col = map(int, move.strip().split())
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Enter two numbers separated by space.")