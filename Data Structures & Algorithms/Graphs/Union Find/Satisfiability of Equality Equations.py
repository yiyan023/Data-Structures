class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        letters = list(range(26))
        # union find is used to determine whether nodes are connected
        def find(x):
            if x != letters[x]:
                x = find(letters[x])
            
            return letters[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            letters[x] = y
        
        for equation in equations:
            a, b = ord(equation[0]) - ord("a"), ord(equation[3]) - ord("a")
            if equation[1] == "=":
                union(a, b) # make them connected!
        
        for equation in equations:
            a, b = ord(equation[0]) - ord("a"), ord(equation[3]) - ord("a")

            if equation[1] == "!":
                if find(a) == find(b): #they are connected
                    return False
        
        return True
