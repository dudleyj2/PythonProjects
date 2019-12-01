# Advent of Code Challenge Day 6
from string import ascii_lowercase


def main():
    # Day 5 Part 1
    left = []
    right = []
    with open('coordinates.txt') as c:
        for line in c:
            line = line.rstrip('\n')
            left_coord, right_coord = line[:line.find(',')], line[line.find(',') + 2:]
            left.append(left_coord)
            right.append(right_coord)
    
    max_coord = 0
    for i in range(len(left)):
        max_coord = max(int(left[i]), int(right[i]), max_coord + 1)
    
    matrix = [["."]*max_coord for i in range(max_coord)]
    
    for i in range(len(left)):
        matrix[int(left[i])][int(right[i])] = i

    matrix = manhattan(matrix)


def manhattan(matrix):
    


main()
