rooms = {
    "A": "Ganda", # Dirty
    "B": "Ganda",
    "C": "Saaf" # Clean
}

# Rule table
rules = {
    ("A", "Ganda"): "S",
    ("B", "Ganda"): "S",  # S-suck
    ("C", "Ganda"): "S",
    ("A", "Saaf"): "MR", # Move Right
    ("B", "Saaf"): "MR",
    ("C", "Saaf"): "ML"  # Move Left
}

dict_naming = {
    "S": "Suck",
    "MR": "Move Right",
    "ML": "Move Left",
    "NO": "No Operation",
}

# Initial location
location = "A"

print(" Starting = \n")

for step in range(10):

    percept = (location, rooms[location])

    # Check if all rooms are clean
    if all(status == "C" for status in rooms.values()):
        action = "NO"  # No operation
        print(f"Step {step+1} => Location = {location} , Percept = {percept} , Action = {dict_naming[action]} ")
        break

    # Select action using rule table
    action = rules.get(percept)

    print(f"Step {step+1} => Location = {location} , Percept = {percept} , Action = {dict_naming[action]} ")

    # Execute action
    if action == "S":
        rooms[location] = "Saaf"

    elif action == "MR":
        if location == "A":
            location = "B"
        elif location == "B":
            location = "C"

    elif action == "ML":
        if location == "C":
            location = "B"
        elif location == "B":
            location = "A"

print("\nFinal Room Status = ", rooms)