# These solutions are not meant to serve as a python
# script.  They are simply solution methods to the 
# associated problem found at https://codingbat.com/python/List-1


#1
def first_last6(nums):
    return nums[0] == 6 or nums[len(nums)-1] == 6


#2
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[len(nums)-1]
  

#3
def make_pi():
    arr = [3, 1, 4]
    return arr


#4
def common_end(a, b):
    return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]


#5
