class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_trans = {}
        count = 0
        pattern_code = ""
        res = []

        for c in pattern:
            if c not in pattern_trans:
                pattern_trans[c] = str(count)
                count += 1
            
            pattern_code += pattern_trans[c] + ","
        
        for word in words:
            word_trans = {}
            word_count = 0
            word_code = ""

            for c in word:
                if c not in word_trans:
                    word_trans[c] = str(word_count)
                    word_count += 1
                
                word_code += word_trans[c] + ","
            
            if word_code == pattern_code:
                res.append(word)
        
        return res
