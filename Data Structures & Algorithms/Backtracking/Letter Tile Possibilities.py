class Solution(object):
    def numTilePossibilities(self, tiles):
        # backtracking problem, where we need to find the total number of possibilies 
        possibilities = set()

        def backtrack(string, t):
            if string: # not empty
                possibilities.add(string)
            
            for i in range(len(t)): 
                backtrack(string + t[i], t[:i] + t[i + 1:])
        
        backtrack("", tiles)
        return len(possibilities)
        