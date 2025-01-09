class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        arr1, arr2 = self.word_indices[word1], self.word_indices[word2]
        i, j = 0, 0
        minVal = float('inf')

        while i < len(arr1) and j < len(arr2):
            minVal = min(minVal, abs(arr1[i] - arr2[j]))

            if arr1[i] < arr2[j]:
                i += 1

            else:
                j += 1

        return minVal


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
