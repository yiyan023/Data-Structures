class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_freq = Counter(words)
        max_heap, res = [], []

        for word in words_freq:
            heapq.heappush(max_heap, (-words_freq[word], word))

        while k:
            freq, word = heapq.heappop(max_heap)
            res.append(word)
            k -= 1
        
        return res
        
