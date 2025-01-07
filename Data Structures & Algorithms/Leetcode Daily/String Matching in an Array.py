class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x: len(x))
        res = []

        for l in range(len(words)):
            for r in range(l + 1, len(words)):
                if words[l] in words[r]:
                    res.append(words[l])
                    break
        
        return res
