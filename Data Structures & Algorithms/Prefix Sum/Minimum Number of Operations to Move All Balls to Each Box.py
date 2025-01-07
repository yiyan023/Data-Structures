class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n 
        
        left_ops = 0
        left_balls = 0
        for i in range(n):
            res[i] += left_ops
            left_balls += (boxes[i] == '1')
            left_ops += left_balls

        right_ops = 0
        right_balls = 0
        for i in range(n - 1, -1, -1):
            res[i] += right_ops
            right_balls += (boxes[i] == '1')
            right_ops += right_balls
        
        return res
