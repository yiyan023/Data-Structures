# recursive solution:

# dfs(r,c)
#   base case: if coords out of bounds, return 0
# otherwise, return 1 + dfs(r + 1, c) + dfs(r, c+ 1)


def unique_paths(m: int, n: int) -> int:

    def in_bounds(r: int, c: int):
        return 0 <= r < m and 0 <= c < n

    def dfs(r: int, c: int):
        if not in_bounds(r, c):
            return 0
        
        if (r,c) == (m-1,n-1):
            return 1
        
        return dfs(r + 1, c) + dfs(r, c + 1)

    return dfs(0,0)

print(unique_paths(3, 7))

# keep a grid of m x n 
# storing: the number of possible paths to reach that block

# base case 1
# the current block is equal to the sum of the left and right possible paths 
# if out of bounds, set to 0 

# return the last value (m-1, n-1) coords 
def unique_paths(m: int, n: int) -> int:
    dp = [1 for _ in range(n)]

    for _ in range(1, m):
        for i in range(n):
            dp[i] += dp[i-1] if i >= 1 else 0 
    
    return dp[-1]

print(unique_paths(15, 10))
assert unique_paths(1, 1) == 1
assert unique_paths(1, 5) == 1
assert unique_paths(3, 1) == 1
assert unique_paths(3, 2) == 3
assert unique_paths(3, 7) == 28
assert unique_paths(10, 10) == 48620
# assert unique_paths(15, 10) == 817190

print("✅ All Python tests passed.")
