class Solution:
    def searchMatrix(self, matrix, target):
        # since this is sorted in non-decreasing order, we can use binary search 

        row = len(matrix) #2
        col = len(matrix[0]) #1
        l, r = 0, row * col - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid // col][mid % col]  == target:
                return True 
            
            elif matrix[mid // col][mid % col]  < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False