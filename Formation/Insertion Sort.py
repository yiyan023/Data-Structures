def insertion_sort(array: list[int]) -> [int]:
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    
    return array
