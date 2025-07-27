from collections import deque

def shortestPathBinaryMatrix(grid: list[list[int]]):
    if grid[0][0]:
        return -1
    
    queue = deque()
    queue.append((0, 0, 1))

    directions = [[-1, 0], [1, 0], [0,-1], [0,1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    seen = set()
    seen.add((0, 0))

    def isValid(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and not grid[r][c]

    while queue:
        r, c, dist = queue.popleft()

        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return dist

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc

            if isValid(new_r, new_c) and (new_r, new_c) not in seen:
                seen.add((new_r, new_c))
                queue.append((new_r, new_c, dist + 1))
    
    return -1

grid = [[0,1],[1,0]]
print(shortestPathBinaryMatrix(grid))

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))

# Python test cases for shortestPathBinaryMatrix
from copy import deepcopy

def run_tests():
    tests = [
        ([[0]], 1),
        ([[1]], -1),
        ([[0,1],[1,0]], 2),
        ([[0,0,0],[1,1,0],[1,1,0]], 4),
        ([[0,0,0],[1,1,1],[1,1,0]], -1),
        ([[0,1,1],[1,0,1],[1,1,0]], 3)
    ]
    for i, (grid, exp) in enumerate(tests, 1):
        res = shortestPathBinaryMatrix(deepcopy(grid))
        assert res == exp, f'Test {i} failed: expected {exp}, got {res}'
    print('All Python tests passed!')

if __name__ == '__main__':
    run_tests()
