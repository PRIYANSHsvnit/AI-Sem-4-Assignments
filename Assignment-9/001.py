import math
import time
import copy

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]

# Performance counter
node_count = 0

# Print board
def print_board(b):
    for row in b:
        print(row)
    print()

# Check if moves left
def is_moves_left(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                return True
    return False

# Evaluate board
def evaluate(b):

    # Rows
    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2] and b[row][0] != " ":
            return 1 if b[row][0] == "X" else -1

    # Columns
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] and b[0][col] != " ":
            return 1 if b[0][col] == "X" else -1

    # Diagonals
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != " ":
        return 1 if b[0][0] == "X" else -1

    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != " ":
        return 1 if b[0][2] == "X" else -1

    return 0

# Minimax with tree visualization
def minimax(b, depth, is_max):

    global node_count
    node_count += 1

    score = evaluate(b)

    # Print tree (visualization)
    if depth <= 2:
        print("Depth:", depth)
        print_board(b)

    # Terminal states
    if score != 0:
        return score

    if not is_moves_left(b):
        return 0

    # Maximizer (X)
    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = "X"
                    best = max(best, minimax(b, depth+1, False))
                    b[i][j] = " "

        return best

    # Minimizer (O)
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if b[i][j] == " ":
                    b[i][j] = "O"
                    best = min(best, minimax(b, depth+1, True))
                    b[i][j] = " "

        return best

# Find best move
def find_best_move(b):

    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):

            if b[i][j] == " ":
                b[i][j] = "X"

                move_val = minimax(b, 0, False)

                b[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Run program
start = time.time()

best_move = find_best_move(board)

end = time.time()

print("Best Move:", best_move)
print("Nodes Explored:", node_count)
print("Time Taken:", end - start)