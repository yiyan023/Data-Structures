"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idx_hash = {}
        visited = set()

        for i in range(len(employees)):
            idx_hash[employees[i].id] = i
        
        def dfs(idx):
            if employees[idx].id in visited:
                return 0
            
            visited.add(employees[idx].id)
            importance = employees[idx].importance

            for nei in employees[idx].subordinates:
                if nei not in visited:
                    importance += dfs(idx_hash[nei])
            
            return importance 
        
        return dfs(idx_hash[id])
