def forward_chaining(rules, facts, goal):
    """
    rules: list of tuples (premises, conclusion)
           premises = set of symbols
    facts: set of known true symbols
    goal: symbol to prove
    """

    inferred = set()  # symbols we already processed

    while True:
        added = False

        for premises, conclusion in rules:
            # If all premises are true AND conclusion not yet inferred
            if premises.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                added = True
                print(f"Inferred: {conclusion} using {premises} → {conclusion}")

                if conclusion == goal:
                    print("\nGoal reached!\n")
                    return True

        if not added:
            break

    return False


print("Forward Chaining = ")

rules = [
    ({"P"}, "Q"),          # P → Q
    ({"L", "M"}, "P"),     # L ∧ M → P
    ({"A", "B"}, "L")      # A ∧ B → L
]

facts = {"A", "B", "M"}  # Given facts
goal = "Q"

print("Result = ", forward_chaining(rules, facts, goal))


print("\nForward Chaining = ")

rulesb = [
    ({"A"}, "B"),          # A → B
    ({"B"}, "C"),          # B → C
    ({"C"}, "D"),          # C → D
    ({"D", "E"}, "F")      # D ∧ E → F
]

factsb = {"A", "E"}  # Given facts
goalb = "F"

print("Result = ", forward_chaining(rulesb, factsb, goalb))