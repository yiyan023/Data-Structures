class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        res = ""

        for key in freq:
            heapq.heappush(heap, (-freq[key], key))

        while heap:
            num, c = heapq.heappop(heap)
            res += (-num * c)
        
        return res
