from collections import defaultdict
def num_uniques(array: list[int]) -> int:
    res = 0
    num_freq = defaultdict(int)

    for num in array:
        num_freq[num] += 1

        if num_freq[num] == 1:
            res += 1
        
        elif num_freq[num] == 2:
            res -= 1
    
    return res

print(num_uniques([])) # 0
print(num_uniques([3, 1, 1, 2, 3, 1, 1, 1, 4])) # 2
print(num_uniques([1])) # 1
