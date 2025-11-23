def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def get_valid_input(prompt):
    """Safely get a valid row/column input."""
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1, 2):
                return value
            else:
                print("Invalid input — must be 0, 1, or 2.")
        except ValueError:
            print("Invalid input — please enter a NUMBER (0, 1, or 2).")


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        print(f"Player {player}'s turn:")
        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")

        if board[row][col] == " ":
            board[row][col] = player

            # If this move wins the game
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")


tic_tac_toe()

