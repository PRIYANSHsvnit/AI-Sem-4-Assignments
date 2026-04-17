from collections import deque
import copy

grid = [
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,0,8,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,0,7,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,2]
]

domains = {}
for r in range(9):
    for c in range(9):
        if grid[r][c] == 0:
            domains[(r, c)] = list(range(1, 10))
        else:
            domains[(r, c)] = [grid[r][c]]

def get_neighbors(cell):
    r, c = cell
    neighbors = set()

    # Row and Column
    for i in range(9):
        neighbors.add((r, i))
        neighbors.add((i, c))

    # 3x3 Box
    br, bc = 3 * (r // 3), 3 * (c // 3)
    for i in range(3):
        for j in range(3):
            neighbors.add((br + i, bc + j))

    neighbors.remove(cell)
    return neighbors

def constraint(x, y):
    return x != y

def revise(domains, xi, xj):
    revised = False
    for x in domains[xi][:]:
        # Check if x has support in xj
        if not any(constraint(x, y) for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised

def ac3(domains):
    queue = deque()

    # Generate all arcs (810+)
    for xi in domains:
        for xj in get_neighbors(xi):
            queue.append((xi, xj))

    removed_count = 0

    while queue:
        xi, xj = queue.popleft()

        before = len(domains[xi])

        if revise(domains, xi, xj):
            after = len(domains[xi])
            removed_count += (before - after)

            # Failure condition
            if len(domains[xi]) == 0:
                return False, removed_count

            # Add neighbors back
            for xk in get_neighbors(xi):
                if xk != xj:
                    queue.append((xk, xi))

    return True, removed_count

domains_copy = copy.deepcopy(domains)

result, removed = ac3(domains_copy)

print("Arc Consistent:", result)
print("Total Values Removed:", removed)

print("\nDomain Size Grid (after AC-3):")
for r in range(9):
    row = []
    for c in range(9):
        row.append(len(domains_copy[(r, c)]))
    print(row)

print("\nCells with single values (solved by AC-3):")
for r in range(9):
    for c in range(9):
        if len(domains_copy[(r, c)]) == 1:
            print(f"Cell ({r},{c}) = {domains_copy[(r, c)][0]}")