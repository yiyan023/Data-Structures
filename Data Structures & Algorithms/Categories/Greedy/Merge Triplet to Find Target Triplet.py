class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue 
            
            cur[0] = max(a, cur[0])
            cur[1] = max(b, cur[1])
            cur[2] = max(c, cur[2])
        
        return cur == target
