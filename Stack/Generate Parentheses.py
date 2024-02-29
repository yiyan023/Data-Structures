class Solution:
    def generateParenthesis(self, n):
        result = []

        def dfs(openN, closeN, string):
            if len(string) == 2 * n:
                result.append(string)
            
            if openN < n:
                dfs(openN + 1, closeN, string + "(")
            
            if closeN < openN:
                dfs(openN, closeN + 1, string + ")")
        
        dfs(0, 0, '')
        return result

        