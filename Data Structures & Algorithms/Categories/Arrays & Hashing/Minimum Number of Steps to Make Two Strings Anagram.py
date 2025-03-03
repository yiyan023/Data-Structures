class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # frequency? 
        s_freq = Counter(s)
        t_freq = Counter(t)

        diff_freq = defaultdict(int)
        
        for key in t_freq:
            if s_freq[key] != t_freq[key]:
                diff_freq[key] += max(0, t_freq[key] - s_freq[key])
        
        return sum(diff_freq.values())
