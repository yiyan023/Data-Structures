def reverse(array):
    l, r = 0, len(array) - 1

    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    
    return array
