def waterPlants(plants, capacity):
    water = 0
    steps = 0
    
    if not plants or not capacity:
        return 0
    
    for i, p in enumerate(plants):
        if p > capacity:
            return -1
        
        if water + p > capacity:
            steps += 2 * i
            water = 0
        
        water += p
        steps += 1
    
    return steps

if __name__ == "__main__":
    arr = [2, 4, 5, 1, 2]
    cap = 6
    
    steps = waterPlants(arr, cap)
    print(steps)
