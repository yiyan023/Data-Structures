class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        result = []
        unique = []
        
        for n in arr1:
            freq[n] = 1 + freq.get(n, 0)
            
            if n not in arr2:
                unique.append(n)
        
        for n in arr2:
            while freq[n]:
                result.append(n)
                freq[n] -= 1
        
        return result + sorted(unique)
