class Solution:
  def maxNumberOfFamilies(self, n, reservedSeats):
    occupied = defaultdict(set)
    result = 2 * n

    for r, c in reservedSeats:
        if c in {2, 3, 4, 5}:
            occupied[r].add('left')
        
        if c in {4, 5, 6, 7}:
            occupied[r].add('middle')
        
        if c in {6, 7, 8, 9}:
            occupied[r].add('right')
    
    for r in occupied:
        if len(occupied[r]) < 3:
            result -= 1
        
        else:
            result -= 2

    return result
