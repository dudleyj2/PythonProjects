# These solutions are not meant to serve as a python
# script.  They are simply solution methods to the
# associated problem found at https://codingbat.com/python/Warmup-2


# 1
def string_times(str, n):
    result = ""
    for i in range(n):
        result += str
    return result


# 2
def front_times(str, n):
    result = ""
    if len(str) < 3:
        for i in range(n):
            result += str
        return result
    for i in range(n):
        result += str[0:3]
    return result


# 3
def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


# 4
def string_splosion(str):
    result = ""
    for i in range(len(str) + 1):
        result += str[:i]
    return result


# 5
def last2(str):
    count = 0
    for i in range(len(str)-2):
        if (str[i:i+2] == str[len(str)-2:len(str)]):
            count += 1
    return count


# 6
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count


# 7
def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False


# 8
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


# 9
def string_match(a, b):
    count = 0
    index = 0
    while index < len(a)-1 and index < len(b)-1:
        if a[index] == b[index] and a[index+1] == b[index+1]:
            count += 1
        index += 1
    return count
