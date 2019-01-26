import random

# Monty Hall Simulation

doors = ["A", "B", "C"]
games = []
for i in range(100000):
    # Randomly create a winning door, either A, B, or C
    winning_door = random.choice(doors)
    if winning_door == "A":
        games.append([1, 0, 0])
    elif winning_door == "B":
        games.append([0, 1, 0])
    else:
        # winning_door is "C"
        games.append([0, 0, 1])


total_door_A_wins = 0
for i in range(100000):
    total_door_A_wins += games[i][0]

print(f"Door 'A' Success Rate: {total_door_A_wins/100000}")


switch_total = 0
for i in range(100000):
    # Find which doors of B and C contain a goat
    goat_doors = []
    if games[i][1] == 0:
        goat_doors.append("B")
    elif games[i][2] == 0:
        goat_doors.append("C")

    # Randomly choose a door that has a goat behind it to be revealed
    revealed_door = random.choice(goat_doors)

    # Switch to the door that is not door A, the original choice, and is not
    # the revealed_door

    if revealed_door == "B":
        # Door B is revealed, so we switch to the contents of door C
        switch_total += games[i][2]

    else:
        # Door C is revealed, so we switch to the contents of door B
        switch_total += games[i][1]

print(f"Switch Door Success Rate: {switch_total/100000}")
