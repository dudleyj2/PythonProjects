# Advent of Code Challenge Day 4
from string import ascii_lowercase


def main():
    # Day 5 Part 1
    with open('polymer.txt') as p:
        polymer = p.readlines()[0]

    part_1 = react_polymer(polymer)
    print("Day 5 Part 1: " + str(len(part_1)))

    # Day 5 Part 2
    shortest_poly = len(part_1)
    for c in ascii_lowercase:
        new_poly = polymer.replace(c.lower(), "").replace(c.upper(), "")
        part_2 = react_polymer(new_poly)
        if len(part_2) < shortest_poly:
            shortest_poly = len(part_2)

    print("Day 5 Part 2: " + str(shortest_poly))


def reaction(a, b):
    return a != b and a.lower() == b.lower()


def react_polymer(polymer):
    reacted = []
    for letter in polymer:
        if len(reacted) > 0 and reaction(reacted[-1], letter):
            reacted.pop()
        else:
            reacted.append(letter)
    return reacted


main()
