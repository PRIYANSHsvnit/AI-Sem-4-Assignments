def resolve(ci, cj):
    """
    Try resolving two clauses
    ci, cj are sets of literals
    """
    resolvents = []

    for literal in ci:
        if f"~{literal}" in cj:
            new_clause = (ci - {literal}) | (cj - {f'~{literal}'})
            resolvents.append(new_clause)

        elif literal.startswith("~") and literal[1:] in cj:
            new_clause = (ci - {literal}) | (cj - {literal[1:]})
            resolvents.append(new_clause)

    return resolvents


def resolution(kb, goal):
    """
    kb: list of clauses (each clause is a set)
    goal: literal to prove
    """

    # Add negation of goal
    neg_goal = {f"~{goal}"}
    clauses = kb + [neg_goal]

    print(f"Negated goal added = {neg_goal}")

    new = []

    while True:
        pairs = [(clauses[i], clauses[j])
                 for i in range(len(clauses))
                 for j in range(i+1, len(clauses))]

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)

            for r in resolvents:
                print(f"Resolving {ci} and {cj} → {r}")

                if len(r) == 0:
                    print("\nDerived empty clause ⇒ PROVED")
                    return True

                new.append(r)

        # If no new clauses
        if all(r in clauses for r in new):
            return False

        for r in new:
            if r not in clauses:
                clauses.append(r)


print("\nResolution = ")

# CNF Conversion:
# P ∨ Q
# P → R  => ~P ∨ R
# Q → S  => ~Q ∨ S
# R → S  => ~R ∨ S

kb = [
    {"P", "Q"},
    {"~P", "R"},
    {"~Q", "S"},
    {"~R", "S"}
]

goal = "S"

print("Result = ", resolution(kb, goal))

print("\nResolution = ")

# CNF:
# P → Q => ~P ∨ Q
# Q → R => ~Q ∨ R
# S → ~R => ~S ∨ ~R
# P (fact)

kbb = [
    {"~P", "Q"},
    {"~Q", "R"},
    {"~S", "~R"},
    {"P"}
]

goalb = "S"

print("Result = ", resolution(kbb, goalb))