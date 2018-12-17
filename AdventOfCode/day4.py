# Advent of Code Challenge Day 4


def main():
    # Day 4 Part 1 and 2
    observations = []
    with open('observations.txt') as o:
        for line in o:
            line = line.rstrip('\n')
            observations.append(line)

    observations = sorted(observations)
    i = 0
    guards = {}

    minute_high_p2 = 0
    minute_p2 = 0
    min_high_guard = ""
    while i < len(observations):
        o = observations[i]
        if o[25:26] == '#':
            guard = o[26:o.find('b')-1]
            i += 1
            o_next = observations[i]

            if guards.get(guard) is None:
                g_minutes = {}
                for q in range(60):
                    g_minutes.update({str(q): 0})
                guards.update({guard: g_minutes})

            if o_next[25:26] == '#':
                i -= 1

            else:
                while o_next[25:26] != '#':
                    if o_next[25:26] == 'u':
                        o_last = observations[i-1]
                        start_nap = o_last[15:17]
                        end_nap = o_next[15:17]
                        time_napping = int(end_nap) - int(start_nap)

                        for p in range(time_napping):
                            minute = int(start_nap) + p
                            prev_total = int(guards[guard][str(minute)])
                            guards[guard][str(minute)] = prev_total + 1

                            if (guards[guard][str(minute)] > minute_high_p2):
                                minute_high_p2 = guards[guard][str(minute)]
                                min_high_guard = guard
                                minute_p2 = minute

                    i += 1
                    if (i == 1040):
                        break

                    o_next = observations[i]
                i -= 1
        i += 1

    high_sum = 0
    sum_high_guard = ""
    for guard in guards:
        current_sum = 0
        for k in range(59):
            current_sum += int(guards[guard][str(k)])

        if current_sum > high_sum:
            high_sum = current_sum
            sum_high_guard = guard

    high_sum_min = 0
    minute_p1 = 0
    for k in range(59):
        curr_high_sum_min = int(guards[sum_high_guard][str(k)])
        if curr_high_sum_min > high_sum_min:
            high_sum_min = curr_high_sum_min
            minute_p1 = k

    print("Day 4 Part 1: " + str(int(sum_high_guard) * int(minute_p1)))
    print("Day 4 Part 2: " + str(int(min_high_guard) * int(minute_p2)))


main()
