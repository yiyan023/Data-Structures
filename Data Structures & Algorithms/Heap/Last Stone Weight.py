import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)

            if one != two:
                newStone = one - two
                heapq.heappush(stones, newStone)
            
        stones.append(0)
        return abs(stones[0])