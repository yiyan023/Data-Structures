# explore 
# will we have to deal with empty array? in that case, would we return 0?

# are we assuming that all elements are valid integers, so don't need to deal with strings or anything? 

# other questions:
# will the array be sorted? 
# will the numbers be positive/negative? 

# test cases
# empty array, array of size 1
# array of all the same elements (1) 
# array with all unique elements (2)
# array with some duplicates (3)
# array with a mix of positive + negative numbers, (2), (3)
# array with all positive (1, 2, 3)
# array with all negative (1, 2, 3)

# brainstorm: 
# 1. brute force solution - iterate through the array & check every previous element to see if it exists already 
# O(n^2) time and O(1) space 

# 2. use a set to check if the number already exists in the array 
# O(n) time complexity & space complexity 

# 3. use a hash to store the frequency of the number - if the frequency is greater than 1, then we don't count it 
# same time and space 

# 2 makes the most sense - the key-value pair for the dictionary doesn't provide much value and I'm making a trade-off for space complexity to optimize the time complexity 

def count_distinct_values(array: list[int]) -> int:
    array_set = set(array)
    return len(array_set)


