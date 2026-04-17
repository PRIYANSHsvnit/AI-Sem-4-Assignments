from itertools import product

class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


# NOT (~P)
def NOT(p):
    return not p

# AND (P ∧ Q)
def AND(p, q):
    return p and q

# OR (P ∨ Q)
def OR(p, q):
    return p or q

# IMPLICATION (P -> Q)
def IMPLIES(p, q):
    return (not p) or q

# BICONDITIONAL (P <-> Q)
def IFF(p, q):
    return p == q


def truth_table(symbols, func, expr_name):
    print("\nTruth Table for:", expr_name)
    print("---------------------------------")

    # Print header
    header = " ".join([s.name for s in symbols])
    print(header, "| Result")

    print("-" * (len(header) + 10))

    # Generate all combinations
    for values in product([False, True], repeat=len(symbols)):
        result = func(*values)

        # Convert True/False to T/F
        row = ["T" if v else "F" for v in values]
        print(" ".join(row), "|", "T" if result else "F")


P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')


# 1. ~P -> Q
def expr1(p, q):
    return IMPLIES(NOT(p), q)

# 2. ~P ∧ ~Q
def expr2(p, q):
    return AND(NOT(p), NOT(q))

# 3. ~P ∨ ~Q
def expr3(p, q):
    return OR(NOT(p), NOT(q))

# 4. ~P -> ~Q
def expr4(p, q):
    return IMPLIES(NOT(p), NOT(q))

# 5. ~P <-> ~Q
def expr5(p, q):
    return IFF(NOT(p), NOT(q))

# 6. (P ∨ Q) ∧ (~P -> Q)
def expr6(p, q):
    return AND(OR(p, q), IMPLIES(NOT(p), q))

# 7. (P ∨ Q) -> ~R
def expr7(p, q, r):
    return IMPLIES(OR(p, q), NOT(r))

# 8. ((P ∨ Q)->~R) <-> ((~P ∧ ~Q)->~R)
def expr8(p, q, r):
    left = IMPLIES(OR(p, q), NOT(r))
    right = IMPLIES(AND(NOT(p), NOT(q)), NOT(r))
    return IFF(left, right)

# 9. ((P->Q) ∧ (Q->R)) -> (Q->R)
def expr9(p, q, r):
    left = AND(IMPLIES(p, q), IMPLIES(q, r))
    right = IMPLIES(q, r)
    return IMPLIES(left, right)

# 10. ((P->(Q∨R)) -> (~P ∧ ~Q ∧ ~R))
def expr10(p, q, r):
    left = IMPLIES(p, OR(q, r))
    right = AND(NOT(p), AND(NOT(q), NOT(r)))
    return IMPLIES(left, right)


# Expressions with P, Q
truth_table([P, Q], expr1, "1. ~P -> Q")
truth_table([P, Q], expr2, "2. ~P ∧ ~Q")
truth_table([P, Q], expr3, "3. ~P ∨ ~Q")
truth_table([P, Q], expr4, "4. ~P -> ~Q")
truth_table([P, Q], expr5, "5. ~P <-> ~Q")
truth_table([P, Q], expr6, "6. (P ∨ Q) ∧ (~P -> Q)")

# Expressions with P, Q, R
truth_table([P, Q, R], expr7, "7. (P ∨ Q) -> ~R")
truth_table([P, Q, R], expr8, "8. ((P ∨ Q)->~R) <-> ((~P ∧ ~Q)->~R)")
truth_table([P, Q, R], expr9, "9. ((P->Q) ∧ (Q->R)) -> (Q->R)")
truth_table([P, Q, R], expr10, "10. ((P->(Q∨R)) -> (~P ∧ ~Q ∧ ~R))")