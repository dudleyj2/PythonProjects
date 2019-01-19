# These solutions are not meant to serve as a python
# script.  They are simply solution methods to the
# associated problem found at https://codingbat.com/python/List-1


# 1
def first_last6(nums):
    return nums[0] == 6 or nums[len(nums)-1] == 6


# 2
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[len(nums)-1]


# 3
def make_pi():
    arr = [3, 1, 4]
    return arr


# 4
def common_end(a, b):
    return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]


# 5
def sum3(nums):
    return nums[0] + nums[1] + nums[2]


# 6
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


# 7
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]


# 8
def max_end3(nums):
    max_nums = max(nums[0], nums[2])
    return [max_nums, max_nums, max_nums]


# 9
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]


# 10
def middle_way(a, b):
    return [a[1], b[1]]


# 11
def make_ends(nums):
    if len(nums) == 1:
        return [nums[0], nums[0]]
    else:
        return [nums[0], nums[len(nums)-1]]


# 12
def has23(nums):
    return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3
