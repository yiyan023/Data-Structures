class Solution:
    def compress(self, chars: List[str]) -> int:
        result, i = 0, 0

        while i < len(chars):
            cur = chars[i]
            length = 0

            while i < len(chars) and chars[i] == cur:
                i += 1
                length += 1
            
            chars[result] = cur 
            result += 1

            if length > 1:
                for c in str(length):
                    chars[result] = c
                    result += 1
        
        return result
