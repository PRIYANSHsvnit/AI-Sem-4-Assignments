from collections import deque

# Variables
variables = ["P1", "P2", "P3", "P4", "P5", "P6"]

# Domains
domains = {v: ["R1", "R2", "R3"][:] for v in variables}

# Constraints (neighbors)
constraints = {
    "P1": ["P2", "P3", "P6"],
    "P2": ["P1", "P3", "P4"],
    "P3": ["P1", "P2", "P5"],
    "P4": ["P2", "P6"],
    "P5": ["P3", "P6"],
    "P6": ["P1", "P4", "P5"]
}

# Constraint: not equal
def constraint(x, y):
    return x != y


def revise(domains, xi, xj):
    revised = False
    for x in domains[xi][:]:
        # Check if there is some y in xj that satisfies constraint
        if not any(constraint(x, y) for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised


def ac3(domains, constraints):
    queue = deque()

    # Initialize queue with all arcs
    for xi in constraints:
        for xj in constraints[xi]:
            queue.append((xi, xj))

    steps = 0

    while queue:
        xi, xj = queue.popleft()
        steps += 1

        print(f"Step {steps}: Checking arc ({xi}, {xj})")

        if revise(domains, xi, xj):
            print(f"  Domain revised: {xi} -> {domains[xi]}")

            if not domains[xi]:
                return False

            for xk in constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True


print("Initial Domains = ")
print(domains)

# Optional assignment: P1 = R1
domains["P1"] = ["R1"]

print("\nAfter assigning P1 = R1 => ")
print(domains)

result = ac3(domains, constraints)

print("\nFinal Domains = ")
print(domains)

print("\nArc Consistent = ", result)

''' “Assigning P1 = R1 reduces domains of its neighbors,
     but AC-3 does not lead to any domain wipeout;
     hence the CSP remains arc-consistent and solvable.”'''