class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        a_set, b_set, c_set = set(), set(), set()

        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])

            if B[i] in a_set: c_set.add(B[i])
            if A[i] in b_set: c_set.add(A[i])
            res.append(len(c_set))
        
        return res
    
