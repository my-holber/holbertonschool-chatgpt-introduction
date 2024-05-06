#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0  # Track the number of moves
    while moves < 9:  # There can be at most 9 moves in a game
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        
        # Input validation
        if row not in range(3) or col not in range(3):
            print("Invalid input! Row and column should be between 0 and 2.")
            continue
        
        if board[row][col] == " ":
            board[row][col] = player
            moves += 1  # Increment moves after a valid move
            if check_winner(board):  # Check for a winner after at least 3 moves
                print_board(board)
                print("Player " + player + " wins!")
                return
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
