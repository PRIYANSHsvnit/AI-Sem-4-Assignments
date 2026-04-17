def backward_chaining(goal, rules, facts, visited=None):
    """
    goal: what we want to prove
    rules: list of (premises, conclusion)
    facts: known facts
    """

    if visited is None:
        visited = set()

    print(f"Trying to prove: {goal}")

    # If already a known fact
    if goal in facts:
        print(f"{goal} is a known fact")
        return True

    # Prevent loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that conclude goal
    for premises, conclusion in rules:
        if conclusion == goal:
            print(f"Checking rule: {premises} → {goal}")

            # Check all premises recursively
            if all(backward_chaining(p, rules, facts, visited) for p in premises):
                print(f"{goal} proven\n")
                return True

    return False


print("\nBackward Chaining = ")

rules2a = [
    ({"P"}, "Q"),   # P → Q
    ({"R"}, "Q"),   # R → Q
    ({"A"}, "P"),   # A → P
    ({"B"}, "R")    # B → R
]

facts2a = {"A", "B"}
goal2a = "Q"

print("Result = ", backward_chaining(goal2a, rules2a, facts2a))


print("\nBackward Chaining = ")

rules2b = [
    ({"A"}, "B"),        # A → B
    ({"B", "C"}, "D"),   # B ∧ C → D
    ({"E"}, "C")         # E → C
]

facts2b = {"A", "E"}
goal2b = "D"

print("Result = ", backward_chaining(goal2b, rules2b, facts2b))