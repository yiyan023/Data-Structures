# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # the celebrity has all incoming nodes (arrows) and no outgoing nodes (arrows)
        celebrity = 0

        for i in range(n):
            if knows(celebrity, i): # a celebrity cannot know anyone 
                celebrity = i

        for i in range(n): # check whether this celebrity is valid
            if celebrity != i:
                if knows(celebrity, i) or not knows(i, celebrity):
                    return -1
        
        return celebrity
