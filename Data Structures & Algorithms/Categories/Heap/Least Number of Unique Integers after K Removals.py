class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_hash = Counter(arr)
        min_heap = list(freq_hash.values())
        heapify(min_heap)
        
        while k > 0 and min_heap:
            if k >= min_heap[0]:
                num = heapq.heappop(min_heap)
                k -= num

            else:
                break
        
        return len(min_heap)
