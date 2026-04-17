import random,math
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
        
def first_choice_hill_climb(board):
    curr = board
    curr_h = h(curr)
    steps = 0

    while True:
        neighbors = get_neighbors(curr)
        random.shuffle(neighbors)   # random order

        improved = False

        for nb in neighbors:
            if h(nb) < curr_h:
                curr = nb
                curr_h = h(nb)
                steps += 1
                improved = True
                break   # move immediately

        if not improved:
            return curr, curr_h, steps, False

        if curr_h == 0:
            return curr, curr_h, steps, True
        
def random_restart(max_restarts=1000):
    total_steps = 0
    restarts = 0

    while restarts < max_restarts:
        board = random_board()
        final_board, final_h, steps, solved = hill_climb(board)

        total_steps += steps
        restarts += 1

        print(f"Restart {restarts} → Final h = {final_h}")

        if solved:
            return final_board, final_h, total_steps, restarts

    return None, None, total_steps, restarts

def simulated_annealing(board):
    curr = board
    curr_h = h(curr)
    T = 100      # initial temperature
    cooling = 0.95
    steps = 0

    while T > 0.1:
        if curr_h == 0:
            return curr, curr_h, steps, True

        neighbors = get_neighbors(curr)
        next_state = random.choice(neighbors)
        next_h = h(next_state)

        delta = next_h - curr_h

        if delta < 0:
            curr = next_state
            curr_h = next_h
        else:
            prob = math.exp(-delta / T)
            if random.random() < prob:
                curr = next_state
                curr_h = next_h

        T *= cooling
        steps += 1

    return curr, curr_h, steps, False
        
def run(choice):

    if choice == 1:
        print("\nSteepest Hill Climbing\n")
        solved = 0
        total_steps = 0

        for i in range(50):
            board = random_board()
            final_board, final_h, steps, status = hill_climb(board)

            print(f"Run {i+1} → Steps = {steps}, Final h = {final_h}, Status = {'Solved' if status else 'Fail'}")

            total_steps += steps
            if status:
                solved += 1

        print("\nSolved =", solved)
        print("Failed =", 50 - solved)
        print("Average Steps =", total_steps / 50)
        print("Success Rate =", (solved/50)*100, "%")


    elif choice == 2:
        print("\nFirst Choice Hill Climbing\n")
        solved = 0
        total_steps = 0

        for i in range(50):
            board = random_board()
            final_board, final_h, steps, status = first_choice_hill_climb(board)

            print(f"Run {i+1} → Steps = {steps}, Final h = {final_h}, Status = {'Solved' if status else 'Fail'}")

            total_steps += steps
            if status:
                solved += 1

        print("\nSolved =", solved)
        print("Failed =", 50 - solved)
        print("Average Steps =", total_steps / 50)
        print("Success Rate =", (solved/50)*100, "%")


    elif choice == 3:
        print("\nRandom Restart\n")
        solution, final_h, total_steps, restarts = random_restart()
        if solution is not None:
            print("\nSolution Found!")
            print("Final h =", final_h)
            print("Restarts Needed =", restarts)
            print("Total Steps =", total_steps)
        else:
            print("No solution found within restart limit.")


    elif choice == 4:
        print("\nSimulated Annealing\n")
        solved = 0
        total_steps = 0

        for i in range(50):
            board = random_board()
            final_board, final_h, steps, status = simulated_annealing(board)

            print(f"Run {i+1} → Steps = {steps}, Final h = {final_h}, Status = {'Solved' if status else 'Fail'}")

            total_steps += steps
            if status:
                solved += 1

        print("\nSolved =", solved)
        print("Failed =", 50 - solved)
        print("Average Steps =", total_steps / 50)
        print("Success Rate =", (solved/50)*100, "%")

    else:
        print("Invalid Choice!")

if __name__ == "__main__":

    print("\nChoose Algorithm = ")
    print("1. Steepest Hill Climbing")
    print("2. First Choice Hill Climbing")
    print("3. Random Restart")
    print("4. Simulated Annealing")

    choice = int(input("Enter choice = "))

    if choice == 1:
        run(1)
    elif choice == 2:
        run(2)
    elif choice == 3:
        run(3)
    elif choice == 4:
        run(4)
    else:
        print("Invalid Choice!")

'''The steepest ascent and first choice hill climbing algorithms frequently get trapped in local minima, resulting in low success rates.
Random restart hill climbing overcomes this limitation by repeatedly starting from new random states, thereby significantly increasing the probability of reaching a solution.
Simulated annealing probabilistically accepts worse moves during early stages, allowing it to escape local minima without restarting.
Experimental results show that random restart and simulated annealing outperform basic hill climbing methods for the 8-Queens problem.
In summary, while steepest ascent and first choice hill climbing can be effective for simple problems, they often struggle with complex landscapes.
Random restart and simulated annealing provide robust strategies to navigate such landscapes, leading to higher success rates in finding solutions.
'''