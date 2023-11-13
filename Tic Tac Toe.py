# Tic-Tac-Toe Game with Minimax and Alpha-Beta Pruning

# The board is represented as a list of strings where each index corresponds to a position on the board.
# 'X' represents the human player, 'O' represents the AI, and an empty string represents an empty space.
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Function to check for available moves
def empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == " "]

# Function to check if the game is over
def game_over(board):
    # Check for a win
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    # Check for a tie
    if " " not in board:
        return "Tie"
    return None

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if game_over(board) == "O":
        return 1
    if game_over(board) == "X":
        return -1
    if game_over(board) == "Tie":
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for move in empty_cells(board):
            board[move] = "O"
            eval = minimax(board, depth - 1, False, alpha, beta)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in empty_cells(board):
            board[move] = "X"
            eval = minimax(board, depth - 1, True, alpha, beta)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move for the AI using Minimax and Alpha-Beta Pruning
def best_move(board):
    best_move = -1
    best_eval = float("-inf")
    for move in empty_cells(board):
        board[move] = "O"
        eval = minimax(board, 9, False, float("-inf"), float("inf"))
        board[move] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Main game loop
while True:
    print_board(board)
    if " " not in board or game_over(board):
        result = game_over(board)
        if result == "Tie":
            print("It's a Tie!")
        elif result == "O":
            print("AI (O) wins!")
        elif result == "X":
            print("User (X) wins!")
        break

    try:
        user_move = int(input("Enter your move (0-8): "))
        if board[user_move] != " ":
            print("Invalid move. That cell is already taken.")
            continue
        board[user_move] = "X"
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 8.")
        continue

    ai_move = best_move(board)
    board[ai_move] = "O"
