# 2019 Advent of Code Challenge Day 1

def get_total_fuel(mass):
    total_fuel = mass//3 - 2
    if total_fuel < 0:
        return 0
    return total_fuel + get_total_fuel(total_fuel)

def main():
    # Day 1 Part 1
    total_fuel = 0
    with open('day1_input.txt') as f:
        for line in f:
            module_mass = int(line)//3 - 2
            total_fuel += module_mass
    print(f'Day 1 Part 1: {total_fuel}')

    total_fuel = 0
    with open('day1_input.txt') as f:
        for line in f:
            module_mass = int(line)
            module_total_fuel = get_total_fuel(module_mass)
            total_fuel += module_total_fuel
    print(f'Day 1 Part 2: {total_fuel}')

main()

# this is a new commit test

