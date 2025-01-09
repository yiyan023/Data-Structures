class Solution:
    def sumZero(self, n: int) -> List[int]:
        acc = 0
        result = []

        for n in range(n-1):
            result.append(n + 1)
            acc += n + 1
        
        result.append(0 - acc)

        return result
