"""
Let’s define the diagonal neighbors of a given cell as the surrounding cells, with precisely one corner touching a corner of the given cell. The picture below shows the diagonal neighbors for the A cell.

(Image shows a 5x5 grid with the cell "A" and its four diagonal neighbors highlighted in green)

Given a board of cells containing a bubble of a specific color, your task is to emulate a bubble-popping game. In this game, the player can click a cell every turn to pop bubbles. After clicking the cell, the following happens:

The bubble in the clicked cell and bubbles of the same color among its diagonal neighbors are "popped" and removed, resulting in empty cells.

After bubbles are removed, the remaining bubbles in cells above the empty ones drop down to fill all empty cells.

After clicking the cell, the following happens:

The bubble in the clicked cell and bubbles of the same color among its diagonal neighbors are "popped" and removed, resulting in empty cells.

After bubbles are removed, the remaining bubbles in cells above the empty cells drop down to fill all empty cells.

Nothing happens if the clicked cell is empty (it does not contain a bubble).

An initial board of cells bubbles – a multidimensional array of integers representing cells containing different colored bubbles;

A set of player turns operations – 2-element integer arrays describing the coordinates (the row and column) of the cell that the player clicked on during each turn.

Return the state of the game board after all operations are processed. The output should be a multidimensional array of integers with the same size as bubbles, but replace the integers in all empty cells (without bubbles) with 0.

You are not expected to provide the most optimal solution, but a solution with time complexity not worse than
O(bubbles.length² · bubbles[0].length² · operations.length)
will fit within the execution time limit.
"""

# implies that the solution for this can be brute force 
# anytime something is removed, set it to zero 

# within a column, do swaps so all the zeros are at the back

# 123400578

# anything after a zero - can use a boolean to keep track of this 
# use a two pointer approach - one pointer to keep track of next element to replace, which starts off with a zero 
# one pointer to keep track of the next element that is replacing 

# l = 0
# hasSpace = false

# for idx in array:
#.  if element is zero, set hasSpace to true, set l to this value

# otherwise, if hasSpace (we don't want this to happen on the same round) and the element is not zero:
#  swap values 
#. increment left


def zero_swap(array: list):
    l = 0
    hasSpace = False 

    for r in range(len(array)):
        if hasSpace:
            if not array[r]:
                continue
            
            array[l], array[r] = array[r], array[l]
            l += 1

        elif not array[r]:
            hasSpace = True
            l = r

    return array

def solution(grid: list[list[int]], operations: list):
    directions = [1, -1]

    def is_valid(r: int, c: int):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
    
    def swap_column_values(c: int):
        l = len(grid) - 1
        hasSpace = False

        for r in range(len(grid)-1, -1, -1):
            if hasSpace:
                if not grid[r][c]:
                    continue
                
                grid[l][c], grid[r][c] = grid[r][c], grid[l][c]
                l -= 1

            elif not grid[r][c]:
                hasSpace = True
                l = r

    for r, c in operations:
        left_pops = 0
        right_pops = 0

        for dr in directions:
            new_r, new_c = r + dr, c - 1

            if is_valid(new_r, new_c) and grid[new_r][new_c] == grid[r][c]:
                grid[new_r][new_c] = 0
                left_pops += 1
            
        for dr in directions:
            new_r, new_c = r + dr, c + 1

            if is_valid(new_r, new_c) and grid[new_r][new_c] == grid[r][c]:
                grid[new_r][new_c] = 0
                right_pops += 1

        if left_pops:
            swap_column_values(c-1)
        
        if right_pops:
            swap_column_values(c+1)
        
        grid[r][c] = 0
        swap_column_values(c)
    
    return grid

        
test_cases = [
    {
        "name": "Basic click in middle with one matching diagonal",
        "bubbles": [
            [1, 2, 3],
            [4, 2, 6],
            [7, 2, 9]
        ],
        "operations": [[1, 1]],  # Click center (2)
        "expected": [
            [1, 0, 3],
            [4, 2, 6],
            [7, 2, 9]
        ]
    },
    {
        "name": "Click on corner, only self pops",
        "bubbles": [
            [1, 2],
            [3, 4]
        ],
        "operations": [[0, 0]],  # Only 1 pops
        "expected": [
            [0, 2],
            [3, 4]
        ]
    },
    {
        "name": "Click empty cell, nothing happens",
        "bubbles": [
            [1, 0],
            [2, 3]
        ],
        "operations": [[0, 1]],  # Cell is already 0
        "expected": [
            [1, 0],
            [2, 3]
        ]
    },
    {
        "name": "Gravity fills gap from top",
        "bubbles": [
            [1, 1],
            [1, 2],
            [1, 1]
        ],
        "operations": [[1, 0]],  # Pop 1 at (1,0), also diagonals (0,1), (2,1) = 2s
        "expected": [
            [0, 0],
            [1, 0],
            [1, 2]
        ]
    },
    {
        "name": "All same color, large board",
        "bubbles": [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]
        ],
        "operations": [[1, 1]],  # Clicking center pops 5 + all diagonal 5s
        "expected": [
            [0, 0, 0],
            [0, 5, 0],
            [5, 5, 5]
        ]
    },
    {
        "name": "Multiple operations",
        "bubbles": [
            [1, 2, 1],
            [2, 1, 2],
            [1, 2, 1]
        ],
        "operations": [[1, 1], [1, 1]],  # First center pops many 1s, then [0,1] pops 2 and diagonals
        "expected": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 2, 0]
        ]
    },
    {
        "name": "No diagonal matches, only one pop",
        "bubbles": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        "operations": [[1, 1]],
        "expected": [
            [1, 0, 3],
            [4, 2, 6],
            [7, 8, 9]
        ]
    }
]

for test in test_cases:
    result = solution([row[:] for row in test["bubbles"]], test["operations"])
    assert result == test["expected"], f"Failed: {test['name']}"
    print(f"Passed: {test['name']}")
