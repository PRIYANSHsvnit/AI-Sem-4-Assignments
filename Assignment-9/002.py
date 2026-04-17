import math
import time

board = [[" " for _ in range(3)] for _ in range(3)]

node_count = 0
pruned = 0

#  LIMIT PRINT DEPTH (VERY IMPORTANT)
PRINT_DEPTH = 2


def print_board(b, depth):
    for row in b:
        print("   " * depth + str(row))
    print()


def is_moves_left(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == " ":
                return True
    return False


def evaluate(b):

    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2] and b[row][0] != " ":
            return 1 if b[row][0] == "X" else -1

    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] and b[0][col] != " ":
            return 1 if b[0][col] == "X" else -1

    if b[0][0] == b[1][1] == b[2][2] and b[0][0] != " ":
        return 1 if b[0][0] == "X" else -1

    if b[0][2] == b[1][1] == b[2][0] and b[0][2] != " ":
        return 1 if b[0][2] == "X" else -1

    return 0


def alphabeta(b, depth, alpha, beta, is_max):
    global node_count, pruned
    node_count += 1

    # 🔹 Controlled Tree Visualization
    if depth <= PRINT_DEPTH:
        print(f"{'   '*depth}Depth {depth} | {'MAX' if is_max else 'MIN'}")
        print_board(b, depth)

    score = evaluate(b)

    if score != 0:
        return score

    if not is_moves_left(b):
        return 0

    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):

                if b[i][j] == " ":
                    b[i][j] = "X"

                    val = alphabeta(b, depth+1, alpha, beta, False)

                    b[i][j] = " "

                    best = max(best, val)
                    alpha = max(alpha, best)

                    if beta <= alpha:
                        pruned += 1
                        print(f"{'   '*depth} PRUNED at depth {depth}")
                        return best   # exit both loops

        return best

    else:
        best = math.inf

        for i in range(3):
            for j in range(3):

                if b[i][j] == " ":
                    b[i][j] = "O"

                    val = alphabeta(b, depth+1, alpha, beta, True)

                    b[i][j] = " "

                    best = min(best, val)
                    beta = min(beta, best)

                    if beta <= alpha:
                        pruned += 1
                        print(f"{'   '*depth} PRUNED at depth {depth}")
                        return best

        return best


def find_best_move(b):

    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):

            if b[i][j] == " ":
                b[i][j] = "X"

                move_val = alphabeta(b, 0, -math.inf, math.inf, False)

                b[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move


#  DRIVER
start = time.time()

best_move = find_best_move(board)

end = time.time()

print("\n===== RESULT =====")
print("Best Move:", best_move)
print("Nodes Explored:", node_count)
print("Pruned Branches:", pruned)
print("Time Taken:", end - start)