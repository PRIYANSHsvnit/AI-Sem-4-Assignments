from queue import Queue

# Goal state
goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

# Moves: up, down, left, right
moves = [(-1,0), (1,0), (0,-1), (0,1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def bfs(start):
    queue = Queue()
    visited = set()

    queue.put((start, 0))
    visited.add(start)

    explored = 0

    while not queue.empty():
        state, depth = queue.get()
        explored += 1

        if state == goal:
            print("Goal found at depth:", depth)
            print("States explored:", explored)
            return

        x, y = find_blank(state)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                new_tuple = tuple(tuple(row) for row in new_state)

                if new_tuple not in visited:
                    visited.add(new_tuple)
                    queue.put((new_tuple, depth + 1))


start_state = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

bfs(start_state)