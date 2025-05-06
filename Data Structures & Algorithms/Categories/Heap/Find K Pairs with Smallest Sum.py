class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        visited = set((0,0))

        while min_heap and k:
            k -= 1
            _, (x, y) = heapq.heappop(min_heap)
            res.append([nums1[x], nums2[y]])

            if (x + 1, y) not in visited and x + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[x + 1] + nums2[y], (x + 1, y)))
                visited.add((x + 1, y))
            
            if (x, y + 1) not in visited and y + 1 < len(nums2): 
                heapq.heappush(min_heap, (nums1[x] + nums2[y + 1], (x, y + 1)))
                visited.add((x, y + 1))

        return res
