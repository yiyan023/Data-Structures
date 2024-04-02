class Solution:
    def findCircleNum(self, isConnected):
        def dfs(i):
            visit.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visit:
                    dfs(j)
            
        
        visit = set()
        provinces = 0
        
        for i in range(len(isConnected)):
            if i not in visit:
                dfs(i)
                provinces += 1
        
        return provinces