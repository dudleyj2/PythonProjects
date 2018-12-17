# Advent of Code Challenge Day 2
from string import ascii_lowercase


def main():
    # Day 2 Part 1
    boxes = []
    with open('boxes.txt') as b:
        for line in b:
            line = line.rstrip('\n')
            boxes.append(line)

    total_2 = 0
    total_3 = 0
    for b in boxes:
        letter_dict = {x: 0 for x in ascii_lowercase}
        has_2 = False
        has_3 = False

        for i in range(len(b)):
            total = letter_dict.get(b[i])
            total += 1
            letter_dict.update({b[i]: total})

        for key in letter_dict:
            if letter_dict.get(key) == 2:
                has_2 = True
            if letter_dict.get(key) == 3:
                has_3 = True

        if has_2 is True:
            total_2 += 1
        if has_3 is True:
            total_3 += 1

    print("Part 1: " + str(total_2 * total_3))

    # Day 2 Part 2
    for b in range(len(boxes) - 1):
        for o in range(b+1, len(boxes)):
            id_1 = str(boxes[b])
            id_2 = str(boxes[o])
            amount_unequal = 0
            unmatched_letter_index = 0
            for i in range(len(id_1)):
                if (id_1[i] != id_2[i]):
                    amount_unequal += 1
                    unmatched_letter_index = i
            if amount_unequal < 2:
                print("Part 2: " + id_1[:unmatched_letter_index] +
                      id_1[unmatched_letter_index+1:])


main()
