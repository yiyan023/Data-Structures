class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = [weights[i] + weights[i+1] for i in range(len(weights)-1)]
        pairs.sort()

        res = 0

        for i in range(k - 1):
            res += pairs[len(pairs) - i - 1] - pairs[i]
        
        return res
