class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        sequences = defaultdict(int)

        for i in range(m, len(arr) - m + 1):
            if arr[i:i+m] == arr[i-m:i]:
                if not sequences[i%m]:
                    sequences[i%m] += 1
                
                sequences[i%m] += 1

                if sequences[i%m] >= k:
                    return True 
            
            else:
                sequences[i%m] = 0
        
        return False
