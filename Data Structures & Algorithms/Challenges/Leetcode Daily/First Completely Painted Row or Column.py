class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        matrix_hash = {}
        columns, rows = defaultdict(int), defaultdict(int)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                matrix_hash[mat[r][c]] = (r,c)
        
        for i, val in enumerate(arr):
            r, c = matrix_hash[val]
            columns[c] += 1
            rows[r] += 1

            if columns[c] == len(mat) or rows[r] == len(mat[0]): return i
        
