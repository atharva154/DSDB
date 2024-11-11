# Constants representing the players
player, opponent = 'x', 'o'

# Function to check if there are moves left on the board
def isMovesLeft(board):
    for row in board:
        if '_' in row:
            return True
    return False

# Function to evaluate the board and return a score
def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            if row[0] == player:
                return 10
            elif row[0] == opponent:
                return -10
   
    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            if board[0][col] == player:
                return 10
            elif board[0][col] == opponent:
                return -10
   
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10
   
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10
   
    # If no one has won, return 0
    return 0

# Minimax function
def minimax(board, depth, isMax):
    score = evaluate(board)
   
    # If the player has won, return the score
    if score == 10:
        return score
   
    # If the opponent has won, return the score
    if score == -10:
        return score
   
    # If there are no more moves, it's a tie
    if not isMovesLeft(board):
        return 0
   
    # If it's the player's turn (maximizer)
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best
   
    # If it's the opponent's turn (minimizer)
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

# Function to find the best move for the player
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
   
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
   
    return bestMove

# Function to print the board
def printBoard(board):
    for row in board:
        print(' '.join(row))
    print()

# Driver code
if __name__ == "__main__":
    board = [
        ['x', 'o', 'x'],
        ['o', 'o', 'x'],
        ['_', '_', '_']
    ]
   
    print("Current Board:")
    printBoard(board)
   
    bestMove = findBestMove(board)
   
    print("The Optimal Move is:")
    print("ROW:", bestMove[0], "COL:", bestMove[1])