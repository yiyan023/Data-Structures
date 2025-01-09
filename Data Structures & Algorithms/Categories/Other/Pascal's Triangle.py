class Solution(object):
    def generate(self, numRows):
        result = []
        
        for i in range(numRows):
            if i <= 1:
                result.append([1] * (i + 1))
            
            else:
                row = [1]

                for n in range(1, len(result[-1])):
                    row.append(result[-1][n] + result[-1][n-1])

                result.append(row + [1])
            
        return result 
