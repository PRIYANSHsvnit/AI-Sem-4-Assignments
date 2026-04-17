def railgaadi(percept):
    inbound, outbound, obstacle, emergency = percept

    # Manual emergency
    if emergency == "A":
        return ("GD", "SO", "SR")    # Gate Down, Siren ON, Signal RED

    # Obstacle on crossing
    if obstacle == "D":
        return ("GU", "SO", "SR")    # Gate UP, Siren ON, Signal RED

    # Train approaching
    if inbound == "D" or outbound == "D":
        return ("GD", "SO", "SG")    # Gate Down, Siren ON, Signal GREEN

    # Normal safe condition
    return ("GU", "SOF", "SG")       # Gate UP, Siren OFF, Signal GREEN

s_table = [                 # D = Detected , ND = Not Detected , C = Clear , N = Neutral , A = Active 
    ("D", "ND", "C", "N"),   # Train approaching
    ("D", "ND", "D", "N"),   # Obstacle present
    ("ND", "ND", "C", "N"),  # Normal condition
    ("ND", "ND", "C", "A")   # Manual emergency
]

S_table_states = {
    0:("D", "ND", "C", "N"),
    1:("D", "ND", "D", "N"),
    2:("ND", "ND", "C", "N"),
    3:("ND", "ND", "C", "A")
}

dict_naming = {
    "GD": "Gate Down",
    "GU": "Gate Up",
    "SO": "Siren ON",
    "SOF": "Siren OFF",
    "SR": "Signal RED",
    "SG": "Signal GREEN",
    "D" : "Detected",
    "ND": "Not Detected",
    "C" : "Clear",
    "N" : "Neutral",
    "A" : "Active"
}

print(" Indian Railways Level Crossing Simulation \n")

for i, percept in enumerate(s_table, start=1):
    action = railgaadi(percept)

    print(f"Scenario {i}")
    print("Location => Railway Level Crossing")
    print(f"Percept => Inbound - {dict_naming[percept[0]]}, Outbound - {dict_naming[percept[1]]}, "
          f"Obstacle - {dict_naming[percept[2]]}, Emergency - {dict_naming[percept[3]]}")
    print(f"Action => {dict_naming[action[0]]}, {dict_naming[action[1]]}, {dict_naming[action[2]]}\n")