class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0

        while i<len(arr):
            if not arr[i]:
                arr.insert(i+1,0)
                i+=1
                arr.pop()
            i+=1
        
