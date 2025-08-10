import bisect 

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted(s for s, _ in flowers)
        end = sorted((e for _, e in flowers))
        res = []

        for p in people:
            s_idx = bisect.bisect_right(start, p)
            e_idx = bisect.bisect_left(end, p) 

            res.append(s_idx - e_idx)
    
        return res
