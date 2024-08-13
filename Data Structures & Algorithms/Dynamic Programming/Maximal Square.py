class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col+1) for r in range(row+1)]
        maxVal = 0

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = max(dp[r][c], 1+ min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1]))
                    maxVal = max(maxVal, dp[r][c])
        
        return maxVal ** 2
        
