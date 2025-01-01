class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        arr = []
        
        def dfs(i):
            if i >= len(s):
                res.append(arr.copy())
                return 
            
            for j in range(i, len(s)):
                if palin(s[i:j+1]):
                    arr.append(s[i:j+1])
                    dfs(j + 1)
                    arr.pop()
        
        def palin(string):
            l, r = 0, len(string) - 1

            while l <= r:
                if string[l] != string[r]:
                    return False 
                
                l += 1
                r -= 1
            
            return True

        
        dfs(0)
        return res
            
            
