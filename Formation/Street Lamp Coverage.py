# idea: sort by position and then radius

# brute force:
# literally iterate through every position. within a radius to check if it is lit 

# count number of 1s

# bigger question: which positions have no overlap? 

# thinking of converting to intervals, sorting, and then finding which intervals have no overlaps. 

# also keep track of the previous lit area (max position)

# if the array has no overlap, then we can add thoe difference btween start and end 

# seet the previous set of lamps equal to this interval 


# otherwise, if the current does have overlap (the start of this array is less or equal to the end of the array ), then we will find the max between 0 and the difference between teh current arrays end to the previous arrays end 

# update the max lit area to the max between the current value and the end value 

def litByOneLight(lamps):
    if not lamps:
        return 0
    
    ranges = []

    for p, r in lamps:
        ranges.append([p-r, p+r])
    
    ranges.sort()
    prev_range = ranges[0]
    res = abs(prev_range[1] - prev_range[0]) + 1

    for i in range(1, len(ranges)):
        if ranges[i][0] > prev_range[1]:
            res += abs(ranges[i][1] - ranges[i][0]) + 1
            prev_range = ranges[i]
        
        else:
            res += max(0, abs(ranges[i][1] - prev_range[1]))
            res -= (prev_range[1] - max(ranges[i][0], prev_range[0]) +1)
            
            prev_range[0] = prev_range[1] + 1
            prev_range[1] = max(prev_range[1], ranges[i][1])
    
    return res

print(litByOneLight([[1, 1]]) == 3)
print(litByOneLight([[1, 1], [2, 1]]) == 2)
print(litByOneLight([[1, 1], [3, 1]]) == 4)
print(litByOneLight([[1, 1], [4, 1]]) == 6)
print(litByOneLight([]) == 0)
print(litByOneLight([[1, 0]]) == 1)
print(litByOneLight([[5, 2]]) == 5)
print(litByOneLight([[5, 2], [4, 1], [6, 1]]) == 0)
print(litByOneLight([[-5, 2], [-4, 1], [-6, 1]]) == 0)
print(litByOneLight([[-5, 2]]) == 5)
