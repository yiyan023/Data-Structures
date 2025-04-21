# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.flattenedList = deque()
        self.i= 0
    
    def nextHelper(self, lst):
        for val in lst:
            if val.isInteger():
                self.flattenedList.append(val)
            
            else:
                child = val.getList()
                self.nextHelper(child)
    
    def next(self) -> int:
        if self.flattenedList:
            return self.flattenedList.popleft()
        
        elif self.nestedList[self.i].isInteger():
            self.i += 1
            return self.nestedList[self.i - 1].getInteger()
        
        child = self.nestedList[self.i].getList()
        self.i += 1

        self.nextHelper(child)
        return self.flattenedList.popleft()
    
    def hasNextHelper(self, lst):
        count = 0

        if not lst:
            return count 
        
        for val in lst:
            if val.isInteger():
                count += 1
            
            else:
                child = val.getList()
                count += self.hasNextHelper(child)
        
        return count
    
    def hasNext(self) -> bool:
        while self.i < len(self.nestedList) and not self.nestedList[self.i].isInteger() and not self.hasNextHelper(self.nestedList[self.i].getList()):
            self.i += 1
        
        return self.i < len(self.nestedList) or self.flattenedList

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
