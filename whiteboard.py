# You must implement a function that returns the difference between the biggest and the smallest value in a list(lst) received as parameter.

# The list(list_nums) contains integers, which means it may contain some negative numbers.

# If the list is empty or contains a single element, return 0.

# The list(list_nums) is not sorted.

# solution([1, 2, 3, 4])   return 3, because 4 - 1 == 3
# solution([1, 2, 3, -4])   return 7, because 3 - (-4) == 7

# find max, find min, 
# return max minus min


def solution(list_nums):
    if len(list_nums) == 0:
        return 0
    return max(list_nums)-min(list_nums) 
print(solution([1, 2, 3, 4]))
