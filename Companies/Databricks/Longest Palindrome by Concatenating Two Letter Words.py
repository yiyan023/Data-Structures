class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        visited = Counter(words)
        hasDouble = False
        matches = 0

        for key, value in visited.items():
            if key == key[::-1]:
                matches += (value // 2) * 2
                
                if value % 2:
                    hasDouble = True 
                
            else:
                matches += min(value, visited[key[::-1]])

        return (matches + hasDouble) * 2

    
    # 5 cc =>
