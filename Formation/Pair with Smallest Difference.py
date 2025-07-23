def smallest_diff(array1, array2):
    array1.sort()
    array2.sort()

    i, j = 0, 0 
    res = [float('inf'), -float('inf')]

    while i < len(array1) and j < len(array2):
        if abs(array1[i] - array2[j]) < abs(res[0] - res[1]):
            res = [array1[i], array2[j]]

        if array1[i] < array2[j]:
            i += 1
        
        else:
            j += 1
    
    return res

print(smallest_diff([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])) # => [28, 26])
# smallestDiff([1, 2], [1, 2]) => [1, 1]
# smallestDiff([-20, -30], [-25, -35]) # [-30, -35], [-30, -25] or [-20, -25] all are correct
# Signature/Prototype
