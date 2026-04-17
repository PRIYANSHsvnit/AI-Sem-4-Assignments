def is_goal(state):
    return state[1] == 'C' and state[2] == 'C'

def suck(state):
    loc, A, B = state
    outcomes = []

    if loc == 'A':
        if A == 'D':
            outcomes = [('A', 'C', B), ('A', 'C', 'C')]
        else:
            outcomes = [('A', 'D', B)]

    elif loc == 'B':
        if B == 'D':
            outcomes = [(loc, A, 'C'), (loc, 'C', 'C')]
        else:
            outcomes = [(loc, A, 'D')]

    return outcomes


def move(state, direction):
    loc, A, B = state
    if direction == 'LEFT':
        return ('A', A, B)
    return ('B', A, B)


def and_or_search(state, path=[]):
    print(f"\nExploring State: {state}")

    if is_goal(state):
        print("-> Goal reached (both tiles clean)")
        return []

    if state in path:
        print("-> Loop detected, backtracking")
        return None

    path = path + [state]

    for action in ['SUCK', 'LEFT', 'RIGHT']:
        print(f"\nTrying Action: {action}")

        if action == 'SUCK':
            results = suck(state)
            print("-> SUCK results (AND node, all must succeed) = ", results)
        else:
            results = [move(state, action)]
            print("-> Move result = ", results)

        plans = []
        success = True

        for res in results:
            print(f"   Processing outcome = {res}")
            plan = and_or_search(res, path)

            if plan is None:
                print("   -> This branch failed")
                success = False
                break

            plans.append(plan)

        if success:
            print(f"-> Action {action} succeeds for ALL outcomes")
            return [action, plans]

    print("-> No valid plan from this state")
    return None


initial_state = ('A', 'D', 'D')

print("And Or Tree = \n")
plan = and_or_search(initial_state)

print("Final = \n")
print("Final Plan:", plan)

print("")

print("1. Tree Construction = ")
print("-> Each state is expanded using possible actions.")
print("-> SUCK creates multiple outcomes → AND node.")
print("-> MOVE creates single outcome → OR node.\n")

print("2. Calculation Logic = ")
print("-> For each action, all possible results are generated.")
print("-> Each result is recursively checked.")
print("-> If ALL outcomes reach goal → action is valid.\n")

print("3. Plan Formation = ")
print("-> First action that works for all outcomes is selected.")
print("-> This creates a conditional plan (AND-OR tree).\n")

print("4. Final Result Meaning = ")
print("-> Plan guarantees cleaning both tiles despite uncertainty.")