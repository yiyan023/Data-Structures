class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = set(candyType)
        eat = len(candyType) // 2
        
        return min(eat, len(candy))
