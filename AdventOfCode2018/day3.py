# Advent of Code Challenge Day 3


def main():
    # Day 3 Part 1
    measurements = []
    with open('measurements.txt') as m:
        for line in m:
            line = line.rstrip('\n')
            measurements.append(line)

    matrix = [[0]*1000 for i in range(1000)]
    total_overlap = 0

    for i in range(len(measurements)):
        sq = measurements[i]
        col_start = int(sq[sq.find('@')+2:sq.find(',')])
        col_len = int(sq[sq.find(':')+2:sq.find('x')])
        row_start = int(sq[sq.find(',')+1:sq.find(':')])
        row_len = int(sq[sq.find('x')+1:])

        for i in range(col_len):
            for j in range(row_len):
                matrix[i+col_start][j+row_start] += 1
                if matrix[i+col_start][j+row_start] == 2:
                    total_overlap += 1

    print("Day 3 Part 1: " + str(total_overlap))

    # Day 3 Part 2
    for i in range(len(measurements)):
        sq = measurements[i]
        col_start = int(sq[sq.find('@')+2:sq.find(',')])
        col_len = int(sq[sq.find(':')+2:sq.find('x')])
        row_start = int(sq[sq.find(',')+1:sq.find(':')])
        row_len = int(sq[sq.find('x')+1:])

        good_sq = True

        for i in range(col_len):
            for j in range(row_len):
                if matrix[i+col_start][j+row_start] != 1:
                    good_sq = False

        if good_sq is True:
            print("Day 3 Part 2: " + sq[1:sq.find('@')-1])


main()
