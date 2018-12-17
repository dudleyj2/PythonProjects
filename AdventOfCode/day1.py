# Advent of Code Challenge Day 1


def main():
    # Day 1 Part 1
    sum = 0
    with open('frequencies.txt') as f:
        for line in f:
            sum += int(line)
    print("Part 1: " + str(sum))

    # Day 1 Part 2
    changes = []
    with open('frequencies.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            changes.append(line)

    result = False
    index = 0
    current_frequency = 0
    past_frequencies = {str(current_frequency): 1}

    while(result is False):
        if (index == len(changes)):
            index = 0
        item = str(changes[index])
        if item[0] == '+':
            current_frequency += int(item[1:])
        else:
            current_frequency -= int(item[1:])

        if str(current_frequency) in past_frequencies:
            print("Part 2: " + str(current_frequency))
            result = True
        else:
            past_frequencies.update({str(current_frequency): 1})

        index += 1


main()
