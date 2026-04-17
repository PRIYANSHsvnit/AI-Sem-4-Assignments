import random
n = 8

def h(board):
    x = 0
    for i in range(n):
        for j in range(i+1,n):
            if board[i] == board[j]:
                x += 1
            if abs(board[i] - board[j]) == abs(i-j):
                x += 1

    return x

def random_board():
    board = []
    for i in range(n):
        board.append(random.randint(0,n-1))
    return board

def get_neighbors(board):
    neighbors = []
    for i in range(n):
        for j in range(n):
            if board[i] != j:
                neighbor = list(board)
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def hill_climb(board):
    curr = board
    curr_h = h(curr)
    st = 0
    while True:
        neighbours = get_neighbors(curr)
        best_n = None
        best_h = curr_h
        for i in neighbours:
            h_i = h(i)
            if h_i < best_h:
                best_h = h_i
                best_n = i
        if best_n is None:
            return curr , curr_h, st , False
        curr = best_n
        curr_h = best_h
        st += 1
        if curr_h == 0:
            return curr , curr_h, st , True
        
def run():
    res = []
    count = 0
    for i in range(50):
        board = random_board()
        initial_h = h(board)

        final_board, final_h, steps, solved = hill_climb(board)

        if solved:
            count += 1

        res.append({
            "Initial_Board": board,
            "Final_Board": final_board,
            "Run": i + 1,
            "Initial h": initial_h,
            "Final h": final_h,
            "Steps": steps,
            "Status": "Solved" if solved else "Fail"
        })

    # Print results
    print("\nResults\n")
    for r in res:
        print(r)

    print("\nSummary = ")
    print("Total Runs = ", 50)
    print("Solved = ", count)
    print("Failed = ", 50 - count)
    print("Success Rate = ", (count / 50) * 100, "%")

if __name__ == "__main__":
    run()