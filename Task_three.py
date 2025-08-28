import random

# to display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print(" - " * 3)

# To check if someone has won
def check_winner(board, player):
    # Rows, columns, diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# To check if board is full
def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

# Player move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken!")
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1 and 9.")

# The computer move (strategic)
def computer_move(board):
    # First try to win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_winner(board, "O"):
                    return
                board[i][j] = " "

    # Then block player
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board, "X"):
                    board[i][j] = "O"
                    return
                board[i][j] = " "

    # Otherwise pick center → corner → edge
    if board[1][1] == " ":
        board[1][1] = "O"
        return
    for (i, j) in [(0,0), (0,2), (2,0), (2,2)]:
        if board[i][j] == " ":
            board[i][j] = "O"
            return
    for (i, j) in [(0,1), (1,0), (1,2), (2,1)]:
        if board[i][j] == " ":
            board[i][j] = "O"
            return

# Main game
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("1. Play with Computer")
    print("2. Play with Another Player")
    print("3. Quit game")
    choice = input("Enter your choice: ")

    board = [[" "]*3 for _ in range(3)]
    print_board(board)

    if choice == "1":
        # Player vs Computer
        while True:
            # Player move
            player_move(board, "X")
            print_board(board)
            if check_winner(board, "X"):
                print("Player X wins!")
                break
            if is_full(board):
                print("It's a tie!")
                break

            # Computer move
            print("Computer is thinking...")
            computer_move(board)
            print_board(board)
            if check_winner(board, "O"):
                print("Computer wins!")
                break
            if is_full(board):
                print("It's a tie!")
                break

    elif choice == "2":
        # Player vs Player
        current_player = "X"
        while True:
            player_move(board, current_player)
            print_board(board)
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            if is_full(board):
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"

    elif choice == "3":
        print("Quitting game...")
    else:
        print("Invalid choice!")

tic_tac_toe()
