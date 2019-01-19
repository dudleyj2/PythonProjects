# These solutions are not meant to serve as a python
# script.  They are simply solution methods to the
# associated problem found at https://codingbat.com/python/String-1


# 1
def cigar_party(cigars, is_weekend):
    if is_weekend is True:
        return cigars > 39
    else:
        return cigars > 39 and cigars < 61


# 2
def date_fashion(you, date):
    if you < 3 or date < 3:
        return 0
    elif you > 7 or date > 7:
        return 2
    else:
        return 1


# 3
def squirrel_play(temp, is_summer):
    if is_summer is True:
        return temp < 101 and temp > 59
    else:
        return temp < 91 and temp > 59


# 4
def caught_speeding(speed, is_birthday):
    low_lim = 61
    high_lim = 81
    if is_birthday is True:
        low_lim += 5
        high_lim += 5

    if speed < low_lim:
        return 0
    elif speed < high_lim:
        return 1
    else:
        return 2


# 5
def sorta_sum(a, b):
    sum = a + b
    if sum > 9 and sum < 20:
        return 20
    else:
        return sum


# 6
def alarm_clock(day, vacation):
    if vacation is False:
        if day > 0 and day < 6:
            return "7:00"
        else:
            return "10:00"
    elif day > 0 and day < 6:
        return "10:00"
    else:
        return "off"


# 7
def love6(a, b):
    if a == 6 or b == 6:
        return True
    elif a - b == 6 or b - a == 6:
        return True
    elif a + b == 6 or a + b == 6:
        return True
    else:
        return False


# 8
def in1to10(n, outside_mode):
    if outside_mode is False:
        return n > 0 and n < 11
    else:
        return n < 2 or n > 9


# 9
def near_ten(num):
    mod = num % 10
    if mod == 8 or mod == 9 or mod == 0 or mod == 1 or mod == 2:
        return True
    else:
        return False
