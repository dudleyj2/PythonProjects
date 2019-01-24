import markdown2
import random

"""
This simple python script serves as a simulation for proving the
famous Monty Hall Problem.

There are three rules to follow throughout this proof:
1) The host must always open a door that was not picked by the contestant
2) The host must always open a door that reveals a goat and never the car
3) The host must always offer the chance to switch between the originally
   chosen door and the remaining closed door
"""

"""
The first step in the process is to generate 100,000 game scenarios for
our sample size.  In each game scenario, we have put our new car prize
behind one of three doors: A, B, or C.  Thus, the probability of the
car being behind each of our doors is P(A) = 1/3, P(B) = 1/3,
and P(C) = 1/3.  Conversely, the probability that a goat is behind each
of the doors is P(A) = P(B) = P(C) = 2/3.

The 'games' list will contain a list of binary responses for where the
door is located - A '1' will indicate that the car is behind that door,
and a '0' will indicate that a goat is behind that door.
"""
doors = ["A", "B", "C"]
games = []
for i in range(100000):
    # Randomly select a random door, either A, B, or C
    winning_door = random.choice(doors)
    if winning_door == "A":
        games.append([1, 0, 0])
    elif winning_door == "B":
        games.append([0, 1, 0])
    else:
        # winning_door is "C"
        games.append([0, 0, 1])

"""
For simplicity, let's assume that the contestant always chooses door
A first.  The game show host must then open a different door to reveal
a goat (Rules 1 & 2). In the first approach, the contestant chooses
not to change their door and they remain with door A.  Thus, in order
to determine the success rate of door A, we simply sum the binary
values located in the representation of door A in our 'games' list.  In
other words, we add the 0 index of each game scenario.  If the value in
a scenario is 1, then the contestant chose A, stuck with their choice,
and was rewarded with a car!  If the value in the scenario is 0, then
the contestant chose A, did not switch to the correct door, and thus
was rewarded with a goat.  The total of adding all index 0 binary values
determines our success rate out of 100,000 game scenarios.
"""
total_door_A_wins = 0
for i in range(100000):
    total_door_A_wins += games[i][0]

print(f"Door 'A' Success Rate: {total_door_A_wins/100000}")

"""
As expected, our success rate is roughly 33.3%, or 1/3.
"""

"""
Next, we test the 'switch door' approach.  Like before, for simplicity,
we assume that the contestant always chooses door A first. The game show
host must then reveal the contents behind either door B or C (Rule 1)
and the door revealed must not contain the car (Rule 2).
"""
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


"""
Thus, throught this python simulation of 100,000 game scenarios, we have
proven that the success rate of staying with your original door is 1/3 and
the success rate of switching is 2/3.
"""