#Districts
districts = [
    "Kutch", "Banaskantha", "Patan", "Mehsana", "Sabarkantha",
    "Gandhinagar", "Ahmedabad", "Kheda", "Panchmahal", "Dahod",
    "Vadodara", "Anand", "Bharuch", "Narmada", "Surat",
    "Navsari", "Valsad", "Dang", "Amreli",
    "Bhavnagar", "Junagadh", "Rajkot", "Jamnagar", "Porbandar",
    "Surendranagar"
]

#Graph
graph = {
    "Kutch": ["Banaskantha", "Surendranagar", "Jamnagar"],
    "Banaskantha": ["Kutch", "Patan", "Sabarkantha"],
    "Patan": ["Banaskantha", "Mehsana", "Surendranagar"],
    "Mehsana": ["Patan", "Sabarkantha", "Gandhinagar", "Ahmedabad"],
    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar", "Panchmahal", "Ahmedabad"],
    "Gandhinagar": ["Mehsana", "Sabarkantha", "Ahmedabad"],
    "Ahmedabad": ["Mehsana", "Gandhinagar", "Kheda", "Anand", "Surendranagar", "Sabarkantha"],
    "Kheda": ["Ahmedabad", "Anand", "Panchmahal"],
    "Panchmahal": ["Sabarkantha", "Kheda", "Vadodara", "Dahod"],
    "Dahod": ["Panchmahal", "Vadodara"],
    "Vadodara": ["Panchmahal", "Dahod", "Anand", "Bharuch", "Narmada"],
    "Anand": ["Ahmedabad", "Kheda", "Vadodara", "Bharuch"],
    "Bharuch": ["Vadodara", "Anand", "Surat", "Narmada"],
    "Narmada": ["Vadodara", "Bharuch", "Surat"],
    "Surat": ["Bharuch", "Narmada", "Navsari"],
    "Navsari": ["Surat", "Valsad", "Dang"],
    "Valsad": ["Navsari", "Dang"],
    "Dang": ["Valsad", "Navsari"],
    "Amreli": ["Bhavnagar", "Junagadh", "Rajkot"],
    "Bhavnagar": ["Amreli", "Ahmedabad"],
    "Junagadh": ["Amreli", "Porbandar", "Rajkot"],
    "Rajkot": ["Junagadh", "Amreli", "Surendranagar", "Jamnagar"],
    "Jamnagar": ["Kutch", "Rajkot", "Porbandar"],
    "Porbandar": ["Jamnagar", "Junagadh"],
    "Surendranagar": ["Kutch", "Patan", "Ahmedabad", "Rajkot"]
}

#Make symmetric
for node in list(graph.keys()):
    for neighbor in graph[node]:
        if neighbor not in graph:
            graph[neighbor] = []
        if node not in graph[neighbor]:
            graph[neighbor].append(node)

#Constraint check
def is_valid(district, color, assignment):
    for neighbor in graph[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

#Degree heuristic
def select_unassigned_variable(assignment):
    unassigned = [d for d in districts if d not in assignment]
    return max(unassigned, key=lambda d: len(graph[d]))

#Backtracking with given colors
def solve(assignment, colors):
    if len(assignment) == len(districts):
        return assignment

    district = select_unassigned_variable(assignment)

    for color in colors:
        if is_valid(district, color, assignment):
            assignment[district] = color

            result = solve(assignment, colors)
            if result:
                return result

            del assignment[district]

    return None

#Minimum colors
def find_min_colors():
    for k in range(1, len(districts)+1):
        colors = list(range(k))  # use numbers instead of names
        solution = solve({}, colors)

        if solution:
            return k, solution

    return None, None

#Run
min_colors, solution = find_min_colors()

#Output
print(f"\nMinimum colors required = {min_colors}\n")

color_emojis = ["🔴", "🟢", "🔵", "🟡", "🟠", "🟣"]

if solution:
    for district in sorted(solution):
        print(f"{district:15} -> {color_emojis[solution[district]]}")