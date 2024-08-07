class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total, cur = sum(cardPoints[n-k:n]), sum(cardPoints[n-k:n])
        l, r = 0, n - k

        while r < n:
            cur += cardPoints[l] - cardPoints[r]
            total = max(total, cur)
            l, r = l + 1, r + 1
        
        return total
