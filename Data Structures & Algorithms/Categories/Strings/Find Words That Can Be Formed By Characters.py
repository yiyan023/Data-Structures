class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        result = 0
        
        for char in chars:
            freq[char] = 1 + freq.get(char, 0)
        
        for word in words:
            chars = {}
            addString = True
            
            for c in word:
                chars[c] = 1 + chars.get(c, 0)
                
                if c not in freq or chars[c] > freq[c]:
                    addString = False 
                    break 
            
            result += len(word) if addString else 0
        
        return result
