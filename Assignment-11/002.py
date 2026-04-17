letters = ['S','E','N','D','M','O','R','Y']
digits = range(10)

def solve():
    assignment = {}
    used_digits = set()
    return backtrack(assignment, used_digits)

def backtrack(assignment, used_digits):
    # If all letters assigned then solution found
    if len(assignment) == len(letters):
        if check_full_solution(assignment):
            return assignment
        return None

    # Select next unassigned variable
    for letter in letters:
        if letter not in assignment:
            break

    for digit in digits:
        # Skip already used digits
        if digit in used_digits:
            continue

        # Leading digit constraint
        if (letter == 'S' or letter == 'M') and digit == 0:
            continue

        # Assign
        assignment[letter] = digit
        used_digits.add(digit)

        # Early pruning
        if is_partial_valid(assignment):
            result = backtrack(assignment, used_digits)
            if result:
                return result

        # Backtrack
        del assignment[letter]
        used_digits.remove(digit)

    return None


#Early constraint checking (column-wise)
def is_partial_valid(a):
    # Only safe constraint (no carry involved)
    if all(k in a for k in ['D','E','Y']):
        if (a['D'] + a['E']) % 10 != a['Y']:
            return False
    return True


#Check full solution at the end (just to be sure)
def check_full_solution(a):
    SEND = a['S']*1000 + a['E']*100 + a['N']*10 + a['D']
    MORE = a['M']*1000 + a['O']*100 + a['R']*10 + a['E']
    MONEY = a['M']*10000 + a['O']*1000 + a['N']*100 + a['E']*10 + a['Y']
    return SEND + MORE == MONEY


#Solver
solution = solve()

#Output
if solution:
    print("\nSolution Found!\n")
    for k in sorted(solution):
        print(f"{k} = {solution[k]}")

    SEND = solution['S']*1000 + solution['E']*100 + solution['N']*10 + solution['D']
    MORE = solution['M']*1000 + solution['O']*100 + solution['R']*10 + solution['E']
    MONEY = solution['M']*10000 + solution['O']*1000 + solution['N']*100 + solution['E']*10 + solution['Y']

    print("\nVerification:")
    print(f"{SEND} + {MORE} = {MONEY}")

else:
    print("No solution found")