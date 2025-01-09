class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"   
        }

        result = []

        def dfs(i, string):
            if i == len(digits):
                if string != "":
                    result.append(string) 
                return 
            
            for c in letter[digits[i]]:
                dfs(i + 1, string + c)
        
        dfs(0, "")
        return result
            
