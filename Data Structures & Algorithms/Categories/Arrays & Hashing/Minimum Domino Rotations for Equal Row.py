class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        possibilities = [tops[0], bottoms[0]]
        maxFreq = 0
        
        for i in range(1, len(tops)):
            if possibilities[0] != tops[i] and possibilities[0] != bottoms[i]:
                possibilities[0] = 0
            
            if possibilities[1] != tops[i] and possibilities[1] != bottoms[i]:
                possibilities[1] = 0
            
        for i in range(len(possibilities)):
            topFreq, bottomFreq = 0, 0

            if not possibilities[i]:
                continue 
            
            for j in range(len(tops)):
                if tops[j] == possibilities[i]:
                    topFreq += 1
                
                if bottoms[j] == possibilities[i]:
                    bottomFreq += 1

            if topFreq > maxFreq or bottomFreq > maxFreq:
                maxFreq = max(topFreq, bottomFreq)

        return len(tops) - maxFreq if maxFreq > 0 else -1
