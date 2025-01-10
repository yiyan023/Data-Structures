class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        max_freq = defaultdict(int)
        
        for w2 in words2:
            cur_freq = defaultdict(int)

            for c in w2:
                cur_freq[c] += 1
                max_freq[c] = max(max_freq[c], cur_freq[c])

        for w1 in words1:
            w1_freq = Counter(w1)
            is_subset = True

            for c in max_freq.keys():
                if max_freq[c] > w1_freq[c]:
                    is_subset = False 
                    break
            
            if is_subset:
                res.append(w1)
        
        return res
                
